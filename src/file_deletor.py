# standard library imports
import glob
import os
import time


class FileDeletor:

    def __init__(self, del_dir: str):
        self.del_dir = del_dir

    def delete(self):
        time.sleep(5)
        files = glob.glob(os.path.join(self.del_dir, '*.txt'))
        for file in files:
            os.remove(file)
        return
