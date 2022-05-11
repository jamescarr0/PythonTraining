animals = [
    {'type': 'dog', 'name': 'diesel', 'age': 10},
    {'type': 'cat', 'name': 'ginger', 'age': 2},
    {'type': 'rabbit', 'name': 'tom', 'age': 7},    
]

print(sorted(animals, key=lambda animal: animal['age'], reverse=True)[0])