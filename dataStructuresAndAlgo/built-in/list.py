
# Adding Elements
num_list = []  # Empty list
num_list.append(1)
num_list.append(2)
num_list.append(3)
print(num_list)



num_list = [1, 2, 3, 5, 6]
num_list.insert(10, 4)  # Inserting 4 at the 3rd index. 5 and 6 shifted ahead
print(num_list)

# Removing Elements

houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
last_house = houses.pop(2)
print(last_house)
print(houses)


houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin", "Ravenclaw"]
print(houses)
houses.remove("Ravenclaw")
print(houses)

# For nested lists
populations = [["Winterfell", 10000], ["King's Landing", 50000],
               ["Iron Islands", 5000]]
print(populations)
populations.remove(["King's Landing", 50000])
print(populations)



# List Slicing

num_list = [1, 2, 3, 4, 5, 6, 7, 8]
a = num_list[2:5]
print(a)
print(num_list[2:5])
print(num_list[0::2])


# Index Search

cities = ["London", "Paris", "Los Angeles", "Beirut"]
print(cities.index("Los Angeles"))  # It is at the 2nd index

# List Sort

num_list = [20, 40, 10, 50.4, 30, 100, 5, 20]
num_list.sort()
print(num_list)