#Itertools : propduct , permutations, combiantions, accumulate

# from itertools import product
# a = [1,2]
# b = [3,4]
# prod = product(a,b)
# print(list(prod))
#
# a = [1,2]
# b = [3,4]
# prod = product(a,b, repeat = 2)
# print(list(prod))
#
#
# a = [1,2]
# b = [3,4]
# prod = product(a,b)
# print(list(prod))
#
#
# from itertools import permutations
# a = [1,2,3]
# perm = permutations(a)
# print(list(perm))
#
# from itertools import permutations
# a = [1,2,3]
# perm = permutations(a,2)
# print(list(perm))
#
# from itertools import combinations
# a = [1,2,3,4]
# comb = combinations(a,2)
# print(list(comb))
#
# from itertools import combinations_with_replacement
# a = [1,2,3,4]
# comb = combinations(a,2)
# print(list(comb))
# comb_wr = combinations_with_replacement(a,2)
# print(list(comb_wr))

# from itertools import accumulate
# a = [1,2,3,4]
# acc = accumulate(a)
# print(a)
# print(list(acc))

# from itertools import accumulate
# import operator
# a = [1,2,3,5,4]
# acc = accumulate(a, func=max)
# print(a)
# print(list(acc))
#
# from itertools import groupby
# persons = [{"name": "Cesar", "age": 28}, {"name": "Max", "age": 29},
#            {"name": "Daisy", "age": 40}, {"name": "Tom", "age": 30}]
#
# group_obj = groupby(persons, key=lambda x:x ["age"])
# for key, value in group_obj:
#     print(key,list(value))

from itertools import count, cycle, repeat

#count
# for x in count(10):
#     print(x)
#     if x == 15:
#         break

#cycle
# a = [1,2,3]
# for x in cycle(a):
#  print(x)

# #repeat
# a = [1,2,3]
# for x in repeat(1,4):
#  print(x)

