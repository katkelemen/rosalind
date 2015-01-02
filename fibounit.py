# -*- coding: utf8 -*-
import unittest

#1,1,2,3,5,8,13,21...
def fibo(n):
    if n == 1 or n == 0:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

def fibok(n,k):
    if n == 1 or n == 0:
        return 1
    else:
        return fibok(n-1,k) + fibok(n-2,k) * k

def fibolist(n):
    a = 1
    b = 1
    for i in range(n-1):
        b, a = a + b, b
    return b

class TestFibo(unittest.TestCase):

####################################

    def test_simple(self):
        self.assertTrue(fibo)
        self.assertEqual(fibo(0),1)
        self.assertEqual(fibo(1),1)
        self.assertEqual(fibo(2),2)
        self.assertEqual(fibo(3),3)

    def test_simplek(self):
        self.assertTrue(fibok)
        self.assertEqual(fibok(0,2),1)
        self.assertEqual(fibok(1,2),1)
        self.assertEqual(fibok(2,2),3)
        self.assertEqual(fibok(3,2),5)


    def test_simplelist(self):
        self.assertTrue(fibolist)
        self.assertEqual(fibolist(0),1)
        self.assertEqual(fibolist(1),1)
        self.assertEqual(fibolist(2),2)
        self.assertEqual(fibolist(3),3)

####################################

if __name__ == '__main__':
    unittest.main()