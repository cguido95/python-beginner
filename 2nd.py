

#Lists


#sorting, clearing, reversing, pop,etc.

mylist = ["banana", "cherry", "apple"]
print(mylist)

mylist.append("lemon")
print(mylist)

mylist.insert(0, "blueberry")
print(mylist)

item = mylist.pop()
print(item)
print(mylist)

item = mylist.remove("cherry")
print(item)
print(mylist)

item = mylist.clear()
print(item)
print(mylist)

item = mylist.reverse()
print(item)
print(mylist)

mylist.sort()
new_list = sorted(mylist)
print(new_list)


#adding lists together
mylist = [0] * 5
print(mylist)

mylist2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

new_list = mylist + mylist2

print(new_list)


#Slices

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a = mylist[1:5]
print(a)

a = mylist[0:]
print(a)




#List_org & list_copy

list_org = ["banana", "cherry", "apple"]

list_cpy = list_org
list_cpy.append("lemon")

print(list_cpy)
print(list_org)


list_org = ["banana", "cherry", "apple"]

list_cpy = list_org.copy()
list_cpy.append("lemon")

print(list_cpy)
print(list_org)

list_org = ["banana", "cherry", "apple"]

list_cpy = list_org[:]

list_cpy.append("lemon")

print(list_cpy)
print(list_org)






#List comprehension
mylist = [1, 2, 3, 4, 5, 6]
b = [x*x for x in mylist]

print(mylist)
print(b)

a = mylist[::2]
print(a)

