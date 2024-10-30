name = 'Fred Scarcelli'
print(name[0])

#len([start:stop:step])
last_name = name[5:(len(name))]
last_name = name[5:]
funky_name = name[::2]
reverse_name = name[::-1]

print(funky_name)
print(last_name)
print(reverse_name)

website1 = "http://www.google.com"
website2 = "www.wikipedia.com"

slice_comHTTP = slice(11, -4)
slice_semHTTP = slice(4, -4)

print(website1[slice_comHTTP])
print(website2[slice_semHTTP])

#list - sequence of mutable values
Food = ['pizza', 'hamburger', 'milkshake']

print(Food)
print(Food[2])

Food[0] = "sushi"
Food.append('ice cream')
Food.insert(1, "cake")
print(Food)
Food.sort()
print(Food)


"""
# LIST 2D
# guloseimas = ['pizza','hamburger','milkshake']
# carne = ['file','busteca']

# food = [guloseimas,carne]

# print (food)

# Tupla - sequence of imutable values
coordinateX = 10.0
coordinateY = 20.0

coordinate = (coordinateX, coordinateY)

student = ('Fred', 35, 'Brasil')

if 'Fred' in student:
    print('Fred is here')
    """

# Set - collection of unique values

s = set()
s.add(1)
s.add(2)
s.add(3)
s.add(4)
print(s)

s.add(3)
print(s)

s.remove(2)
print(s)
print(f'The set has {len(s)} elements')

# Collection unordered, unindexed and no duplicate values

# utensils={"Fork","Spoon","Knife"}
# dishes = {"bowl","cup","plate"}
# dishes.add('Knife')

# for i in utensils:
#    print (i)

# utensils.clear()
# utensils.add('Knife')
# utensils.update(dishes)
# dinner_table = utensils.union(dishes)

# for i in dinner_table:
#    print (i)

# print(utensils.difference(dishes))
# print(utensils.intersection(dishes))

# Dictionary collection of key-value pairs - Changeable, unordered

Capitals = {"USA": "Washington", "China": " Beijing", "Russia": "Moscou"}

print(Capitals["Russia"])
print(Capitals.get("Brazil"))

Capitals.update({"Brazil": "Brasilia"})
Capitals["China"] = "Godira"
print(Capitals.get("Brazil"))

for key, values in Capitals.items():
    print(key, values)
