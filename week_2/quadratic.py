#programme to solve a quadratic equation
#date : 20/02/2024
#name ; ivy nicole


import math


a = float(input ("enter the coefficient of first term : "))
b = float(input("enter the coefficient of second term : "))
c = float(input("enter the constant : "))


discriminant = (b**2) - 4 * a * c


x_1 = (-b + (discriminant)) /2* a
x_2 = (-b - (discriminant)) /2* a


print("the  first solution of the quadratic equation ",x_1)
print("the second solution of the quadratic equation ",x_2)