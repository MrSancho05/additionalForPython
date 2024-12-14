myTuple = ('apple', 'banana', 'apricot', 'cherry', 'mango')
# lst = list(myTuple)
# lst.append('orange')
# myTuple2 = tuple(lst)
# print(myTuple2)

# easy way 
# y = ('orange',)
# myTuple += y
# print(myTuple)
# lst = list(myTuple)
# lst.remove('apricot')
# myTuple2 = tuple(lst)
# print(myTuple2)
# del myTuple2
# print(myTuple2)


# (one, two, three) = myTuple
# print(one)
# print(two)
# print(three)
# (one, *two, three) = myTuple
# print(one)
# print(two)
# print(three)

for i in myTuple:
    print(i)