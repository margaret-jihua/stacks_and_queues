# class Node:
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next

#collection is a python module
#deque is a object(class) on the module
from collections import deque

my_queue = deque()
my_queue.append(1)
my_queue.append(5)
my_queue.append(10)

print(my_queue)

my_queue.popleft()

print(my_queue)