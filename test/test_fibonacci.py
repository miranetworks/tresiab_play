#!/usr/bin/env python

import sys
import os
import unittest

sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir, 'src'))

import fibonacci

#==================================================================================

class TestFibonacci(unittest.TestCase):
    
    def init(self):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testFib(self):
        """ 
        Test that fib function returns the correct list of fibonacci series for a given number
        """

        expected_list = [1, 1, 2, 3, 5, 8, 13, 21]
        fib30 = fibonacci.fib(30)
        self.assertEquals(fib30,
            expected_list,
            'The fibonacci series for the number 30 is not as expected, shoud be:\n%s\nfound:\n%s' %\
            (expected_list, fib30))

    def testFail(self):
        self.assertTrue(True,
            'It broke')

#==================================================================================

if __name__ == '__main__':
    unittest.main()
