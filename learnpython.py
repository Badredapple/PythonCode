width =input('Please input a width:')

price_width=10
item_width=width-price_width

header_format='%-*s%*s'
format       ='%-*s%*.2f'

print ('='*width)

print header_format % (item_width,'item',price_width 'Price')

print ('-'*width)

print format %(item_width, 'Apples' ,price_width,0.4)
print format %(item_width,'Pears',price_width,0.5)
print format %(item_width, 'Cantaloupes', price_width,1.92)
print format %(item_width, 'Dried Apricots(16 oz)',price_width,8)
print format %(item_width, 'Prunes (4 1bs)',price_width,12)

print ('='*width)

#实际上，2.5到3.5的区别很大，所以这里很多的类似的符号会出错，看看就好