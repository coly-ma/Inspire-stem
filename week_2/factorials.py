#programme to show factorials of numbers (assignment)
#date : 22/02/2024
#name : ivy nicole

factorial_num = 1
max_value = int(input("enter the max value : "))

for x in range(1,max_value + 1):
    factorial_num = factorial_num * x
    print(factorial_num)

print("\t")


# lesson....
for i in range(0,20,2):  #skips by two (even numbers)  ......steps
    print(i)

print("\t")

for i in range(1,20,2):  #odd numbers.........steps
    print(i)