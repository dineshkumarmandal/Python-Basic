#Code that modifies a collection while iterating over that same collection can be tricky to get right. Instead, it is usually more straight-forward to loop over a copy of the collection or to create a new collection:
# Create a sample collection
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# Strategy:  Iterate over a copy
for user, status in users.copy().items():
    print("\n------ Before Delete -------\n")
    print(user)
    if status == 'inactive':
        del users[user]
    
    print("\n------ After Delete -------\n")
    print(user)

# Strategy:  Create a new collection
active_users = {}
for user, status in users.items():
    print(user)
    if status == 'active':
        active_users[user] = status