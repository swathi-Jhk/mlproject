import sys
import logging

def error_message_detail(error,error_detail: sys):
    _,_,exc_tb=error_detail
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(file_name,exc_tb.tb_lineno,str(error))


class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message
    


# if __name__=="__main__":

#     try:
#         a=1/0
#         print("a",a)
#     except ZeroDivisionError as zero_div_error:
#         exception_str="Zero division error occured"
#     except Exception as e:
#         print("Exception object :",e)
#         if hasattr(e, '__str__'):
#             try:
#                 exception_str=str(e)
#             except Exception as str_err:
#                 print("Error converting exception to string",str_err)
#         else:
#              exception_str = "Exception object cannot be converted to a string"
#         raise CustomException(exception_str,sys.exc_info())
    
# # Add logging to log the exception message
# logging.basicConfig(filename='error.log', level=logging.ERROR)
# logging.error(exception_str)
# print("Exception message logged:", exception_str)