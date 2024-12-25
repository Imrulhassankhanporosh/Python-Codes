a = [5, 2, 1, 3]
print(a)
print(a[2])
# 3rd element
print(a[2:])
# from 3rd element to last element
print(a[-1])
# from reverse 1st element

print(1 not in a)
print(4 in a)
# in function

print(len(a))
# length of list

a.append(2.5)
print(a)
# add element in last

a.insert(2, 7)
print(a)
# insert element in specified index

a.remove(7)
print(a)
# remove element

a.sort()
print(a)
# sort

a.reverse()
print(a)
# reverse

a.pop();
print(a)
# remove last element

b = a.copy();
print(a)
# remove last element

pos = a.index(2.5);
print(pos)
# element position

count = a.count(1);
print(count)
# count of the element
