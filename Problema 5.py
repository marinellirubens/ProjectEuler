#-*- encoding: utf-8 -*-
import math
import sys
sys.setrecursionlimit(30000)
PREMISSA='''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?'''

def main():
	n = 20
	while list(filter(lambda x: n % x != 0, range(11,21))) != []:
		n = n + 20	
	print(n)
if __name__ == '__main__':
	main()
