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

   def pow(x, y):
      if x is None:
         x = 0
      if y is None:
         y = 0
      if isinstance(x, (int, float)) == False or isinstance(y, (int, float)) == False:
         raise TypeError("Both parameters in the function need to be numeric")
      if x < 0 and isinstance(y, int) == False:
         raise ValueError("Undefined. If x is less than zero, y needs to be an integer.")
      return x**y
