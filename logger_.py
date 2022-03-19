from os import mkdir
import cs_ as ConfigAndStates
from datetime import datetime
from time import time

class Logger:
    def __init__(self):
        self.state = ConfigAndStates.LogState.NONE
        try:
            self.log_file = open(ConfigAndStates.LOGS_PATH + str(datetime.fromtimestamp(time())).replace(' ','').replace(':','') + ConfigAndStates.LOGS_EXT, 'w')
            self.state = ConfigAndStates.LogState.SUCCES
        except:
            try:
                mkdir(ConfigAndStates.LOGS_PATH.split('/')[0])
                self.log_file = open(ConfigAndStates.LOGS_PATH + str(datetime.fromtimestamp(time())).replace(' ','').replace(':','') + ConfigAndStates.LOGS_EXT, 'w')
                self.state = ConfigAndStates.LogState.SUCCES
            except:
                self.state = ConfigAndStates.LogState.FAILURE
    
    def close(self):
        self.log_file.close()
        del self
    
    def log(self, log_line: str):
        self.log_file.write(log_line + '\n')
