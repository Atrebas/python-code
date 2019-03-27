
# These are my notes taken during the Python MOOC (completed Jan. 2018).
# https://www.fun-mooc.fr/courses/course-v1:UCA+107001+session01/about
# https://github.com/parmentelat/moocpython/blob/master/pdf_du_cours/from_latex/Python.pdf
# https://github.com/parmentelat/moocpython/files/1639944/Python3.-.1.a.9.avec.index.pdf

## ----------------------------------------------------------
## ----------------------------------------------------------
## Introduction

## Guido Van Rossum, creator, BDFL until 2018
## Highly readable language for an easy access
## Pragmatic, focus on ease of use
## Uniform syntax on the different types of objects
## Allows a rapid development
## A lot of libraries, especially for data science, ...
## v1 in 1994, v2 in 2000, v3 in 2008 (breaking changes)
## https://docs.python.org/3/faq/programming.html

print("Hello, World!")


## The zen of python
import this

# several flavours python, IPython
# idle, notebooks

## modules
import math             # import module
from numpy import cos   # import a function
import numpy as np      # import with alias
print(math)
dir(math)               # list included functions
help(math.pi)           # math.pi? in jupyter notebooks
## standard library (modules included by default)

 
## a variable is a name that references an object
'spam'.upper() # upper is a method
n = 3
type(n)
n = "spam"     # dynamic (and strongly typed) language
type(n)
isinstance(n, str)

del n          # garbage collector will free the memory

## keywords that can't be used as variable name
import keyword
keyword.kwlist


## ----------------------------------------------------------
## ----------------------------------------------------------
## Numeric types

# int, float, complex
i = 1        # integer
i += 1       # a = a + 1
f = 0.1      # float
c = 1 + 1j   # complex
1j ** 2      # square
7 // 3       # integer division
7.//3        # // with float returns float
7 % 3        # modulo
abs(-1)      # absolute value

## floating point precision
z = 1.1 - 1
z == 0.1
print(z)
print("%0.1f" % z)
format(0.1, '.17f')
## check decimal or fractions modules
from decimal import Decimal
Decimal('1.1') - Decimal('1') == Decimal('0.1')

True + False
int("1") # int, float, complex, str

## bitwise operators
bin(3) 
bin(6) 
bin(12) 
3 << 1
3 << 2
i >>= 2
0xf0
# import sys; print(sys.float_info)


## ----------------------------------------------------------
## ----------------------------------------------------------
## Basic notions

## strings

# reminder: bits (01) are decoded to an integer value
# for a given encoding system (e.g. ASCII), a value corresponds to a character
# problem: limited number of possible characters
# 7 bits => 128 characters
# 8 bits => 256 characters extended
# several systems exist but incompatible
# UNICODE project: UTF-8/16/32, UTF-8 compatible with ascii
# unicode > 120k coded characters
# USE UTF-8

"\u529b"  ## python supports unicode
s  = "力"
en = s.encode("utf-8")
en.decode("utf-8")

dir(str)  # str? IPython only
help(str)

c = "spam" ## strings are immutable (see pythontutor)
c.title()
c.replace("spam", "ham") 

# f-strings
a  = 1
b  = 2
f"{a} and {b}"  
"{} and {}".format(a, b) 

## some examples of string methods
'abc:def:ghi:jkl'.split(':')
":".join(['abc', 'def', 'ghi', 'jkl'])
"abcdeabcdeabcde".replace("abc", "zoo")
"abcdeabcdeabcde".replace("abc", "zoo", 2)
"[x] versus  [y]".replace("[x]", "spam").replace("[y]", "ham")
" abc:de f:g hi ".replace(" ", "")
" \trm_special\n".strip()
'abc;def;ghi;jk;'.strip(';').split(';')
"abcdefcdefghefg".find("def")
"abcdefcdefghefg".find("zoo")
"abcdefcdefghefg".rfind("fgh")
"abcdefcdefghefg".index("zef") # like find but throws exception
"cde" in "abcdek"
"abcdefcdefghefg".count("ef")
"abcdefcdefghefg".startswith("abcd")
"abcdefcdefghefg".endswith("hefg")
"abcdefcdefghefg".upper()
"abcdefcdefghefg".swapcase()
"abcdefcdefghefg".capitalize()
## https://docs.python.org/3/library/stdtypes.html#string-methods

