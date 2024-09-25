import sys
import logging
import src.logger

def error_message_detail(error, error_detail:sys):
    _, _, exc_tb = error_detail.exc_info() #3 important information, the 3rd give the line and where
    file_name = exc_tb.tb_frame.f_code.co_filename #given in the documentation
    error_message = "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message
    


        