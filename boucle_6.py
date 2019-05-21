
def suite():
   x = 0
   y = 1
   for i in range(10):
        z = x + y 
        x = y
        y = z 
        print(x, "+", y, "=", z )
suite()
  