# # Creating a Tuple
car = ("Ford", "Raptor", 2019, "Red")
print(car)

# Length
print(len(car))

# Indexing
print(car[1])

# Slicing
print(car[2:])


# # Merging Tuples
hero1 = ("Batman", "Bruce Wayne")
hero2 = ("Wonder Woman", "Diana Prince")
awesome_team = (hero1, hero2)
print(awesome_team)

# # Nested Tuples
cities = ("London", "Paris", "Los Angeles", "Tokyo")
print("Moscow" in cities)

# # Search
cities = ("London", "Paris", "Los Angeles", "Tokyo")
print(cities.index("Tokyo"))

cities = ("London", "Paris", "Los Angeles", "Tokyo")
print(cities.index("Tokyo"))

del cities
# # Immutability