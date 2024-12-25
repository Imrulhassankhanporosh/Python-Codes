a = []
a.append(2)
a.pop()
a.append(9)
print(a)

# stack

from collections import deque

b = deque([1, 2, 5, 3])
b.popleft()
print(b)



