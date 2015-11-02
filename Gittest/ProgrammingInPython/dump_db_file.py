#__author__ = 'DKjack'
from make_db_file import loadDbase
db = loadDbase()#引用后面没有实际的指针；
for key in db:
    print(key, '=>\n', db[key])
print(db['sue']['name'])
