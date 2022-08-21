import psutil
from config import *
import time

def filesOfProcesses(processName):
    files = set()
    for proc in psutil.process_iter():
        if processName in proc.name():
            try:
                files |= set([i.path for i in proc.open_files()])
            except psutil.NoSuchProcess as e:
                pass
    return files


if __name__ == '__main__':
    files = set()
    while True:
        time.sleep(interval)
        newFiles = filesOfProcesses(processName)
        for file in (newFiles - files):
            print(file)
        files |= newFiles

