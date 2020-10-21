import math
from fractions import Fraction

class Calculator: 
   def add(x, y):
      if x is None:
         x = 0
      if y is None:
         y = 0
      if isinstance(x,(int,float)) == False or isinstance(y,(int,float)) == False:
         raise TypeError("Both parameters in the function need to be numeric")
      return x + y

   def subtract(x, y):
      if x is None:
         x = 0
      if y is None:
         y = 0
      if isinstance(x, (int, float)) == False or isinstance(y, (int, float)) == False:
         raise TypeError("Both parameters in the function need to be numeric")
      return x - y

   def multiply(x, y):
      if x is None:
         x = 0
      if y is None:
         y = 0
      if isinstance(x, (int, float)) == False or isinstance(y, (int, float)) == False:
         raise TypeError("Both parameters in the function need to be numeric")
      return x * y

   def divide(x, y):
      if x is None:
         x = 0
      if y is None:
         y = 0
      if isinstance(x, (int, float)) == False or isinstance(y, (int, float)) == False:
         raise TypeError("Both parameters in the function need to be numeric")
      return x / y

   def isEven(numberToTest):
      if isinstance(numberToTest, (int))==False:
         return False
      if numberToTest%2==0:
         return True
      
      return False 

   def pow(x, y):
      if x is None:
         x = 0
          
      if y is None:
         y = 0
          
      if isinstance(x, (int, float)) == False or isinstance(y, (int, float)) == False:
         raise TypeError("Both parameters in the function need to be numeric")
      
      negativeToAddBackIn = 1
      if x < 0 and abs(y)<1:
         exponentFraction = Fraction(y).limit_denominator()
         exponentDenominator = exponentFraction.denominator
         
         isEvenRoot = Calculator.isEven(exponentDenominator)
         
         if isEvenRoot:
            raise ValueError("{0} to the {1} power results in an imaginary number which is not supported by this function".format(x,exponentFraction))
         x=x*-1
         negativeToAddBackIn=-1
         
      return negativeToAddBackIn*(x**y)
