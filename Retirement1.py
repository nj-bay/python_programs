#!/usr/bin/env python

# NJ Shultz, 131A, write a program that models retirement savings after 40 years.

import random


#Inputs: goFor - number of years, money - cumulative total, 
#minRange, maxRange - interest range, addAmount - interest to add per year
#Returns: a list with record of total money for each year
def retirement_calc(goFor,money,minRange,maxRange,addAmount):
    money_hist = []

    for i in range (0,goFor):
	    money += addAmount
	    money *= random.random() * (maxRange - minRange) + minRange
	    money_hist.append(money)

    return money_hist

#Define variable a that is the money list and print out in defined year set
if __name__ == '__main__':
    a = retirement_calc(40,0,.9,1.15,5000)
    for i in range(0,len(a)):
        print "year:", i+1, " balance:", a[i]
