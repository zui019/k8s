storage={}
storage['first']={}
storage['middle']={}
storage['last']={}

me = 'Magunus lie Hetland'
storage['first']['one']=[me]
storage['middle']['two']=[me]
storage['last']['three']=[me]

初始化字典的函数init
def init(data):
	data['first']={}
	data['middle']={}
	data['last']={}
使用方式：
init(storage)

def lookup(data,lable,name):
	return data[lable].get(name)

lookup(storage,'last','three02')

def store(data,full_name):
	names=full_name.split()
	if len(names)==2: names.insert(1,'')
	lables='first','middle','last'
	for lable,name in zip(lables,names):
		people = lookup(data,lable,name)
		if people:
			people.append(full_name)
		else :
			data[lable][name]=[full_name]

def change(n):
	n[1]='Mr. chen'


names=['MRS. Yang','MISS. muli']
change(names)

def hello_1(greeting,name):
	print '%s,%s' %(greeting,name)

def hello_2(name,greeting):
	print '%s,%s' %(name,greeting)
	
def hello_3(greeting='Hello',name='world'):
	print '%s,%s' %(greeting,name)

	
store(data,name1,name2,name3)

def print_params(*params):
	print params
	
def print_params_2(title,**params):
	print title
	print params
	
	
def add01(a1,a2,a3=0,a4=0,a5=0,a6=0):
	return a1+a2+a3+a4+a5+a6


params=(1,2,4,5,5)

add01(*params)


args={'name':'Mr. chen','Age':32}

def with_star(**kwds):
	print kwds['name'],' is ',kwds['Age'],' old'

with_star(**args)

def with_nostar(kwds):
	print kwds['name'],' is ',kwds['Age'],' old'

with_nostar(args)

x =1 
scope= vars()

scope['x']

x

def foo():
	x=42
	print x

此处x的值为引用全局变量的值
def foo(x):
	x=100
	return globals()['x']+y
	
将函数的局部变量申明为全局变量

def change_globals():
	global x
	x=x+100

def foo():
	def bar():
		print "hello world!"
	bar()

def multiplier(factor):
	def multiplyByFactor(number):
		print number
		print factor
		return number * factor
	return multiplyByFactor

double=multiplier(2)
double(5)
	
multiplier(3)(6)

递归

def rec(y):
	return rec()

累加从1 加到100
x=1
y=0
while x<=100:
	y+=x
	x += 1
	print y
	

def leijia(n):
	if n ==1:
		return 1
	else:
		return n+leijia(n-1)
	
	
x=1
y=1
for i in range(1,101):
	y=y*i
	print y

从1 乘到100
def factorial(n):
	result=n
	for i in range(1,n):
		result *= i
	return result
	

def factorial(n):
	if n ==1:
		return 1
	else:
		return n*factorial(n-1)


def power(x,n):
	result=1
	for i in range(n):
		result *= x
	return result


def power(x,n):
	if n ==0:
		return 1
	else :
		return x*power(x,n-1)


seq=[34,23,25,27,12,15,62,75,86,1,5,9,7]
seq.sort()

		
def func(x):
	return x.isalnum()
	

seq =['foo','x65','*(','67']
filter(func,seq)

[x for x in seq if x.isalnum()]

from random import choice
x= choice(['hello world',[1,2,'a','c','e']])

def add(x,y):
	return x+y

def length_message(x):
		print "the length of",repr(x),"is",len(x)

		