import binascii
import logging
import re

logging.basicConfig(level=logging.ERROR, format='%(levelname)s - %(message)s')

class Video:

    def __init__(self, input_path: str, output_path: str=""):
        self.input_path = input_path
        self.output_path = output_path if output_path else re.compile(".webm", re.IGNORECASE).sub("-ttlv.webm", input_path)
        self._hexdata = b""
    
    def _get_extension(self):
        return self.input_path.split(".")[-1].lower()
    
    def _modify_webm(self):
        try:
            index = self._hexdata.index(b"4489")
        except ValueError:
            return
        else:
            if index != -1:
                self._hexdate  = self._hexdata[:index+4] + b"8840B07DB000" + self._hexdata[index+4+12:]
        return True
    
    def _modify_mp4(self):
        try:
            index = self._hexdata.index(b"6d766864")
        except ValueError:
            return
        else:
            if index != -1:
                self._hexdate  = self._hexdata[:index+24+8] + b"000003E800003A98"  + self._hexdata[index+24+8+16:]
        return True

    def save(self):
        with open(self.input_path, "rb") as input_file:
            self._hexdata = binascii.hexlify(input_file.read())
        extension = self._get_extension()
        if extension == "mp4":
            is_modified = self._modify_mp4()
        else:
            is_modified = self._modify_webm()
        if is_modified:
            with open(self.output_path, "wb") as f:
                f.write(binascii.unhexlify(self._hexdate))
        else:
            logging.error("Video cannot be saved as TikTok long video.")
