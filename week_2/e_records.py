#employee info  (assignment)
#date : 21/02/2024
#name : ivy nicole

e_name = input("enter employee name : ")
e_age = input("enter employee age : ")
e_salary = (float(input("enter employee salary : ")))
e_bonus = (float(input("enter employee bonus : ")))
 
print("\n")


print("the employee name ", e_name)
print("the employee age ", e_age)
print("the employee salary ", e_salary)
print("the employee bonus ", e_bonus)

print("\n")


s_increase = (float(input("enter value of increment (30%): ")))
s_decrease  = (float(input("enter value of decrement : ")))

print("\n")


print("the final salary", e_salary + e_bonus + s_increase - s_decrease)


