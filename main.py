#Print Hello World
print("Hello, World!")

#Variables
age = 18      # age is of type int
name = "Akshat" # name is now of type str
print(name)

#slicing String
msg = "Hello, World!"
print(msg[2:5])

#Lists
mylist = []
mylist.append(1)
mylist.append(2)
for item in mylist:
    print(item) # prints out 1,2

#If-Else
num = 200
if num > 0:
    print("num is greater than 0")
else:
    print("num is not greater than 0")

#Loops
for item in range(6):
    if item == 3: break
    print(item)
else:
    print("Finally finished!")

#Functions
def my_function():
    print("Hello from a function")

#File handling
with open("myfile.txt", "r", encoding='utf8') as file:
    for line in file:
        print(line)

#Arithmatic
result = 10 + 30 # => 40
result = 40 - 10 # => 30
result = 50 * 5  # => 250
result = 16 / 4  # => 4.0 (Float Division)
result = 16 // 4 # => 4 (Integer Division)
result = 25 % 2  # => 1
result = 5 ** 3  # => 125

#Plus Equals
counter = 0
counter += 10           # => 10
counter = 0
counter = counter + 10  # => 10

message = "Part 1."

# => Part 1.Part 2.
message += "Part 2."

#f-Strings
website = 'Quickref.ME'
f"Hello, {website}"
"Hello, Quickref.ME"

num = 10
f'{num} + 10 = {num + 10}'

#BUILT IN DATA TYPES

#Strings
hello = "Hello World"
hello = 'Hello World'

#Numbers
x = 1    # int
y = 2.8  # float
z = 1j   # complex

print(type(x))
<class 'int'>

#Booleans
my_bool = True
my_bool = False

bool(0)  # => False
bool(1)  # => True

#Lists
list1 = ["apple", "banana", "cherry"]
list2 = [True, False, False]
list3 = [1, 5, 7, 9, 3]
list4 = list((1, 5, 7, 9, 3))

#Tuple
my_tuple = (1, 2, 3)
my_tuple = tuple((1, 2, 3))

#Set
set1 = {"a", "b", "c"}
set2 = set(("a", "b", "c"))

#Dictionary
empty_dict = {}
a = {"one": 1, "two": 2, "three": 3}
a["one"]

a.keys()
dict_keys(['one', 'two', 'three'])
a.values()
dict_values([1, 2, 3])
a.update({"four": 4})
a.keys()
dict_keys(['one', 'two', 'three', 'four'])
a['four']
4

#integers
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

#float
x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

#Strings
x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'







