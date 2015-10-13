#chapter1-unions.py
from ctypes import *

class barley_amount(union):
    _fields_=[
        ("barley_long",c_long),
        ("barley_int",c_int),
        ("barley_char",c_char *8),
        ]
    value= raw_input("Enter the amount of barley to put into the beer vat:")
    my_barley=barley_amount(int(value))
    print('barley amount as a long :%ld' % my_barley.barley_long)