## string formatting
print(1, 'a', 12 + 4j)
first, last, age = 'John', 'Doe', 35
f"{first} {last} is {age}"
f"In 5 years {first} will be {age + 5}"
"%s %s is %s" % (first, last, age) # old version

## format numbers
from math import pi
f"pi rounded: {pi:.2f}"
x = 1
f"{x:03d}"

## fixed length
x = [(1, 1, 1), (111, 111, 111), (11111, 11111, 11111)]
for col1, col2, col3 in x:
    print(f"{col1:<7} -- {col2:^7} -- {col3:>7}")

# number = input(Pick a number: ")
# print(f"number={number}")

## https://docs.python.org/3/library/string.html#formatstrings    

## Regular expressions
import re
x = "Lorem ipsum dolor sit amet"
print(re.findall(r"[a-m]", x))
x = "dsf-6 ,333 1._nb9;"
re.findall("[-\d]+", x)
# ...

import string
char = string.ascii_lowercase
print(char)

###########################
## Sequences

## sequences = list/tuple/str/bytes/...
## elements with finite and ordered 
s = 'spam'
len(s)
s[0]
"sp" not in s 
s = s + " and ham"
s.index('a')
s.count('m')
max(s)
"x" * 30
## slicing
s[0:3]
s[2:]
s[0:10:2]
s[::2]
s[-5:-1]
s[::-1]
s[:]  # shallow copy

###########################
## Lists

## Lists are sequences of heterogeneous objects
## List don't store the obj, store the reference (so memory size independant)
## Lists are mutable (doesn't need a copy => memory efficient)
## Sequences operations can be applied on lists
## Lists are highly flexible

a = []
type(a)
a = [1,2,3,4]
a[1:3] = [1,2,3] ## ! delete, then add
a[1:3] = []      ## ! delete
del a[1]
dir(list)
help(list.append)      # list.append? IPython
a.append(9)
a.extend(a)
a.sort(reverse = True) # modified by reference
b = sorted(a)          # sort and copy
s = "spam egg beans"
s = s.split()
s[0] = s[0].upper()
" ".join(s)
a = list(range(10))
a + a
a.insert(0, "a")
a.remove("a")  # first match only
b = a.pop(2)   # extract and remove (last one by default)
a.reverse()
a * 3  # duplicates n times


###########################
## If

## instruction block : + spaces
## <79 characters on one line better

if 'g' in 'egg':
    print('yes')
else:
    print('no')

## nested if: indent again

char = 'spam'

if 'a' in char:
    if 'b' in char:
        cas11 = True
        print('a and b')
    else:
        cas12 = True
        print('a but not b')
else:
    if 'b' in char:
        cas21 = True
        print('b but not a')
    else:
        cas22 = True
        print('neither a nor b') 

# if elif elif ... else

## More about if
# test can be any expression => bool evaluated (or len, 0 => false)
# built-in: False 0 [] {} () ''
# comparaison / membership ==, !=, is, is not in <=, <, >, >=
# operators:   and   or   not	


###########################
## For loops and functions

for i in range(10):
    print(i**2)

for i in [1, 2, True]:
    print(i)

a = []
for n in [1, 2, '3', 4, 'END']:
    a.append(str(n))

print(",".join(a))

for i, e in enumerate([1, 3, 5]):
    print(i, e)

def square(x):   # note: x passed by reference
    L = []
    for i in x:
        L.append(i**2)
    return L

def foo():
    return

type(foo())   # None

def foo2(): ## function that does nothing
    pass

for integer in range(1000):
    # ignore numbers non multiple of 10
    if integer % 10 != 0:
        continue
    print(f"processing {integer}")
    # stop at 50
    if integer >= 50:
        break


x = True
y = 1 if x else 0

a =  list(range(1,10))
while a:
    a.pop()
    if len(a) == 5:
        continue # break # continue goes to the top of the while
    print(a)

while True:
    s = input("what is your question?\n")
    if 'none' in s:
        break

# while can take an else



###########################
## Lists (and list comprehension)

