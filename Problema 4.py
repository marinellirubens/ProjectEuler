#-*- encoding: utf-8 -*-
import math
import sys
sys.setrecursionlimit(30000)
PREMISSA='''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.'''

def main():
	number1 = 999
	number2 = 999
	StrNUmber = str(number1 * number2)
	StrNUmberArr = []
	while number1 > 100:
		if number2 > 100:
			number2 = number2 - 1
		else:
			number1 = number1 - 1
			number2 = 999
		StrNUmber = str(number1 * number2)
		if StrNUmber == StrNUmber[::-1]:
			StrNUmberArr.append([int(StrNUmber), number1,number2])
	print(sorted(StrNUmberArr),number1,number2 )

if __name__ == '__main__':
	main()
