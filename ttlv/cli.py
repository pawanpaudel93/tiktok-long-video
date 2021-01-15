import logging
import argparse
import os

from ttlv import Video

__version__ = "0.0.1"


def main():
    description = 'This package/cli tool saves webm video to upload Tiktok long videos above 60 seconds. Accepts video filepath and output video filepath.'
    parser = argparse.ArgumentParser(
        description=description,
        prog='ttlv',
        usage='%(prog)s [arguments]',
        allow_abbrev=False,
    )
    parser.add_argument("-v", "--version", help="show package version", action='version', version='%(prog)s {version}'.format(version=__version__))
    parser.add_argument('-i', '--input', help='Input Video filepath')
    parser.add_argument('-o', '--output', help='Output video filepath', type=str, default="")

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
        logging.error("No input or output filepath provided.")

if __name__ == "__main__":
    main()