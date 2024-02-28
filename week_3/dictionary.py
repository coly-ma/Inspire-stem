#
#you can type on another line......

laptop = {"make":"lenovo","colour":"black","weight":"1.2","year":"2015"}

print(laptop["make"])
print(laptop["colour"])
print(laptop["year"])

print("\n")

laptop["colour"] = "fuschia"
laptop["year"] = "2030"

laptop["size"] = "1200mm x 600mm"
print (laptop)

print("\n")

del laptop["colour"]
print(laptop)
"""
for key , value in laptop.items():
    print(key)
    print("\n")
    print(value)
"""

siz_laptop = laptop.copy()
print(laptop)