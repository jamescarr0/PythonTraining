animals = [
    {'type': 'dog', 'name': 'diesel', 'age': 10},
    {'type': 'cat', 'name': 'ginger', 'age': 2},
    {'type': 'rabbit', 'name': 'tom', 'age': 7},    
]

# Print the oldest animal 
# Sort animals by age in reverse and print the 1st element (index zero)
print(sorted(animals, key=lambda animal: animal['age'], reverse=True)[0])