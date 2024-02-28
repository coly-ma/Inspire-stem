#programme to solve geometric progression  (assignment)
#date : 20/02/2024
#name : ivy nicole


import math 


a = (input("enter value of first term : "))
r = (input("enter value of common ratio : "))
n = (input("enter value of number of terms : "))


nth_gp = a  * (r ** n-1)


print("the nth term of gp ", nth_gp)