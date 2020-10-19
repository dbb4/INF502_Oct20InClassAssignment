from CalculatorClass import Calculator
import unittest

class TestStringMethods(unittest.TestCase):

    def test_add_positive(self):
        self.assertEqual(Calculator.add(3,5),8,"Test failed, add(3,5) should equal 8")
        
    def test_add_negative(self):
        self.assertEqual(Calculator.add(-3,5),2,"Test failed, add(-3,5) should equal 2")

    def test_add_zero(self):
        self.assertEqual(Calculator.add(0,-5),-5,"Test failed, add(0,-5) should equal -5")

    def test_add_none(self):
        self.assertEqual(Calculator.add(None,-5),-5,"Test failed, add(None,-5) should equal -5")

    def test_add_none_reverse(self):
        self.assertEqual(Calculator.add(3,None),3,"Test failed, add(3,None) should equal -3")

    def test_add_decimals(self):
        self.assertEqual(Calculator.add(3.5,3.8),7.3,"Test failed, add(3.5,3.8) should equal 7.3")
        
    def test_add_letters(self):
        with self.assertRaises(TypeError,msg="Test failed, TypeError not raised when add(3.5,\"abc\") is called"):
            Calculator.add(3.5,"abc")
            
    def test_add_letters_to_letters(self):
        with self.assertRaises(TypeError,msg="Test failed, TypeError not raised when add(\"def\",\"abc\") is called"):
            Calculator.add("def","abc")

        
if __name__ == '__main__':
    unittest.main()
