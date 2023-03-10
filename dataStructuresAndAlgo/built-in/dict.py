# # Creating a Dictionary

empty_dict = {}  # Empty dictionary
print(empty_dict)

phone_book = {"Batman": 468426,
              "Ghostbusters": 44678,
              "Cersei": 237734,
              "Ghostbusters": 44578}
print(phone_book)


# # The dict() Constructor

empty_dict = dict()  # Empty dictionary
print(empty_dict)

phone_book = dict(Batman=468426, Cersei=237734, Ghostbusters=44678)
# Keys will automatically be converted to strings
print(phone_book)

# Alternative approach
phone_book = dict([('Batman', 468426),
                   ('Cersei', 237734),
                   ('Ghostbusters', 44678)
                   ('Cersei', 2334)])
print(phone_book)

# # Accessing Values

phone_book = {"Batman": 468426,
              "Cersei": 237734,
              "Ghostbusters": 44678}
print(phone_book["Cersei"])
print(phone_book.get("Ghostbusters"))