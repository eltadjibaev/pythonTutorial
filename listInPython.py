names = ['John', 'Bob', 'Mosh']
print(names[0])
print(names[-1])
print(names[2:])

cordinates = [1, 2, 3]
x, y, z = cordinates

# 2D lists

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
]
print(matrix[0][1])

# List Methods
numbers = [5,1,2,7,4]
numbers.append(20) # add item at the end
numbers.insert(0,10)
numbers.remove(5)
#numbers.clear()
numbers.pop()
print(numbers)
print(numbers.index(4))
print(numbers.count(7))
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
numbers2 = numbers.copy()

