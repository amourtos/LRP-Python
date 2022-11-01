
import unittest
import importlib
import calc
import sys


PKG_NAME = 'calc'
# supporess __pycache__ and .pyc files
sys.dont_write_bytecode = True


class TestCalc(unittest.TestCase):
    """Main test fixture for 'calc' module"""

    @classmethod
    def setUpClass(cls):
        """Performs module import and suite setup at test-runtime"""
        # check for python 3
        cls.assertGreaterEqual(cls, sys.version_info[0], 3)
        cls.module = importlib.import_module(PKG_NAME)

    def test_addition(self):
        """Test if the addition function is performing correct arithmetic operations"""
        self.assertEqual(calc.addition(2, 2), 4)
        self.assertEqual(calc.addition(6, 4), 10)
        self.assertEqual(calc.addition(50, 50), 100)
    
    def test_subtractioN(self):
        """Test if the subtraction function is performing correct arithmetic operations"""
        self.assertEqual(calc.subtraction(2 ,2) , 0)
        #TODO: Add more test cases here. 
        #       Follow the paradigm and try to understand what is happening here
        