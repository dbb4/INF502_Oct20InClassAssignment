from CalculatorClass import Calculator
import unittest, math

class TestCalculatorMethods(unittest.TestCase):

 # Testing the addition method in the Calculator Class

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

 # Testing the subtract method in the Calculator Class

    def test_subtract_positive(self):
        self.assertEqual(Calculator.subtract(3, 5), -2, "Test failed, subtracting (3,5) should equal -2")

    def test_subtract_none(self):
        self.assertEqual(Calculator.subtract(3, None), 3, "Test failed, subtracting (3,None) should equal 3")

    def test_subtract_decimals(self):
        difference = abs(Calculator.subtract(3.8, 3.5) - 0.3)
        self.assertLessEqual(difference, 0.001, "Test failed, subtracting (3.8,3.5) should less than or equal 0.3")

    def test_subtract_letters_from_letters(self):
        with self.assertRaises(TypeError, msg="Test failed, TypeError not raised when subtracting (\"def\",\"abc\") is called"):
            Calculator.subtract("def", "abc")

 # Testing the multiply method in the Calculator Class

    def test_multiply_positive(self):
        self.assertEqual(Calculator.multiply(3, 5), 15, "Test failed, multiply(3,5) should equal 15")

    def test_multiply_zero(self):
        self.assertEqual(Calculator.multiply(3, 0), 0, "Test failed, multiply(3,0) should equal 0")

    def test_multiply_one_negative_num(self):
        self.assertEqual(Calculator.multiply(3, -5), -15, "Test failed, multiply(3,-5) should equal -15")

    def test_multiply_two_negative_num(self):
        self.assertEqual(Calculator.multiply(-3, -5), 15, "Test failed, multiply(-3, -5) should equal 15")

    def test_multiply_none(self):
        self.assertEqual(Calculator.multiply(None, 5), 0, "Test failed, multiply(None, 5) should equal 0")

    def test_multiply_strings(self):
        with self.assertRaises(TypeError, msg="Test failed, TypeError not raised when multiplying (\"def\",\"abc\") is called"):
            Calculator.multiply("def", "abc")

    def test_multiply_list(self):
        with self.assertRaises(TypeError, msg="Test failed, TypeError not raised when multiplying (\"def\",\"abc\") is called"):
            Calculator.multiply([2,3,4], 1)

# Testing the divide method in the Calculator Class

    def test_divide_positive(self):
        self.assertEqual(Calculator.divide(10, 2), 5, "Test failed, divide(10, 2) should equal 5")

    def test_divide_by_zero_error(self):
        with self.assertRaises(ZeroDivisionError,msg="Test failed, ZeroDivisionError not raised when dividing by 0"):
            Calculator.divide(1, 0)

    def test_divide_result_type(self):
        self.assertEqual(Calculator.divide(3, 5), 0.6, "Test failed, divide(3, 5) should equal .6")

    def test_divide_floating_point_inputs(self):
        self.assertEqual(Calculator.divide(1.5, 0.3), 5, "Test failed, divide(1.5, 0.3) should equal 5")

    def test_divide_negatives(self):
        self.assertEqual(Calculator.divide(-5, -5), 1, "Test failed, divide(-5, -5) should equal 1")

    def test_divide_undefined(self):
        self.assertTrue(math.isnan(Calculator.divide(math.nan,1)), msg="Test failed, result not nan")

# Testing the "pow" (power) method in the Calculator Class

    def test_pow_positive(self):
        self.assertEqual(Calculator.pow(3, 2), 9, "Test failed, pow(3, 2) should equal 9")

    def test_pow_parameter_2_negative(self):
        self.assertEqual(Calculator.pow(2, -3), 0.125, "Test failed, pow(2, -3) should equal 0.125")

    def test_pow_parameter_2_zero(self):
        self.assertEqual(Calculator.pow(3, 0), 1, "Test failed, pow(3, 0) should equal 1")

    def test_pow_parameter_2_between_0_and_1(self):
        self.assertEqual(Calculator.pow(16, 0.25), 2, "Test failed, pow(16, 0.25) should equal 2")

    def test_pow_parameter1_negative_parameter2_odd(self):
        self.assertEqual(Calculator.pow(-2, 3), -8, "Test failed, pow(-2, 3)) should equal -8")

    def test_pow_parameter1_negative_parameter2_even(self):
        self.assertEqual(Calculator.pow(-2, 2), 4, "Test failed, pow(-2, 2)) should equal 4")

    def test_pow_parameter1_is_zero(self):
        self.assertEqual(Calculator.pow(0, 2), 0, "Test failed, pow(0, 2) should equal 0")

    def test_pow_parameters_are_positive_floats_less_than_1(self):
        self.assertEqual(Calculator.pow(0.0016, 0.25), 0.2, "Test failed, pow(0.0016, 0.25) should equal 0.2")

    def test_pow_param1_pos_floating_param2_neg_floating(self):
        self.assertEqual(Calculator.pow(0.00032, -0.2), 5, "Test failed, pow(0.00032, -0.2) should equal 5")

    def test_pow_parameters_both_neg_floating(self):
        with self.assertRaises(ValueError, "Test failed, pow(-0.00032, -0.2) should raise ValueError."):
            Calculator.pow(-0.00032, -0.2)

if __name__ == '__main__':
    unittest.main()
