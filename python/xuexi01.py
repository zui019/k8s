months=[
     'January',
     'Feburary',
     'March',
     'April',
     'May',
     'June',
     'July',
     'August',
     'September',
     'October',
     'November']


endings=['st','nd','rd'] + 17*['th']\
       +['st','nd','rd'] + 7*['th']\
	   +['st']
	   
year= raw_input('Year: ')
month= raw_input('Month(1-12): ')
day= raw_input('Day(1-30): ')

month_number= int(months)
day_number= int(day)

month_name = months[month_name-1]
ordinal= day + endings[day_number-1]

print month_name + '  ' + ordinal + ',  ' + year

endings=['st','nd','rd'] + 17*['th']\
       +['st','nd','rd'] + 7*['th']\
	   +['st']
	   
year= raw_input('Year: ')
month= raw_input('Month(1-12): ')
day= raw_input('Day(1-30): ')

month_number= int(month)
day_number= int(day)

month_name = months[month_name-1]
ordinal= day + endings[day_number-1]

print month_name + '  ' + ordinal + ',  ' + year


sentence =raw_input("Sentence = :")
hello world
screen_width=80
text_width=len(sentence)
box_width=text_width+6
left_margin=(screen_width-box_width)//2
print
print ' ' * left_margin + '+' + '-' * (box_width-2) + '+'



database=[
['aa',11],
['bb',22],
['cc',33],
['dd',44],
['ee',55]
]

username =raw_input('User name: ')
aa
pin=raw_input('Pin number: ')
11
username,pin
if [username,pin] in database: print  'Access granted'



width=input('please enter width: ')
30

price_width=10
item_width=width- price_width

header_format='%-*s%*s'
format='%-*s%*.2f'

print  '=' * width

print header_format % (item_width,'item',price_width,'Price')

print '-' * width

print format % (item_width,'Apples',price_width,0.4)
print format % (item_width,'Pears',price_width,0.5)
print format % (item_width,'Cantaloupes',price_width,1.92)
print format % (item_width,'Dried Apricots (16 oz.)',price_width,8)
print format % (item_width,'Prunes(4 lbs)',price_width,12)

print '=' *width
 

phonebook={'Beth':'1992','Alice':'2341','Cecil':'3258'}

d={}
d['name']='chen'
d['age']='18'



people={'Chen':'1992','Alice':'2341','Cecil':'3258'}
lables = {
   'phone':'phone number',
   'addr':'address'
   }
   
name = raw_input('Names is: ')

request = raw_input('Phone number (p) or address (a)? ')

key = request

if request =='p' : key = 'phone'
if request =='a': key =='addr'

person = people.get(name,{})
label = lables.get(key,key)
result = people.get(key,'not avaliable')

print "person is: %s" %(person)
print "label is: %s" %(label)
print "result is: %s" %(result)
print "%s's %s is %s." %(name,label,result)


d= {'title':'Python web site','url':'http://www.python.org','spam':'0'}
d.items()


name = raw_input('What is your name:')
Mr. Chencheng
if name.endswith('Chencheng'):
	if name.startswith('Mr.'):
		print "erceng"
	else:
		print 'Hello MR.Chen'
elif name.endswith('Anan'):
	print 'Hello,Anan'
else:
	print 'bye bye'


name = raw_input('Please input your name: ')
ANAN
char1 = raw_input('Please input char1: ')
Chen
if char1 in name:
	print "%s is in %s" %(char1,name)
else :
	print "%s is not in %s" %(char1,name)


number=input('please input number between 1 and 10')
if number <=10:
	if number >=1:
		print "Great"
	else:
		print "wrong"
else:
	print "please exec again"
	

number=input('please input number between 1 and 10')
if  1  <  8 < 10:
 print 'ok'


age =10
assert 0<age < 10,'hahah'

names=['anne','beth','george',''demon']
ages=[10,20,30,40]
for i in range(len(names)):
	print i
	print names[i],'is',ages[i],'years old'

	
def test():
	print 'this is printed'
	return 'okoko'
	print 'this is not'
 

 -------------
def try_to_change(n):
	n = 'Mr. Gumby'


name = 'Mrs. Entity'


try_to_change(name)
name	

-------
def change(n):
	n[0]='Mr. chen'
	
	

names=['Mrs. Entity','Mrs. Thing']

change(names)



storage={}
storage['first']={}
storage['middle']={}
storage['last']={}

def lookup(data,lable,name):
	return data[lable].get[name]
	



