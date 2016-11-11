#!/bin/python
# -*- coding: utf-8 -*-

print ("Hello,world!")
print (u'中文')

for age in range(30):
	if age >= 18:
		print "Adult, you age is %d"%age
	else:
		print "Teenager, your age is %d"%age
#sum = 0
#for i in range(101):
#	sum = sum + i
#print sum

def sum(n):
	s=0
	for i in range (n):
		s = s + n
	return s

sum = sum(30)

print sum
