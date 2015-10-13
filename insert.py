#insertline.py
import os
def add_to_story(line,fname='story.txt'):
    f=open(fname, 'a')
    f.write(line)
    f.close()
def insert_title(title, fname='story.txt'):
    f=open(fname,'r+')
    temp=f.read()
    temp=title+'\n\n'+temp
    f.seek(0)
    f.write(temp)
    f.close()
