#!/usr/bin/env python

"""
def palcounter(num):
    counter = 0
    while (is_palindrome(num) is not True):
          numstr = str(num)
          revnumstr = numstr[::-1]
          revnumint = int(revnumstr)
          sum = revnumint + num
          num = sum
          counter +=1


    return counter

def is_palindrome(num):
    numstr + str(num)
    revnumstr = numstr[::-1]
    if numstr == revnumstr:
        return True
    else:
        return False

"""

# this is a comment

def reverse_num(num):
    num_str = str(num)
    num_str = num_str[::-1]
    return int(num_str)

def check_palindrome(num1, num2):
    return num1 == num2      

def palcounter(num):
    counter = 0
    while (True):
        num2 =  reverse_num(num)
        if num == num2:
            return counter, num
        else:
            num += num2    
        counter += 1

if __name__ == '__main__':
    print palcounter(195)