a = [1,4,18,29,13]
import math
b = [math.log(i) for i in a]
a = [-1,4,18,29,13]
b = [math.log(i) for i in a if i > 0]
a = ["Eve","bob","TOM"]
a = [p.lower() for p in a]
entry = [1, 2, 3, 4, 5, 6, 7, 8, 9]
squares = [x**2 for x in entry] 
[(num1, num2) for num1 in range(1, 3) for num2 in range(3, 5)]
['positive' if x > 0 else 'negative' for x in [-2,2,3]]



## ----------------------------------------------------------
## ----------------------------------------------------------
## More about basic notions, shared references

###########################
## Files

f = open(r"c:\spam.txt", "w", encoding = "utf8") 
# r = rawstring
# r = read, w = write, a = append

for i in range(100):
    f.write(f"line {i + 1}\n")

f.close()

# !type or !cat c:\spam.txt # ipython only

f  = open(r"c:\spam.txt",  "r", encoding = "utf8") 
f2 = open(r"c:\spam2.txt", "w", encoding = "utf8") 

for line in f:
    line = line.split()
    line[0] = line[0].upper()
    f2.write(",".join(line) + "\n")
f.close()
f2.close()

## context manager: modern way to manipulate files
## context manager protocol, avoids to use .close()

with open(r"c:\spam.txt",  "r", encoding = "utf8") as f:
    for line in f:
        print(line) # file close automatically

## binary file (b before w indicates binary, e.g. pickled file)
with open(r"c:\spam.bin",  "bw") as f:
    for i in range(100):
        f.write(b'\x3d')    # bytes

import pickle
# Open pickle file and load data: d
with open('data.pkl', 'rb') as file:
    d = pickle.load(file)

# other:
# https://docs.python.org/3/library/pathlib.html
# https://docs.python.org/3/library/json.html

###########################
## Tuples (immutable lists)

## a tuple is a sequence
## tuples are immutable lists (useful for dictionnaries)

t = ()
t = (4,)            # (4) is simply an integer, use the comma
t = (True, 1, "a")
t = True, 1, "a"    # parentheses are not mandatory
1 in t 
t[0]
a = list(t)         # convert tuple to list
t = tuple(a)        # convert list to tuple
(a, b) = [3, 4]     # tuple unpacking
a, b = [3, 4]       # tuple unpacking
a = list(range(10)) # extended tuple unpacking
x, *y = a 
*x, y = a
1,3 + 3, 4, + 2,1 + 1,2 # weird...
up  = ["A", "B", "C"]
low = ["a", "b", "c"]
list(zip(up, low)) # zip function, more than two possible


###########################
## Dictionnaries 

# hash tables: set and dictionnaries
# time of operations is independant of the nb of elements
# e.g. access, insert, test in, delete, ...
# all immutable objects are 'hashable'
# no order in dictionnaries

age = {}
age = {'ana': 35, 'eve': 30, 'bob': 38}
age['ana']

age = dict(ana = 35, eve = 35, bob = 35)
a   = [('ana', 35), ('eve', 35), ('bob', 35)]
age = dict(a)
age['bob']
age['bob'] = 45  # see also update

del age['bob']
len(age)
'ana' in age
age.get("bob", 0)
k = age.keys() # k will be modified if age modified
age.values()
age.items()    # returns a vue (a vue is an iterable object)

for k, v in age.items():
    print(f"{k} {v}")

# see also collections module

###########################
## Sets

## related to dictionaries, but stores only keys, no values
## useful for unique values, or membership test
## better to convert a sequence to a set for in test

s = set()
type(s)
s = {1,2,3, 'a', True}
s = set([1,1,2,3,20,18,4])  # s is ordered, keys are unique
len(s)
1 in s
s.add("bob")
s.update([1,2,3,4,5,6,7])
s
s1 = {1,2,3}
s2 = {2,3,4}
s1 - s2 # difference
s1 | s2 # union
s1 & s2 # intersection
s1 ^ s2 # symetrical difference
a = [0]
#s{0}

# frozenset: set that can not be modified
fs = frozenset(s)  # fs.add(2) will fail

###########################
## Exceptions

## exceptions can be captured and bring info about the error
## frequently used mechanism in python

# 1 / 0 => ZeroDivisionError

