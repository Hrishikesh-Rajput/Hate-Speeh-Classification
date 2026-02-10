from hate_speech.logger import logging

from hate_speech.exception import CustomException
import sys

try: 
    a = 1 / "0"
except Exception as e:
    raise CustomException(e, sys) from e   
     

#logging.info("This is a demo log message.")