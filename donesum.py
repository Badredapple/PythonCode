#donesum.py
total=0
s=input('Enter a number (or"done"):')
while s!='done':
	num=float(s)
	total=total+num;
	s=input('Enter a number (or"done"):')
print('The sum is'+str(total) )