#initialize data to be stored in  files,pickles


#records
bob={'name':'Bob Smith', 'age':42, 'pay':30000, 'job':'dev'}
sue={'name':'Sue Jones', 'age':45, 'pay':40000, 'job':'hdw'}
tom={'name':'Tom',       'age':52, 'pay':700000   , 'job':None}

#database
db={}
db['bob']=bob
db['sue']=sue
db['tom']=tom

#if _name_=='_main_':#using in when it used as a script
for key in db:
    print(key,'=>\n',db[key])