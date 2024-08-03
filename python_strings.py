#Array-Like
hello = "Hello, World"
print(hello[1])
print(hello[-1])

#Looping
for char in "foo":
    print(char)

#string_length
hello = "Hello, World!"
print(len(hello))

#Multiple-copies
s = '===+'
n = 8
s * n
'===+===+===+===+===+===+===+===+'

#Check-String
s = 'spam'
s in 'I saw spamalot!'
s not in 'I saw The Holy Grail!'

#concatenates
s = 'spam'
t = 'egg'
s + t

#Formatting
name = "John"
print("Hello, %s!" % name)

#PYTHON F-STRINGS

#f-strings_usage
website = 'Nike.com'
f"Hello, {website}"
"Hello, Nike.com"

num = 10
f'{num} + 10 = {num + 10}'
'10 + 10 = 20'

f"""He said {"I'm Akshat"}"""
"He said I'm Akshat"

f'5 {"{stars}"}'
'5 {stars}'
f'{{5}} {"stars"}'
'{5} stars'

name = 'Eric'
age = 27
f"""Hello!
...     I'm {name}.
...     I'm {age}."""
"Hello!\n    I'm Eric.\n    I'm 27."

#fill-allign
f'{"text":10}'     # [width]
'text      '
f'{"test":*>10}'   # fill left
'******test'
f'{"test":*<10}'   # fill right
'test******'
f'{"test":*^10}'   # fill center
'***test***'
f'{12345:0>10}'    # fill with numbers
'0000012345'

#f-strings-type
f'{10:b}'        # binary type
'1010'
f'{10:o}'        # octal type
'12'
f'{200:x}'       # hexadecimal type
'c8'
f'{200:X}'
'C8'
f'{345600000000:e}' # scientific notation
'3.456000e+11'
f'{65:c}'       # character type
'A'
f'{10:#b}'      # [type] with notation (base)
'0b1010'
f'{10:#o}'
'0o12'
f'{10:#x}'
'0xa'

#others
f'{-12345:0=10}'  # negative numbers
'-000012345'
f'{12345:010}'    # [0] shortcut (no align)
'0000012345'
f'{-12345:010}'
'-000012345'
import math       # [.precision]
math.pi
3.141592653589793
f'{math.pi:.2f}'
'3.14'
f'{1000000:,.2f}' # [grouping_option]
'1,000,000.00'
f'{1000000:_.2f}'
'1_000_000.00'
f'{0.25:0%}'      # percentage
'25.000000%'
f'{0.25:.0%}'
'25%'