def div (a,b):
    try:
        print(a / b)
    except ZeroDivisionError:
        print("Can not divide by zero")
    except TypeError:
        print("Numbers required")
    print("next...")

# try: captures exception, except: properly handles the error
# div(3, 1); div(3, 0); div(3,"a")

## bubbling => exceptions go up

def function_with_finally(number):
    try:
        return 1 / number
    except ZeroDivisionError as e:
        print(f"D'oh! {type(e)}, {e}")
        return("zero-divide")
    finally:
        print("Final action even if return called above")

function_with_finally(0)

def function_with_else(number):
    try:
        1 / number
    except ZeroDivisionError as e:
        print(f"D'oh! {type(e)}, {e}")
    else:
        print("Do this only if non-zero number")
    return 'Something else'

function_with_else(0)


###########################
## Shared references

## side effects
a    = [1,2]
b    = a
b[0] = 0
a
b    = a[:]          # use a shallow copy to avoid side effects 
# but if the list references a mutable object, shallow is not enough
# for example:
a = [1, [2]]
b = a[:]
a[1][0] = 9
b

import copy
b = copy.deepcopy(a) # deep copy

a is b  # check shared references
id(a)   # 'memory adress'

# https://docs.python.org/3/reference/datamodel.html#objects-values-and-types
# circular references...

el = [0]
myList = [el, el, el]
myList[0][0] = 1

myList = 3 * [ [0] ]
myList
myList[0][0] = 1
myList


###########################
## Classes

class C:
    pass

c1 = C()

# self corresponds to the class instance

class Phrase:
    def __init__(self, phrase):
        self.words = phrase.split()
    
    def upper(self):
        self.words = [m.upper() for m in self.words]
    
    def __str__(self):                # str allows to print the content 
        return "\n".join(self.words)

p = Phrase("hello world")
p.words    # words = attribute
p.upper()  # upper = method
print(p)


## ----------------------------------------------------------
## ----------------------------------------------------------
## Functions (scope), if, while, ...

###########################
## Functions

# functions are object, below ff is the variable that references the function

def ff(a,b,c):
    print(a,b,c)

g = ff
g(1,2,3)

# in Python, arguments are passed by reference (vs by value)
# side effect *IN PLACE*
# "MUST BE USED CAREFULLY", good for performance
# need to document properly using docstring (help(list.sort))

def add1(a):
    """
    Help of add1 function (docstring).
    """
    a.append(1)

L = []
add1(L)

# but using shallow copy may be more safe
def add2(a):
    a = a[:]
    a.append(1)
    return a

L = add2(L) # is more explicit

# polymorphism => execute on all the types compatible with the function
# for example
def my_add(a, b):
    print(f"{a} and {b}")
    return a + b

# my_add works on integers/floats/characters
# my_add(1, 2); my_add(1.0, 2.0); my_add("a", "b"); 

# type hints inform about expected types
# just to document, no check during execution	
nb_items : int = 0
def fact(n : int) -> int:
    return 1 if n <= 1 else n * fact(n-1)

from typing import List
def fun_with_hints(x: List[int]) -> List[str]:
    pass

# https://docs.python.org/3/library/typing.html#user-defined-generic-types

def fi(x):
    # use isinstance to check type of arguments
    if isinstance(x, int):
        return x + 1
    else:
        raise TypeError(x)   # raise ValueError('Error message')

fi("a")


###########################
## Parameters and arguments

## parameters: in the definition of the function
## arguments: variables passed for execution

def fff(a, b = 3): # default values can be used
    print(a, b)

fff(b = 3, a = 6)  # named
fff(5)           # ordered

def hh(*t):     # * arguments put in a tupple, number arbitraty
    print(t)

hh(); hh(1,2,3) # tupple

def jj(**d):
    print(d)

jj(a = 1, b = 2) # dictionary

# * and ** can also be used arguments even if not in parameters
L = [1,2,3]
hh(*L) # tupple unpacking
d = {"sep" : " and ", "end" :"\n\n"}
print(1,2, **d) # ** can be used to pass arguments as a dict

# https://docs.python.org/3/reference/expressions.html#calls
# be careful with mutable arguments!
# https://docs.python.org/3/faq/programming.html#why-are-default-values-shared-between-objects

