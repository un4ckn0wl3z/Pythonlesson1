#!/usr/bin/env python
import sys

class Calculator :
	
	def __init__(self, ina, inb) :
		self.a = ina
		self.b = inb

	def add(self) :
		return self.a + self.b

	def mul(self) :
		return self.a * self.b





class SciCal(Calculator) :

	def power(self) :
		return pow(self.a, self.b) 





objCal = Calculator(int(sys.argv[1]), int(sys.argv[2]))

print "A + B = %d" % objCal.add()

print "A * B = %d" % objCal.mul()


objSci = SciCal(int(sys.argv[3]), int(sys.argv[4]))


print "A + B = %d" % objSci.add()
print "A * B = %d" % objSci.mul()
print "A ^ B = %d" % objSci.power()





