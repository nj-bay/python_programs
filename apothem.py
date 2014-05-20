#!/usr/bin/env python3
#NJ Shultz CS130a 

from math import *


#function for area
def area_calculator(n):
	area = (1/4.0)* n *1 * ((cos(pi/n))/(sin(pi/n)))
	return area



#function to find the differential between n and n+1
def increase(a,b):
	num = ((b-a)/a) * 100
	print ("**** num is " , num)
	return num 


#function to solve problem statement
def main(x,y):
	for n in range(x,y+1):
		a = area_calculator(n)
		b = area_calculator(n+1)
		print("a is " , a, "b is ", b)
		difference = increase(a,b)
		print("the difference between", n, n+1, " is " , difference)





if __name__ == '__main__':
	main(3,12)