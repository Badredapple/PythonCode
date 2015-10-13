#write.py
import os
def make_story():
    if os.path.isfile('story.txt'):
        print('story.txt is already exists')

    else:
        f=open('story.txt','w')
        f.write('May had a little lamb,\n')
        f.write('and then she had some more .\n')



