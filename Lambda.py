#Lambda : arguments: expression

#Sorted
# points2d = [(1,-2), (6,4), (5,-6), (10,8)]
# points2d_sorted = sorted(points2d)
# print(points2d)
# print(points2d_sorted)

# points2d = [(1,-2), (6,4), (5,-6), (10,8)]
# points2d_sorted = sorted(points2d, key = lambda x: x[1])
# print(points2d)
# print(points2d_sorted)

# points2d = [(1,-2), (6,4), (5,-6), (10,8)]
# points2d_sorted = sorted(points2d, key = lambda x: x[0] + x[1])
# print(points2d)
# print(points2d_sorted)

# #map function
# a = [1,2,3,4,5]
# b = map(lambda x: x*2, a)
# print(list(b))
# #easier
# c = [x*2 for x in a]
# print(c)

#fucntion in sequence
# a = [1,2,3,4,5,6]
# b = filter(lambda x: x%2 == 0, a)
# print(list(b))
# c = [x for x in a if x%2 == 0]
# print(c)

#Reduce function
from functools import reduce
a = [1,2,3,4,5,6]
product_a = reduce(lambda x,y: x*y, a)
print(product_a)

