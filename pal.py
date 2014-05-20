#!/usr/local/bin/python3
print("python working")
path='/users/abrick/resources/american-english-insane'

pals = []
with open(path) as ins:
        for line in ins:
                linestr = line.strip('\n')
                if len(linestr) == 7:
                        if linestr == linestr[::-1]:
                                print(linestr)# [0] for x in line.split('\n')) 
        #       print(line.split('\n')[::-1])

                                #pals.append(line)
#print(pals)
