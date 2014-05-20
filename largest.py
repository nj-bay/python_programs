#!/usr/bin/env python3 

import re

def num_largest(path):
    a = []
    with open(path) as urantia:
        a = urantia.read().split()

    highest_number = 0

    for item in a:
        item = re.sub("[^0-9]", "", item)
        if item is not "":
            item = int(item)
        else:
            continue
 
        if item > highest_number:
            highest_number = item
            print(item)
    return highest_number



if __name__ == '__main__':
    path = '/home/nj_510/Documents/urantia'
    urantia_largest = num_largest(path)
    print(urantia_largest)	


