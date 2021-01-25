import logging
import argparse
import os

from ttlv import Video

__version__ = "0.6.0"


def main():
    description = 'This package/cli tool saves webm video to upload Tiktok long videos above 60 seconds. Accepts video filepath and output video filepath.'
    parser = argparse.ArgumentParser(
        description=description,
        prog='ttlv',
        usage='%(prog)s [arguments]',
        allow_abbrev=False,
    )
    parser.add_argument("-v", "--version", help="show package version", action='version', version='%(prog)s {version}'.format(version=__version__))
    parser.add_argument('-i', '--input', help='Input Video filepath', type=str, default="")
    parser.add_argument('-o', '--output', help='Output video filepath', type=str, default="")

    args = parser.parse_args()
    input_path = args.input
    is_acceptable = input_path.lower().endswith(("mp4", "webm"))
    if input_path and is_acceptable:
        video = Video(input_path=input_path, output_path=args.output)
        video.save()
    elif input_path and not is_acceptable:
        logging.error("It is not a webm/mp4 video file.")
    else:
        logging.error("No input or output filepath provided.")

if __name__ == "__main__":
    main()