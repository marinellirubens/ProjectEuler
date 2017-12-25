#-*- encoding: utf-8 -*-
import functools
import sys
sys.setrecursionlimit(30000)
PREMISSA='''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''

def main():
	n = [2]
	i = 3
	while len(n) < 10001:
		if IsPrime(i):
			n.append(i)
			#print(i)
		i += 2
	print(n)




def IsPrime(Number, multiplier = 3):
	#print(Number, multiplier)
	if Number <= 3:
		return True
	elif Number % 2 == 0:
		return False
	elif Number <= multiplier:
		return True
	elif Number % multiplier == 0:
		return False
	else:
		return IsPrime(Number, multiplier + 2)

if __name__ == '__main__':
	main()
