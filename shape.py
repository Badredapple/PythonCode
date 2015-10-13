#shape.py
"""A collection of functions
    for printing basic shapes,
"""
CHAR='*'
def rectangle(height,width):
    """print a rectangle."""
    for row in range(height):
        for col in range(width):
            print(CHAR, end=' ')
        print()
def square(side):
    """Pprint a square"""
    rectangle(side, side)
def triangle(height):
    """ptrints a right triangle"""
    for row in range(height):
        for col in range(1,row+2):
            print(CHAR, end=' ')
        print()

if __name__ == '__main__':
    rectangle(2,3)