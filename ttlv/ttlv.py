import binascii
import logging
import re

logging.basicConfig(level=logging.ERROR, format='%(levelname)s - %(message)s')

class Video:

    def __init__(self, input_path: str, output_path: str=""):
        self.input_path = input_path
        self.output_path = output_path if output_path else re.compile(".webm", re.IGNORECASE).sub("-ttlv.webm", input_path)

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
