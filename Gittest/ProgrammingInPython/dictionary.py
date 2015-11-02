#leraning python dictionary   . this is code
bob={'pay':30000, 'job':'dev', 'age':42, 'name':'Bob Smith'}
sue={'job':'haw', 'pay':40000, 'age':45, 'name':'Sue Jones'}
people=[bob,sue]
for person in people:
    print(person['name'],person['pay'],sep=', ')
for person in people:
    if person['name'] == 'Sue Jones':
        print(person['pay'])
    else:
        print('I can not find the elments')
        break# look at this .
names=[person['name'] for person in people]
print(names)
lists=list(map((lambda x: x['name']),people))
print(lists)
sums=sum(person['pay'] for person in people)
print(sums)

for person in people:
    print(person['name'].split( )[-1])
    person['pay']*=1.10

for person in people:  print(person['pay'])


bob2={'name': {'first':'Bob','last':'smith'},
      'age':  42,
      'job':  ['software','writing'],
      'pay': (40000,50000)}
for job in bob2['job']: print(job)
print(bob2)

db={}
db['bob']=bob
db['sue']=sue
print (db)
import pprint
pprint.pprint(db)


for key in db:
    print(key, '=>',db[key]['name'])

for key in db:
    print(key, '=>',db[key]['pay'])

for key in db:
    print(db[key]['name'].split()[-1])
    db[key]['pay'] *=1.10

for record in db.values(): print(record['pay'])

x=[db[key]['name'] for key in db]
print(x)
y=[rec['name'] for rec in db.values()]
print(y)

#add a new record using dict
db['tom']=dict(name='Tom',age=50,job=None,pay=0)

print(db['tom'])
print(db['tom']['name'])
print(len(db))
