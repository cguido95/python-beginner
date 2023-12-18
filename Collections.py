#Collections

# from collections import namedtuple
# Point = namedtuple("Point", "x,y")
# pt = Point(1,-4)
# print(pt)
#
# Point = namedtuple("Point", "x,y")
# pt = Point(1,-4)
# print(pt.x, pt.y)

# from collections import OrderedDict
# ordered_dict = OrderedDict()
# ordered_dict["a"] = 1
# ordered_dict["b"] = 2
# ordered_dict["c"] = 3
# ordered_dict["d"] = 4
# print(ordered_dict)

# from collections import defaultdict
# d = defaultdict(int)
# d["a"] = 1
# d["b"] = 2
# print(d["c"])
#
# d = defaultdict(float)
# d["a"] = 1
# d["b"] = 2
# print(d["c"])
#
# d = defaultdict(list)
# d["a"] = 1
# d["b"] = 2
# print(d["c"])
#
# d = {}
# d["a"] = 1
# d["b"] = 2
# print(d["c"])


#append, pop, extend
from collections import deque
d = deque()

d.append(1)
d.append(2)
d.appendleft(3)

d.extend([4,5,6])
print(d)
d.rotate()
print(d)

d.popleft()
print(d)