"""
This part of my life is called - Being A Python ...

Before we start on anything, be it a programming language, learning music, trying to master a new skill, we start with
the very first basics. This is my journey to master Python and to relate it with the 'little' things I know till date.
"""

""" Seeking Blessings from the God of Wisdom - Hello World"""
print("Hello World!")


""" 
Types in Python
----------------

Python is a dynamically typed language; Meaning - the interpreter is smart enough to identify the variable type 
automatically. But, in the recent version [from 3.6], there is an additional feature which enable us to provide type
hints in the language. Unlike the different typed languages out there(which has a plethora of types), Python only has 
a limited list of types which makes learning the language very easy.   
     
Integers and Floats
-------------------
     
Defining Numeric and Decimal variables are pretty simple and straight forward.
"""

numeric = 30
print(numeric)

floating = 80.244
print(floating)

"""
You can also cast/convert numeric/decimal values to and fro in a very convenient manner.
"""
print(float(numeric))
print(int(floating))


"""
Strings
-------

Strings can be defined in the following ways 
  - values encapsulated in single quotes
  - values encapsulated in double quotes
  - values encapsulated in 3 * double quotes.  - This can also be used as Comments.
"""

string_form1 = 'hello'
string_form2 = "hello"
string_form3 = """hello"""

print(string_form1 == string_form2 == string_form3)


"""
There are lot of built in functions associated with Strings and are quite handy
"""

print(string_form1.capitalize())
print(string_form1.replace("l", "A"))
print(string_form1.isalpha())
print(string_form1.isdigit())
print((string_form1 + "," + string_form2 + "," + string_form3).split(","))

"""
We also have different ways to format the string including the string interpolation
"""
name = "Neo"
machine = "Oracle"
print(f"Nice to meet you {name}! I am {machine}")
print("Nice to meet you {0}! I am {1}. Choose the red Pill, {0}".format(name, machine))

"""
Booleans Types
--------------

Booleans denotes the true or flag values as in any programming language. The basic difference which I could notice is 
that the [T]rue and F[alse] starts with an upper case letter. The Boolean value can be casted/converted to its 
equivalent String & Integer [0/1] values.   
"""
neg_boolean = False
positve_boolean = True
print(int(neg_boolean))
print(int(positve_boolean))
print(str(positve_boolean))

"""
None Types
----------

None is similar to Null in other languages. When we assign None to a variable, it gives a simple direction that the 
variable has be created but it is not associated with any value. 
"""
none_thing = None
print(none_thing)


"""
IF Statements
-------------

The IF conditional statements works just like any other programming languages but with a minor difference in the styling 
and formatting. Both IF and else ends with ":" and uses indentation for identifying the code blocks. 
"""
test_bool = True

if test_bool == True:
    print("It's working!")
else:
    print("It's not working!")

"""
The IF statements can also be used to check the truthy and falsy value (whether the variable has been defined or not)
"""
truthy_thing = None

if truthy_thing:
    print("It's defined!")
else:
    print("It's not defined!")
    print("It's not defined!, Multiple blocks")
"""
Python also supports ternary if Blocks which yields a value if the condition satisfied and another if otherwise. 
"""
print("Smaller") if 1 < 2 else print("larger")

"""
You can also use multiple conditions in the IF block by using AND | OR
"""

if ((1 < 2 and 4 < 6) or 1 == 1):
    print("Multiple statements are checked!")
else:
    print("Multiple conditions are not being validated!")