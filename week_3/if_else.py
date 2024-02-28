#use of if,else & elif in python
#date : 26/02/2024
#name : ivy nicole


age = 25
if age > 18 :
   print("you are allowed to drive")

print("\t")

if age > 18.6 :
    print("you are allowed to drive")

print("\t")

age = 17
if age > 18 :
    print("you are allowed to drive")  #does not print anything

print("\t")

salary = 45000
if salary > 30000 and salary < 50000 :
    salary = salary * 0.1 + salary
    print(salary)

print("\t")

home_county = "nyeri"
if home_county == "nyeri" or home_county == "kisii" :
    print("you get a busary")

print("\t")

grade = 70

if grade > 84 :
    print ("you are promoted to next class")
else :
     print("you repeat the class")


print("\t")

if grade >= 84  and grade <=90 :
    print("you win a calculator")
elif grade >= 50 and grade <= 83 :
    print("you win a mathematical set")
else :
    print("you get nothing !")

print("\t")

