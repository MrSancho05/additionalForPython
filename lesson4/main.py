# myCar = {
#     'Brand': 'Mers',
#     'year' : 2024,
#     'color': 'black'
# }
# print(myCar['Brand'])
# print(myCar['year'])
# print(myCar['color'])

# users = {
#     'user': 
#     {
#     'name': 'Sancho',
#     'age': 19,
#     },
#     'user2': 
#     {
#     'name': 'Bob',
#     'age': 25,
#     },
#     'user3': 
#     {
#     'name': 'Oscar',
#     'age': 30,
#     }
# }

# print(f'Ismi {users['user']['name']}, yoshi {users['user']['age']}')

d2 = dict(name='Palmer', age=21)
# print(d2)
# x = d2['name']
# x = d2.get['age']
# print(x)
# x = d2.keys()
# print(x)
# x = d2.values()
# print(x)
# d2['age'] = 25
# print(d2)

# x = d2.items()
# print(x)

# d2.update({'model': 'Mers'})
# print(d2)
# d2.update({'color': 'blue'})
# print(d2)
# d2.pop('model')
# print(d2)
# del d2
# d2.clear()
# print(d2)

# myDict = d2.copy()
# print(myDict)

# x = {'key1', 'key2', 'key3'}
# y = 0
# thisDict = dict.fromkeys(x,y)
# print(thisDict)

# thisD = {
#     "name": 'Palmer', 
#     "age": 19
# }
# x = thisD.get["age"]
# print(x)


car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.get("brand")

print(x)


x = 10
if x != 5:
    print('Bu 5 soni')
else:
    print('Bu 10 soni')
