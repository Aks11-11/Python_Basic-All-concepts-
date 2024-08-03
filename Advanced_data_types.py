#Heap
import heapq

myList = [9, 5, 4, 1, 3, 2]
heapq.heapify(myList) # turn myList into a Min Heap
print(myList)    # => [1, 3, 2, 5, 9, 4]
print(myList[0]) # first value is always the smallest in the heap

heapq.heappush(myList, 10) # insert 10
x = heapq.heappop(myList)  # pop and return smallest item
print(x)                   # => 1

#Stacks and Queues
from collections import deque

q = deque()          # empty
q = deque([1, 2, 3]) # with values

q.append(4)     # append to right side
q.appendleft(0) # append to left side
print(q)    # => deque([0, 1, 2, 3, 4])

x = q.pop() # remove & return from right
y = q.popleft() # remove & return from left
print(x)    # => 4
print(y)    # => 0
print(q)    # => deque([1, 2, 3])

q.rotate(1) # rotate 1 step to the right
print(q)    # => deque([3, 1, 2])

#Slicing_Strings
s = 'mybacon'
s[2:5]
'bac'
s[0:2]
'my'

s = 'mybacon'
s[:2]
'my'
s[2:]
'bacon'
s[:2] + s[2:]
'mybacon'
s[:]
'mybacon'

s = 'mybacon'
s[-5:-1]
'baco'
s[2:6]
'baco'

s = '12345' * 5
s
'1234512345123451234512345'
s[::5]
'11111'
s[4::5]
'55555'
s[::-5]
'55555'
s[::-1]
'5432154321543215432154321'

#FUNCTIONS

#Basic
def hello_world():
    print('Hello, World!')

#return
def add(x, y):
    print("x is %s, y is %s" %(x, y))
    return x + y

add(5, 6)    # => 11

#Positional-Arguments
def varargs(*args):
    return args

varargs(1, 2, 3)  # => (1, 2, 3)

#keyword-arguments
def keyword_args(**kwargs):
    return kwargs

# => {"big": "foot", "loch": "ness"}
keyword_args(big="foot", loch="ness")

#returning-multiple
def swap(x, y):
    return y, x

x = 1
y = 2
x, y = swap(x, y)  # => x = 2, y = 1

#Default-Value
def add(x, y=10):
    return x + y

add(5)      # => 15
add(5, 20)  # => 25

#anonymous-functions
# => True
(lambda x: x > 2)(3)

# => 5
(lambda x, y: x ** 2 + y ** 2)(2, 1)

#MODULES

#math

from math import *

import math
print(math.sqrt(16))  # => 4.0

import math as m

# => True
math.sqrt(16) == m.sqrt(16)

from math import ceil, floor
print(ceil(3.7))   # => 4.0
print(floor(3.7))  # => 3.0

import math
dir(math)

#Exception-handling
try:
    # Use "raise" to raise an error
    raise IndexError("This is an index error")
except IndexError as e:
    pass                 # Pass is just a no-op. Usually you would do recovery here.
except (TypeError, NameError):
    pass                 # Multiple exceptions can be handled together, if required.
else:                    # Optional clause to the try/except block. Must follow all except blocks
    print("All good!")   # Runs only if the code in try raises no exceptions
finally:                 # Execute under all circumstances
    print("We can clean up resources here")
