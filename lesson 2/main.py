# lst = []
# print(type(lst))

# fruits = ['apple', 'banana', 'orange']
# print(fruits[0])
# print(fruits[-1], fruits[2])
# fruits[0] = 'limon'
# print(fruits)

# lst1 = ['apple', 'limon', 'banana']
# lat2 = [True, False, True]
# lst3 = [12,13,14]

# append
# lst = ['numbers']
# lst2 = list()
# lst2.append('num')
# print(lst2)

# insert() belgilangan qismga element qo'shadi
# fruits = ['banana', 'limon','kiwi']
# fruits.insert(2, 'apple')
# print(fruits)

# remove()
# fruits = ['banana', 'limon','kiwi']
# fruits.remove('limon')
# print(fruits)
# print(fruits.pop())

# del 
# fruits = ['banana', 'limon','kiwi']
# del fruits[1]
# del fruits
# print(fruits)

# extend()
# fList = [1,2,3,4,5,6]
# sList = [7,8,9,10]
# fList.extend(sList)
# print(fList)

# sort()
# nums = [5,9,1,3,2,4,8,7]
# nums.sort()
# print(nums)

# reverse()
# nums = [1,2,3,4,5,6]
# nums.reverse()
# print(nums)

# len()
# nums = [1,2,3,4,5,6]
# print(len(nums))

# slicing [start, stop, step]
# simpleList = [True, False, 'hello', 'bye', 'why', 1, 5, 15, 1.5]
# print(simpleList[0:3])
# print(simpleList[-1])
# print(simpleList[:4])


# nums = [1,2,3,4,5,6,7,8,9,10]
# print(nums[1::2])

# txt = """Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."""

# myList = txt.split()
# # print(myList)
# print(myList[0:19:])


# thisList = ['apple', 'banana', 'mango', 'cherry','kiwi', 'limon']
# thisList[1:4] = ['men', 'sen', 'biz']
# print(thisList)

# thisList = ['apple', 'banana', 'mango', 'cherry','kiwi', 'limon']
# thisList.pop(0)
# print(thisList)
# thisList.clear()
# print(thisList)

# thisList = ['apple', 'banana', 'cherry']
# thisList.remove('banana')
# print(thisList)

# thisList = [100,50,65,82,23]
# thisList.sort(reverse=True)
# print(thisList)
# thisList.reverse()
# print(thisList)

# my_list = thisList.copy()
# my_list.append('hi')
# print(my_list)

# loop
# fruits = ['apple', 'banana', 'cherry']
# for i in fruits:
#     print(i)

nums = [1,2,3,4,5,6,7,8,9]
sum = 0
# for i in nums:
#     sum += i
# print(sum)

for i in nums:
    print(f'{i} = {i**2}')

