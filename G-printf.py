from ctypes import *
def print():
    msvcrt=cdll.msvcrt
    message_string="hello, world!\n"
    msvcrt.printf("Testing :%s",message_string)

