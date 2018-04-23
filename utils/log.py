import os
import numpy as np

import utils

def get_log_path(log_name):
    return os.path.join(utils.storage_dir(), "logs", log_name+".txt")

def synthesize(array):
    return np.mean(array), np.std(array), np.amin(array), np.amax(array)

class Logger:
    def __init__(self, log_name):
        self.path = get_log_path(log_name)
        utils.create_folders_if_necessary(self.path)
        self.file = open(self.path, "a")
    
    def log(self, obj, to_print=True):
        obj_str = str(obj)

        if to_print:
            print(obj_str)

        self.file.write(obj_str+"\n")
