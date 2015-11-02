#__author__ = 'DKjack'

"""
save in-memory database object to a file with custom formatting;
assume 'endrec','enddb.', and '=>' are not used in the data;
assum db is dict of dict;warning :eval() can be dangerous - it
runs string as code; could also eval() record dict all at once;
could also dbfile.write(key+'\n') vs print (key,file=dbfile);
"""

dbfilename = 'people-file'
ENDDB = 'enddb.'
ENDREC = 'endrec.'
RECSEP =  '=>'

def storeDbase(db,dbfilename = dbfilename):
    "formatted dump of database to flat file"
    dbfile = open(dbfilename,'w')
    for key in db:
        print(key,file=dbfile)
        for(name,value) in db[key].items():
            print(name +RECSEP +repr(value),file=dbfile)
        print(ENDREC,file=dbfile)
    print(ENDDB,file=dbfile)
    dbfile.close()

def loadDbase (dbfilename = dbfilename):
    "parse data to reconstruct database"
    dbfile = open(dbfilename)
    import sys
    sys.stdin = dbfile
    db = {}
    key=input()
    while key != ENDDB:
        rec={}
        field=input()
        while field != ENDREC:
            name, value =field.split(RECSEP)  #这里切片有问题，问题在于，前置要求返回2个值，后面才返回一个
            rec[name]=eval(value)
            field = input()
            db[key]  =rec
            key = input()
        return db


if __name__ == '__main__':
    from initdata import db
    storeDbase(db)
