__metaclass__ = type
class Person:
	def setname(self,name):
		self.name=name
	def getName(self):
		return self.name
	def greet(self):
		print "Hello,world! I'm %s. " %self.name

foo=Person()
bar=Person()
foo.setname('Luke Sky')
bar.setname('ANak in Sky')
foo.greet()
bar.greet()

class Class:
	def method(self):
		print "I'm is a boy!'"

def function():
	print "I'm not a ...."

instance =Class()
instance.method()
instance.method=function
instance.method()


class Bird:
	song = 'Squaawk'
	def sing(self):
		print self.song


class Mingzi:
	name = 'Sir Lancelot'
	def getname(self):
		print self.name

c=Mingzi()
c.name
c.getname()

class Secretive():
	"""docstring for Secretive"""
	def __inaccessible(self):
		print "Bet you canot see me..."
	def accessible(self):
		print "Bet you can see me ..."
  		self.__inaccessible()


def foo(x):	
	return x*x

foo = lambda x: x*x


class MemberCounter:
	"""docstring for MemberCounter:__init__(self, arg):
		super(MemberCounter:_init__()
		self.arg = arg"""
	members =0
	def init(self):
		MemberCounter.members += 1


class Filter:
	def init(self):
		self.blocked=[]
	def filter(self,sequence):
		return [x for x in sequence if x not in self.blocked]

class SPAMfilter(Filter):
	"""docstring for SPAMfiter"""
	def init(self):
		self.blocked=['SPAM']
		
f=Filter()
f.init()
f.filter([1,2,3])

s=SPAMfilter()
s.init()
s.filter(['SPAM','SPAM','SPAM','eggs','chen','SPAM'])


查看一个类是否是另一个类的子类
issubclass(SPAMfilter,Filter)



class Calculator:
	def caculate(self,expression):
		self.value = eval(expression)

class Talker:
	def talk(self):
		print 'Hi,my value is',self.value

class TalkingCalculator(Calculator,Talker):
	pass

tc = TalkingCalculator()
tc.caculate('1+2*3')
