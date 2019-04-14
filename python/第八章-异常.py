raise Exception
raise Exception('hehhehehe')

import exceptions
dir(exceptions)

class SomeCustomException(Exception):pass

try:
	x= input('Enter the first number:')
	y = input('Enter the second number:')
	print x/y
except ZeroDivisionError as e:
	print "The second number canot be zero"
except TypeError as sd:
	print "The second number is char"
finally:
	pass

try:
	x= input('Enter the first number:')
	y = input('Enter the second number:')
	print x/y
except (ZeroDivisionError,TypeError,NameError) as e:
	print e
finally:
	pass


class MuffledCalculator:
	muffled = False
	def calc(self,expr):
		try:
			return eval(expr)
		except ZeroDivisionError:
			if self.muffled:
				print 'Division by zero is illegal'
			else:
				raise


try:
	print "A simple task"
	print "what's something wrong"
else:
	print "Ah, it's a joe"

while True:
	try:
		x= input('Enter the first number:')
		y = input('Enter the second number:')
		value= x/y	
		print 'x/y is ',value
	except Exception as e:
		print e
	else:
		break

try:
	1/0
except NameError:


def fault():
	raise Exception('Something is wrong')


def ignore_exception():
	fault()

	
def handle_exception():
	try:
		fault()
	except:
		print 'handle_exception'
