import sys
from src.logger import logging

# To create the custom Error message that is having file name, line number and error description
def error_message_details(error,error_details:sys):
    _,_,exc_tb = sys.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_no = exc_tb.tb_lineno
    error_message = '[ANIL] Error occured in python script name:[{0}],line number[{1}], error message[{2}]'.format(file_name,line_no,str(error))
    return error_message

# use system built in class Exception to defind user defined Exceptions
class CustomException_ANIL(Exception):
    def __init__(self,error_message,error_details:sys):
        super().__init__(error_message)
        self.error_message = error_message_details(error_message,error_details=error_details)

    def __str__(self):
        return self.error_message