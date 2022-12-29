my_dictionary = {
    1: "A",
    2: "B",
}

print(my_dictionary[1])

empty_dict = {"A": "B"}

print(type(empty_dict))

# Creating empty dictionary
empty_dictionary = dict()

# Get a value from dictionary
print(my_dictionary[1])
print(my_dictionary.get(1))

# removing item
my_dictionary.pop(1)
print(my_dictionary)

my_dictionary.clear()
print(my_dictionary)

# get the list of all keys
scores = {
    "A": 10,
    "B": 20,
    "C": 30,
}

all_keys = list(scores.keys())
print(type(all_keys))

all_keys = scores.keys()
print(all_keys)
print(type(all_keys))

# get all values
all_values = scores.values()
print(all_values)
print(type(all_values))

# Simple problem
name_count = 0
duplicate_list = ["Amal", "Amal", "Amal", "Kamal", "Kamal","Kamal","Kamal", "Sunil", "Sunil", "Saman", "Saman","Saman", "Nimal", "Nimal", "Ajith", "Sarath"]
duplicate_dictionary = {}
for name in range(len(duplicate_list)):
    for i in duplicate_list:
        if duplicate_list[name] == i:
            name_count += 1
    duplicate_dictionary[duplicate_list[name]] = name_count
    name_count = 0

print(duplicate_dictionary)


