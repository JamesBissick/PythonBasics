from datetime import date

# Fundamental Data Types
'''
int
float
bool
str
list
dict
tuple
set
'''

# Classes -> custom types

# PyCharm tips
# use option + command + L to reformat code according to PEP coding style

# Specialized Data Types
# None

print(2 + 3)

# Print types of
print(type(2 - 4))
print(type(2 / 5))

# Keeps the decimal anyways
print(8.9 + 1.1)

# Double operations return integers
print(2 ** 2)
print(5 // 4)

# Modulo
print(6 % 4)

# Math functions
print(round(3.2))
print(abs(-21))

# Operator precedence
print(20 - 3 * 4)
print((20 - 3) * 4)

# Binary
print(bin(5))
print(int('0b101', 2))

# Type Conversion
print(str(100))
print(type(str(100)))

# Variables
iq = 142
user_age = 'James'
a, b, c = 1, 2, 3

print(iq)
print(user_age)
print(a)
print(b)
print(c)

# Augmented assignment operator
some_value = 5
some_value += 2
print(some_value)

# Strings
string = 'text'
long_string = '''
 😎
≤))≥
_| \_
'''
fname = 'James'
lname = 'Bissick'
full_name = fname + ' ' + lname

print(string)
print(long_string)

# Formatted Strings (f strings)
name = 'Jack'
age = 34

print('Hello ' + name + '. You are ' + str(age) + ' years old.')
print(f'Hello {name}. You are {age} years old.')  # A bit like string literals in javascript

# String Indexes
example = 'Hello World!'

print(example[6])
# [start:stop]
print(example[0:5])
# [start:toend]
print(example[:])
# [num:toend]
print(example[1:])
# [frombegin:tonum]
print(example[:9])
# [-1] select the last one
print(example[-1])

# Built-in Functions
# https://www.w3schools.com/python/python_reference.asp

value = len('Hello World!')
print(f'{value} chars')

quote = 'to be or not to be'
quote2 = quote.replace('be', 'me')
print(quote2)
print(quote)

# Ex 1.
# birth_year = int(input('What year were you born? '))
# now = date.today()
# age = now.year - birth_year
# print(f'Your age is {age}!')

# Ex 2.
# name = input('What is your name? ')
# password = input('Enter a password: ')
# pass_length = len(password)
# hidden_pass = '*' * pass_length
# print(f'Hello {name}, your password {hidden_pass} is {pass_length} letters long.')

# Lists (a bit like Arrays)
li = [1, 2, 3, 4, 5]
li2 = ['a', 'b', 'c', 'd', 'e']
li3 = [1, 2, 'x', True]

# List Slicing and Mutable example
amazon_cart = [
    'notebooks',
    'sunglasses',
    'toys',
    'grapes'
]
amazon_cart[3] = 'laptop'
print(amazon_cart)
# new_cart = amazon_cart # Modify the list
new_cart = amazon_cart[:]  # Copy the list
new_cart[0] = 'gum'
print(new_cart)
print(amazon_cart)

# Matrix (Multidimentional Lists)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[0][1])

basket = [1, 2, 3, 4, 5]
print(len(basket))
basket.append(100)
new_basket = basket
print(new_basket)
basket.remove(4)  # Works with the value we want to remove
new_basket = basket
print(new_basket)
basket.pop(4)  # Works with the index we want to remove
new_basket = basket
print(new_basket)

# Range
print(list(range(10)))  # Inside a list method it generates a list from 0 to 10

# String Methods
sentence = ['Hi!', 'My', 'name', 'is', 'Jack.']
separator = ' '
new_sentence = separator.join(sentence)
print(new_sentence)

# List unpacking
a, b, c, *rest, x = [1, 2, 3, 4, 5, 6, 7, 8]
print(a)
print(b)
print(c)
print(x)
print(rest)

# Dictionary (keys has to be unique)
dictionary = {
    1: [1, 2, 3],
    2: 'x0fe',
    3: 'x0ab'
}

print(dictionary[2])
print(dictionary[1][1])

user2 = dict(name='Jack')
print(user2)

# Tuple (like immutable Lists)
# If you don't need to modify a List, use a Tuple instead (more performance)
my_tuple = (1, 2, 3, 4, 5)
# my_tuple[1] = 'z'
print(my_tuple.index(5))

# Sets (unordered collection of unique objects)
my_set = {1, 2, 3, 3, 4, 5, 5}
my_set.add(2)  # wont add 2 because it already exists
my_set.add(10)
print(my_set)

my_list = [1, 2, 3, 3, 4, 5, 5]
print(set(my_list))  # remove duplicates
print(1 in my_list)