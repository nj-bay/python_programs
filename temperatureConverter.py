#!/usr/bin/env python3

def farenheit_celsius (Tf):
    Tc = (5/9) * (Tf - 32)
    return Tc

def celsius_farenheit (Tc):
    Tf = (9/5) * (Tc + 32)   
    return Tf


if __name__=='__main__':
	print ("Temperature Converter")
	temp_to_convert = input("Enter a Temperature")
	temp_type = input("Enter a Type")
	if temp_type == Celsius:
	    newTemp = celsius_farenheit(temp_to_convert)
	else temp_type == Farenheit:
	    newTemp = farenheit_celsius(temp_to_convert) 
	print(newTemp)       	

	
