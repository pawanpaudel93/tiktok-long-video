import binascii
import logging
import argparse
import re
import os

__version__ = "0.0.1"

logging.basicConfig(level=logging.ERROR, format='%(levelname)s - %(message)s')

class Video:

    def __init__(self, input_path, output_path=""):
        self.input_path = input_path
        self.output_path = output_path if output_path else re.compile(".webm", re.IGNORECASE).sub("-tlv.webm", input_path)

    def save(self):
        with open(self.input_path, "rb") as input_file:
            hexdata = binascii.hexlify(input_file.read())
        try:
            index = hexdata.index(b"4489")
        except ValueError:
            logging.error("Video cannot be saved as TikTok long video.")
        else:
            if index != -1:
                hexdate  = hexdata[:index+4] + b"8840B07DB000" + hexdata[index+4+12:]
                with open(self.output_path, "wb") as f:
                    f.write(binascii.unhexlify(hexdate))
            else:
                logging.error("Video cannot be saved as TikTok long video.")

def main():
    description = 'This package saves webm video to upload Tiktok long videos above 60 seconds. Accepts video filename/filepath and output video name/filepath.'
    parser = argparse.ArgumentParser(
        description=description,
        prog='tlv',
        usage='%(prog)s [arguments]',
        allow_abbrev=False,
    )
    parser.add_argument("-v", "--version", help="show package version", action='version', version='%(prog)s {version}'.format(version=__version__))
    parser.add_argument('-i', '--input', help='Video filename/filepath')
    parser.add_argument('-o', '--output', help='Output video filename/filepath', type=str, default="")

    args = parser.parse_args()
    input_path = args.input
    if input_path and "webm" in input_path.lower():
        if os.path.isfile(input_path):
            video = Video(input_path=input_path, output_path=args.output)
            video.save()
        else:
            logging.error("File Does Not Exist.")
    elif input_path and "webm" not in input_path.lower():
        logging.error("It is not a webm video file.")
    else:
        logging.error("No input or output filename/filepath provided.")

if __name__ == "__main__":
    main()