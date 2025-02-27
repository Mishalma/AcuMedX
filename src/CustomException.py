import sys
import traceback
from src.logger import logging

class CustomException(Exception):
    def __init__(self, error_message, error_details: Exception):
        super().__init__(error_message)  # Initialize the base Exception class
        _, _, exc_tb = sys.exc_info()  # Get exception details

        if exc_tb is not None:
            self.lineno = exc_tb.tb_lineno
            self.file_name = exc_tb.tb_frame.f_code.co_filename
        else:
            self.lineno = "Unknown"
            self.file_name = "Unknown"

        self.error_message = error_message

    def __str__(self):
        return "Error occurred in script [{0}] at line [{1}]: {2}".format(
            self.file_name, self.lineno, str(self.error_message)
        )
