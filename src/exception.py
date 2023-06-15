import sys
from src.logger import logging

# To create the custom Error message that is having file name, line number and error description
def error_message_details(error,error_details:sys):
    _,_,exc_tb = sys.exc_info()
    # logging.info(f'exc_tb:{exc_tb}')
    file_name = exc_tb.tb_frame.f_code.co_filename
    # logging.info(f'file_name:{file_name}')
    line_no = exc_tb.tb_lineno
    # logging.info(f'line_no:{line_no}')
    error_message = '[ANIL] Error occured in python script name:[{0}],line number[{1}], error message[{2}]'.format(file_name,line_no,str(error))
    return error_message

# use system built in class Exception to defind user defined Exceptions
class CustomException_ANIL(Exception):
    def __init__(self,error_message,error_details:sys):
        super().__init__(error_message)
        self.error_message = error_message_details(error_message,error_details=error_details)
        # logging.info(self.error_message)

    def __str__(self):
        return self.error_message
    

# testing of exception.py
# if __name__=='__main__':
#     try:
#         a = 1/0
#         logging.info('Try block has been running till end : no Error')
#     except Exception as e:
#         print(e)
#         logging.info("exception has occured, except block has been running")
#         logging.info('Error::should be division by zero')
#         raise CustomException_ANIL(e,sys)
#     else:
#         logging.info('exception has not occured, else block has been running')
#     finally:
#         logging.info('finally block  has been running irrespective of error')
    

