#!/usr/bin/env python

import random

def roll():
    return random.randint(1,6)

if __name__=='__main__':
    num1 = roll()
    num2 = roll()
    print 'num1:', num1, 'num2:', num2, 'sum:', num1+num2
