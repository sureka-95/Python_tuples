#create list of dictionary of people with name and age
people = [
    {"name": "Anita", "age": 25},
    {"name": "Babu", "age": 17},
    {"name": "vasanth", "age": 19},
    {"name": "priya", "age": 16},
    {"name": "Ezhil", "age": 22},
    {"name":"kavi","age":28}
]

# Filter out people under 18
child= filter(lambda person: person["age"] < 18, people)
#Filter out people over 18
adults=filter(lambda person:person["age"]>=18,people)


# Extract names of adults and list using map
adult_names = list(map(lambda person: person["name"], adults))

print(adult_names)  # Output