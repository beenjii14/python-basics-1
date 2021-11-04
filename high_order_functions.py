# use filter
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pairs = list(filter(lambda x: x % 2 == 0, numbers))
odd = list(filter(lambda x: x % 2 != 0, numbers))
print(pairs)
print(odd)

# use map
squares = list(map(lambda y: y**2, numbers))
print(squares)

#use reduce
from functools import reduce
sum = reduce(lambda x, y: x + y, numbers)
print(sum)

# using reduce to compute maximum element from list
element = reduce(lambda x, y: x if x > y else y, numbers)
print(element)
