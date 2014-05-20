#!/usr/bin/env python3

#module maintained by the interpreter and functions that interact strongly with
#the interpreter
import sys

# func_name : process_file
# arguments
# words : array of lines
# variables used 
# char_count - number of characters in entire file
# word_count - how many words there are in entire file
# line - element value of location in current loop

def process_file(words):
    char_count = 0
    word_count = len(words)
    for line in words: 
        char_count += len(line)
    return word_count, char_count/word_count
 

if __name__=='__main__':
    f = open(sys.argv[1]).readlines()
    print (process_file(f))  
    
