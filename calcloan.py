#!/usr/bin/env python

import sys

f =open( sys.argv[1]).readlines()

def process_file(lines):
    for line in lines : 
        info = line.split(' ')
        loan_amount =  info[0] 
        interest = info[1]
        duration = info[2]
        total = 0
    return 0

if __name__=='__main__':
    process_file(f)

