#-*- encoding: utf-8 -*-
import functools
import sys
sys.setrecursionlimit(30000)
PREMISSA='''
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''

def main():
	n = 100
	squareSum = functools.reduce((lambda x, y: x + (y**2)), range(1,n + 1))
	SumSquare = functools.reduce((lambda x, y: x + y), range(1,n + 1)) ** 2

	print(SumSquare - squareSum)

if __name__ == '__main__':
	main()
