users = [
    {'id': 0, 'name': 'Hero'},
    {'id': 1, 'name': 'Dunn'},
    {'id': 2, 'name': 'Sue'},
    {'id': 3, 'name': 'Chil'},
    {'id': 4, 'name': 'Thor'},
    {'id': 5, 'name': 'Clive'},
    {'id': 6, 'name': 'Hicks'},
    {'id': 7, 'name': 'Devin'},
    {'id': 8, 'name': 'Kate'},
    {'id': 9, 'name': 'Klein'}
]
print(users)

friendship_pairs = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4), (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]
print(friendship_pairs)

### Initialize o dict com uma lista vazia para cada id de usuario:

friendships = {user['id']: [] for user in users}

### Em seguida, execute um loop pelos pares de amigos para preenchê-la

for i, j in friendship_pairs:
    friendships[i].append(j)
    friendships[j].append(i)
