#!/usr/bin/python3
# Test case for adding two numbers
import unittest

from program import mul

class TestSum(unittest.TestCase):
	def test1(self):
		a1 = 30
		b1 = 20
		result = mul(a1, b1)
		self.assertEqual(result, 600)
		
	def test2(self):
		a2 = 15
		b2 = 8
		result = mul(a2, b2)
		self.assertEqual(result, 120)

	def test3(self):
		a3 = 50
		b3 = 60
		result = mul(a3, b3)
		self.assertEqual(result, 3000)

	def test4(self):
		a4 = 5
		b4 = 58
		result = mul(a4, b4)
		self.assertEqual(result, 20) 

	def test5(self):
		a5 = 58
		b5 = 42
		result = mul(a5, b5)
		self.assertEqual(result, 25)

if __name__ == '__main__':
	unittest.main()
