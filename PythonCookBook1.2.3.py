#python cookbook
#python 1.2.3
record=[
    ('foo',1,2),
    ('bar','hello'),
    ('foo',3,4),
    ]

def do_foo(x,y):
    print('foo',x,y)

def do_bar(s):
    print('bar',s)


for tag, *args in record:
    if tag=='foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)
