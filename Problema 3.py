#-*- encoding: utf-8 -*-
import math
import sys
sys.setrecursionlimit(30000)
PREMISSA='''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?'''

def main(Number):
	i = 3
	while i * i < Number:
		while Number % i == 0:
			#print(Number)
			Number = Number / i
		i = i + 1
		#print(i)
	print(Number) 



if __name__ == '__main__':
	main(600851475143)
