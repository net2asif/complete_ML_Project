#logger is used to log the error in python
import logging
from datetime import datetime
now = datetime.now()
import os
import sys

log_file=f"{now.strftime('%m_%d_%Y_%H_%M_%S')}.log"# log file is created with current date and time
logs_path = os.path.join(os.getcwd(),"logs",log_file) # logs folder is created in current working directory
os.makedirs(logs_path,exist_ok=True)# logs folder is created 

log_file_path=os.path.join(logs_path,log_file)

logging.basicConfig(
    filename=log_file_path,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occurred python script name [{0}] line number [{1}] error message [{2}]".format(file_name,exc_tb.tb_lineno,str(error))
    return error_message

# if __name__=="__main__":
#     logging.info("Logging has started")