###########################
## Scoping rules

## to access variables, Python follows the LEGB rule
## LEGB: Local, Enclosing, Global, Built-in
## Local (in the block of a function)
## Global variables (defined outside functions)

a, b, c = 1, 1, 1

def gg():
    b = 2
    b = b + 10
    # print(locals()) # b
    def h():
        c = 5
        print(a, b, c)
    h()

gg()

# a global, b enclosing, c local
print(a, b, c) # all global (print is built-in)
locals(); globals()

import builtins
dir(builtins) # accessible built-in functions 
builtins.print

# UnboundLocalError
# when trying to modify locally a referenced (used) global variable
# need to use the global instruction for that
# but not recommended: use parameters and assignment
## similarly, nonlocal instruction used to modify enclosing variables

# Namespaces
# global variables for each module
# how to communicate across namespaces?


## ----------------------------------------------------------
## ----------------------------------------------------------
## Iteration, import, and namespaces

###########################
## Iterators

s = {1,2,3,'a'}
[x for x in s if type(x) is int] # list comphrehension

it = iter(s)   # creates an iterator on s
it
next(it)
next(it)
next(it)
next(it)
next(it)      # StopIteration error

## iterable object vs iterators
# __iter__() # iterable objects have this method ## ''contains the data'
# iter(s) ~ s.__iter__()
# this method returns an iterator
## iterators have two methods: .__iter__() and .__next__() (goes through the data)
## iterator can be run over only once 
## simple, compact, very low cost to create

enum = enumerate([1, 3, 5], start = 1) # returns index and value
next(enum); next(enum); next(enum)
a = [1,2]
b = [3,4]
z = zip(a, b) # [tuple(a0,b0), tuple(a1,b1)]
z is iter(z)
[i for i in z]
[i for i in z] # used once, now empty

import itertools ## offers more functionalities for iterators (combinations, ...)
# https://docs.python.org/3/library/itertools.html


###########################
## Functional programming

## functional programing: use functions as objects and use them as argument of other functions

# lambda functions are anonymous, they are an expression
# sometimes, easier to use (avoids to declare a function)

# map: applies a function to each element
m = map(lambda x: x**2 - 1, range(10))
m
list(m)
## filter function
## filter an iterable object using a test
n = filter(lambda x: x%2 == 0, range(10))
n
list(n)

# map and filter produce iterables (usable once)
# map and filter are like list comphehension
# list comprehension is more pythonic


###########################
## Comprehension: lists, sets, and dictionnary (all iterable objects)

names = ["ana","EVE","Alice", "bob"]
[n.lower() for n in names if n.lower().startswith('a')] 
names.extend(names) # duplicates
[n.lower() for n in names if n.lower().startswith('a')] 
{n.lower() for n in names if n.lower().startswith('a')}
# curly brackets => unique values directly!

# list comprehension can also be used on dictionary
ages = [('Ana',20), ('Eve', 30), ('Bob', 40)]
ages = dict(ages)
{p.lower():a for p, a in ages.items()}
{p.lower():a for p, a in ages.items() if a < 40}

##
[n + p for n in [2, 4] for p in [10, 20, 30]]
[n + p for n in [2, 4] for p in [10, 20, 30] if n*p >= 40]


###########################
## Generator expressions

## Avoid to generate temporary objects
## Very memory-efficient
## List comprehension returns a list 
## Generators returns an iterator

sqr = [x**2 for x in range(1000)]
len(sqr)
sum(sqr)
sqr = (x**2 for x in range(1000))  # parentheses instead of square brackets
sqr
sum(sqr)
sum(sqr) ## iterator is over

# can be chained!
gen_sqr = (x**2 for x in range(1000))
palindrome = (x for x in gen_sqr if str(x) == str(x)[::-1])
list(palindrome)

# http://python-history.blogspot.com/2010/06/from-list-comprehensions-to-generator.html

## generative function

def gen():
    yield 10

gen()


###########################
## Modules and namespaces

# object.attribut
# access to an attribute in the object's namespace
# namespace: group of variables belonging to an object

import os
print(os)  ## os is a variable that references the module object
os.environ['PYTHONPATH']
import sys
sys.path # paths to search for modules
sys.modules
sys.builtin_module_names

