friends = ["abima","sandra","elsie","brandon","lorna","suzzie"]

for friend in friends :
    print(friend)


print("\n")

enemies = friends[:]   #to copy one list into another

fruits = ["mango","banana","pawpaw","kiwi","lime","apple"]
#slice the list ie get part of the list
print(fruits[0:3])

print("\n")

del fruits[0] #delete
print(fruits)

print("\n")

squares = [] #initialises an empty list

for x in range(0,11):
    squares.append(x**2)

print(squares)