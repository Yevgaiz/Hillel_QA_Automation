users = [
    {'name': 'Luarvik L. Luarvik',
     'age': 17},
    {'name': 'Olaf Andvarafors',
     'age': 18},
    {'name': 'Brun Du Barnstokr',
     'age': 19},
    {'name': 'John Smith',
     'age': 23},
    {'name': 'Bred Pitt',
     'age': 44}
]

more_than_18 = []
for user in users:
    if user['age'] >= 18:
        more_than_18.append(user['name'])

print(more_than_18)