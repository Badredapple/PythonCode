#list.py
import os

def list_cwd():
    return os.listdir(os.getcwd())
def files_cwd():
    return [p for p in list_cwd()
            if os.path.isfile(p)]
def folders_cwd():
    return [p for p in list_cwd()
            if os.path.isdir()]
