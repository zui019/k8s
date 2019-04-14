class FooBar:
	def init(self,value=100):
		self.someval=value

class Foobar:
	def __init__(self,value=42):
		self.someval=value


class A:
	def hello(self):
		print "Hello.I'm A"
class B(A):
#	def ():
		pass

class C(A):
	def hello(self):
		print "I'm B"


class Brid:
	def __init__(self):
		self.hungry=True
	def eat(self):
		if self.hungry:
			print 'ANANNA'
			self.hungry=False
		else:
			print 'NO,thanks'

class SongBird(Brid):
	def __init__(self):
		self.sound='Squawk'
	def sing(self):
		print self.sound

class SongBird(Brid):
	def __init__(self):
		Brid.__init__(self)
		self.sound = 'Squawk'
	def sing(self):
		print self.sound

__metaclass__=type
class Brid:
	def __init__(self):
		self.hungry=True
	def eat(self):
		if self.hungry:
			print 'ANANNA'
			self.hungry=False
		else:
			print 'NO,thanks'
class SongBird(Brid):
	def __init__(self):
		super(SongBird,self).__init__()
		self.sound='Squawk'
	def sing(self):
		print self.sound


def checkIndex(key):
	if not isinstance(key,(int,long)):raise TypeError
	if key <0:raise IndexError
class ArithmeticSequence:
	def __init__(self,start=0,step=1):
		self.start =start
		self.step = step
		self.change = {}
	def __getitem__(self,key):
		checkIndex(key)
		try:
			return self.change[key]
		except KeyError:
		return self.start + key*self.step
	def __setitem__(self,key,value):
		checkIndex(key)
		self.change[key] = value


class CounterList(list):
	def __init__(self,*args):
		super(CounterList,self).__init__(*args)
		self.counter =0
	def __getitem__(self,index):
		self.counter +=1
		return super(CounterList,self).__getitem__(index)

class CounterList(list):
	def __init__(self,*args):
		super(CounterList,self).__init__(*args)
		self.counter =0
		self.cheng=2
	def __getitem__(self,index):
		print "hahahahha22222"
		self.counter +=1
		return super(CounterList,self).__getitem__(index)


class Rectagngle:
	def __init__(self):
		self.width=0
		self.height =0
	def setSize(self,size):
		self.width,self.height = size
	def getSize(self):
		return self.width,self.height

__metaclass__=type
class Rectagngle:
	def __init__(self):
		self.width=0
		self.height =0
	def setSize(self,size):
		self.width,self.height = size
	def getSize(self):
		return self.width,self.height	
	size= property(getSize,setSize)

__metaclass__=type
class MyClass:
	def smeth():
		print "This is a static method"
	smeth=staticmethod(smeth)
	def  cmeth(cls):
		print "This is a class method",cls
	cmeth = classmethod(cmeth)

__metaclass__ = type
class MyClass:
	@staticmethod
	def smeth():
		print "This is a static method"

	@classmethod
	def cmeth(cls):
		print "This is a class method of",cls


class Rectagngle:
	def __init__(self):
		self.width=0
		self.height=0
	def __setattr__(self,name,value):
		if name =='size':
			self.width,self.height = value
		else:
			self.__dict__[name] = value
	def __getattr__(self,name):
		if name == 'size':
			return self.width,self.height
		else:
			raise AttributeError


class Fibs:
	def __init__(self):
		self.a=0
		self.b=1
	def next(self):
		self.a,self.b=self.b,self.a+self.b
		return self.a
	def __iter__(self):
		return self

for i in fib.next():
	if i >1000:
		print i
		break


it= iter(range(1,100))
for i in it:
	if i > 98:
		i+=1
		print i
		break

class TestIterator:
	value = 0
	def next(self):
		self.value += 1
		if self.value >10:
			raise StopIteration
		return self.value
	def  __iter__(self):
		return self

nested =[[1,2,3,5],[3,4],[5],[5],[5],[5]]

def flatten(nested):
	for sublist in nested:
		for element in sublist:
			yield element

aa=flatten(nested)

for num in flatten(nested):
	print num

def flatten(nested):
	try:
		for sublist in nested:
			for element in sublist:
				yield element
	except TypeError:
		yield nested



nested =[1]

for num in flatten(nested):
	print num

