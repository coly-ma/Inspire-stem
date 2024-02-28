#programme to solve the surface area of a cylinder  (assignment)
#date : 20/02/2024
#name : ivy nicole


import math

pi = 3.142
r = (float(input("enter value of radius : ")))
h = (float(input("enter value of height : ")))


sa_cylinder = ( 2 * pi * r * h) + ( 2 * pi * (r**2))



print("the surface area of a cylinder ", sa_cylinder)