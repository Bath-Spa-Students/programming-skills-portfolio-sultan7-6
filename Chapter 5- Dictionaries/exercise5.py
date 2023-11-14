# Make an empty list to store the pets in.
pets = []

# Make individual pets, and store each one in the list.
pet = {
    'animal type': 'lion',
    'name': 'shera',
    'owner': 'charles',
    'weight': 75,
    'eats': 'meat',
}
pets.append(pet)

pet = {
    'animal type': 'hen',
    'name': 'peter',
    'owner': 'james',
    'weight': 2,
    'eats': 'seeds',
}
pets.append(pet)

pet = {
    'animal type': 'husky',
    'name': 'loca',
    'owner': 'hakeem',
    'weight': 32,
    'eats': 'dog food',
}
pets.append(pet)

# Display information about each pet.
for pet in pets:
    print(f"\nHere's what I know about {pet['name'].title()}:")
    for key, value in pet.items():
        print(f"\t{key}: {value}")