#strings in python
#date : 22/02/2024
#name : ivy nicole


city = "nairobi"

print(city[0]) #n
print(city[1]) #a
print(city[2]) #i
print(city[3]) #r
print(city[4]) #o
print(city[-2]) #b
print(city[-1]) #i


#convert to uppercase

print(city)
print("\n") #prints a new line
print(city.upper())


name ="IVY NICOLE"

print(name.lower()) #converts string to lower case


town = "  naivasha"

print(town)
print("\t") #prints new tab
print(town.strip())

town = "      naivasha     "

print(town.strip())


#add two strings

f_name = "ivy"
s_name = "nicole"

full_name = f_name + s_name

print(full_name)


#replacing a character

fruit = "orange"

print(fruit.replace("o","y"))

print("\t")

fruit = "banana"

print(fruit.replace("a","i"))

print("\t")


subject = "physical,sciences"

print(subject.split(","))

print("\t")


age = 18
height = 1.2


print("i am {0} years old and {1} metres tall".format(age,height))

print("\t")

name = "ivy nicole"
print(len(name))  #len prints the number of characters in a string 

print ("\t")

activity = "dancing"
print("my hobby is %s" %(activity))  #formating method borrowed from cc+

print("\t")

height = 1.23
print("my height is %5.4f" %(height))   #prints upto 4 decimal points >> that (.4)

print("\t")

print(f"my full name is {name}")  #another string format

print("\t")

school = "engineering"
course = "electrical engineering"

print("i am studying {course} in the school of {school}" .format(course = "medicine"  ,school = "human sciences"))