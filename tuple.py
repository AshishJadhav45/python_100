tup = (2,2,4,25,6,43,14,6)
tup2 = ("red","Green","Blue")
print(tup)
print(tup2)
print(tup+tup2)

#check for items

country = ("Spain", "Italy", "India", "England", "Germany")
if "Russia" in country:
    print("Russia is present.")
else:
    print("Russia is absent.")


#index in tuple 

country = ("india","itly","spain","america","england")
tem = country.index("india")
print(tem)