## when a module is imported
## precompilation: byte code in __pycache__
## then byte code read to create the object module

## to force the reloading of a module
import importlib; importlib.reload(mod) 
# %load_ext autoreload   # for notebooks

# to build a custom module, use setuptools
# modules are mutable
# modules have their namespace
# see also packages (collection of modules)


###########################
## OOP

# a class allows to define a custom type
# calling a class creates an instance
# namespace instance first, then namespace class: inheritance tree
# method = function defined in a class

class Phrase0:
    my_phrase = "Python is fun."

Phrase0
p = Phrase0()
vars(Phrase0) # Phrase.__dict__  
p.my_phrase  # not defined in instance, found in the class
Phrase0.words = Phrase0.my_phrase.split()
p.words


class Phrase1:
    "Docstring for the Phrase class"
    def __init__(self, my_phrase):
    ## __init_ method is the constructor
        self.my_Phrase = my_phrase

# self = reference of the instance
p=Phrase1("Python is fun.")
vars(p)
help(Phrase1)


## special methods __something__
## allows to define methods that behave like builtin types
## len, print, in, +, ...
## a lot of special methods available (around eighty?)
## https://docs.python.org/3/reference/datamodel.html#specialnames

class Phrase2:
    def __init__(self, my_phrase):
        self.my_phrase = my_phrase
        self.words = my_phrase.split()
    
    def nb_letters(self):
        return len(self.my_phrase)
    
    def __len__(self):
        return len(self.words)
    
    def __contains__(self, word):
        return word in self.words
    
    def __str__(self):
        return " ".join(self.words)


p = Phrase2("Python is fun.")
p.words
p.nb_letters()
len(p)
"is" in p
print(p)


## inheritance
## an instance inherits from the class
## a class can inherit from other classes

s = "Python is fun."

class PhraseNoCase(Phrase2):
    def __init__(self, my_phrase):
        Phrase2.__init__(self, my_phrase)
        self.words_lower = {m.lower() for m in self.words}

pnoc = PhraseNoCase(s)
isinstance(pnoc, Phrase2)
isinstance(pnoc, PhraseNoCase)
pnoc.words_lower

## multiple inheritance
## MRO: method resolution order
## attribute resolution
## object = super class of all the classes

class CC:
    pass

CC.__bases__
CC.mro()  ## path followed in attribute resolution
## mro depends on the order the super classes are defined

# see also class property
# https://docs.python.org/3.6/library/functions.html#property


## define a class that is an iterator
class Phrase3:
    def __init__(self, my_phrase):
        self.my_phrase = my_phrase
        self.words = my_phrase.split()
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if not self.words:
            raise StopIteration
        return self.words.pop(0)

pp = Phrase3("Python is fun")  ## Phrase3 defined as an iterator
[m for m in pp]
# next(pp) => StopIteration
iter(pp)

## define a class that is iterable
class Phrase4:
    def __init__(self, my_phrase):
        self.my_phrase = my_phrase
        self.words = my_phrase.split()
    
    def __iter__(self):
        for m in self.words:
           yield m

ppp = Phrase4("Python is fun") ## Phrase3 defined as an iterable object
[m for m in ppp]
iter(ppp)


## use custom exception in classes

class Phrase5:
    def __init__(self, my_phrase):
        self.my_phrase = my_phrase
        if not my_phrase:
            raise EmptyPhraseError('The phrase is empty.')
        self.words = my_phrase.split()

class EmptyPhraseError(Exception):
    pass

Phrase5('ff')
Phrase5('')

try:
    Phrase5('')
except EmptyPhraseError as e:
    print(e.args)    # arguments as a tuple


## context manager

## with 



##############################
## variables and attributes

x = 10            # variable  => lexical scoping (?) , static
an_object.x = 10  # attribute => MRO, dynamic
## two different mechanisms
# modules, packages, functions, classes, instances can have attributes


##############################
## date and time

from datetime import datetime
now = datetime.now()
print(now)
print('%s/%s/%s' % (now.month, now.day, now.year))
print('%s:%s:%s' % (now.hour, now.minute, now.second))


##############################
## miscellaneous

# python -m http.server 8080
