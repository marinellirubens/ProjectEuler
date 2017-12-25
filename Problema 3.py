#-*- encoding: utf-8 -*-
import math
import sys
sys.setrecursionlimit(15000)
PREMISSA='''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?'''

def main(Number):
	Square = math.sqrt(Number)
	MaxNumber = []
	#print(int(Square))
	for x in range(3,int(Square),2):
		#print(x, IsPrime(x,3))
		if IsPrime(x,3):
			MaxNumber.append(x)

	result = 0
	print(result)
	print(MaxNumber)
	MaxNumber.reverse()
	for x in MaxNumber:
		if Number % x == 0:
			result = x
			break
	print(result)

def IsPrime(NumberPrime, Compare):
	if NumberPrime <= Compare:
		return True
	elif NumberPrime % Compare == 0:
		return False
	else:
		return IsPrime(NumberPrime, Compare + 2)

if __name__ == '__main__':
	main(600851475143)