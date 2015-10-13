#global_errror.py
name='jack'
def say_hello():
    print('Hello'+name+'!')
def change_name(new_name):
    global name
    name=new_name
