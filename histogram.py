#!/usr/bin/env python3


import random


def random_number():
    return random.randint(0,19)

#scaling results in histogram tally to a factor of 10
#use scale number to print asterisk
def print_asterisk(value):
    #used double slash for python 3 integer division
    value = value // 10 

    #creating output string
    output = ''
    
    #loop to append asterisks
    for i in range(0, value): 
        output += '*'
        
    return output 
    






if __name__=='__main__':
    #declare array for samples
    sample_array = [0] * 20

    #took 10000 samples and incremented the array
    #stores the tallies   
    for i in range(0,10000):
        sample_array[random_number()] += 1

    #print out the asterisk for each represented number
    for i in range(0,20):
        #passing tally into print_asterisk function
        #and then print it
        print(print_asterisk(sample_array[i])) 
        

