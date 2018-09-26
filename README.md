<h1><center> The Monster Crash Course in Python </center></h1>

<img src="https://github.com/purcellconsult/Python-Core-Basics/blob/master/monster.png">

###### Monster: Art in Bloom 2009: Storming Party in Art Museum - Seongbin Im - Image - CC BY 2.0

I pretty much condense the core features of Python into a single chapter so that you can quickly get a grasp of the language. After this chapter you should become familiar with the built in data types, common operators, variables, strings, functions, data structures, control flow, iteration, modules, and classes. The point of this chapter is to equip you with the skills needed to start building your own Python programs. Also, I apologize in advance if the PAC-man-like ghost image is too grisly for you. 

### Variables in Python

A variable is a placeholder for data that’s changeable. Some examples of changeable data in the real world are day of the week, temperature, and your mood. Variables can hold a myriad of data types such as boolean or numeric. Python is a dynamically typed language, and therefore you can declare variables without explicitly stating a type and it will still compile just dandy. The following code snippets are all legal in Python: 

``` python
> a = 1
> b = 1.27398202
> c = "Jambo"
> d = '/0024'
> e = []
```
However, there are some rules that Python programmers must follow when creating variable names:

 - **Variables must be assigned**. For example `a = 5000` is allowed, but   
   simply writing a without assigning it is illegal. 	
  - The `=` sign is called the assignment operator, and inserts the value on the right of the equal sign to that of the variable name. 	
  - Variable names in Python may not start with a number. For example, `1c = "Hello"` is illegal, while `c1 = "Hello"` is OK. 	
  - Underscore is allowed in variable names. For example, the following are allowed:
	  -  `>>> mymesaage = "hey"`
	  -  `>>> my_message = "wake up"`
	 -    `>>> _my_message = "wake up"`
	 -    `>>> mymessage_ = "wake up"`
- Variable names are case sensitive as `a = 5`, and `A = 10` are allowed.
- It’s legal to reassign variables. For example, the following code snippet is allowed and legal: 

``` python
>>> a = 1
>>> a = 1.1
>>> a = 'c'
>>> a = "c"
>>> a = [1, 1.1, 'c', "c"]
>>> a
[1, 1.1, 'c', 'c']
```

### Lists

Python has a built in data type known as a list that’s a mutable, or changeable ordered sequence of elements. A list could contain numbers, strings, booleans, tuples, sets, or other lists as elements. To create a list use the square bracket `[]` notation: 

``` python
>>> []
>>> [2, 4, 6, 8, 10]
>>> [True, False, True, True, False]
>>> ["hip hop", "rock and roll", "country", "electronic"]
```
To access an element in an array you can use the subscript notation, or:

    list[index]

The first element corresponds to the index of 0. Let’s take the following list as an example:

```python
>>> list = [12, 382, 29, True, False, "Hello", 23.292]
>>> list[2] * 2
58 
>>> list[4] = True
>>> list
[12, 382, 29, True, True, 'Hello', 23.292]
```

Also, list elements can be accessed using negative list notation. The notation `list[-1]` will allow you to access the last element. 

```python
>>> list[-1]
23.292
```
In this example the length of the list is -7, so `list[-7]` will get you the first element.
```python
>>> list[-7]
12
```
It’s important to keep track of the accessible indexes in the list. For example, if you try to access an index that doesn’t exist an error will occur, like `list[7`]. 

```python
>>> list[7]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
```
The length of a list is the total amount of elements that it contains, and you can access it by using the `len()` function. Therefore, to get the length of a list, use `len(characters)` which is equal to 5. To get the last element of the list you can do:
```python
>>> characters[len(characters) – 1] 
```
Here's a diagram that visually represents the following list in Python:

<img src="https://github.com/purcellconsult/Python-Core-Basics/blob/master/list.png" />

They say a picture is worth a thousand words so ideally the diagram clarifies lists for you. The list in Python is considered a sequence type, and sequence types in Python have a set number of operations. Below is a list of some of the operators that can be applied to sequence types. 

```python
>>> x = [2, 622, 8768, 981, 90]
>>> 622 in x
True
>>> 100 not in x
True
```
Lists can be concatenated or combined with the plus (+) operator. 

```python
>>> a = [1, 2, 3]
>>> b = [4, 5, 6]
>>> a + b
[1, 2, 3, 4, 5, 6]
```
Lists can be multiplied by using the asterisk (*) operator.

```python
>>> a = [1, 2]
>>> b = a * 3
>>> b
[1, 2, 1, 2, 1, 2]
```

You can get the length of a list by using the `len()` method and you can also get the smallest and largest item of a list by using the `min()` and `max()` methods appropriately.

```python
>>> a = [2, 4, 6, 8, 10]
>>> len(a)
5
>>> min(a)
2
>>> max(a)
10
```

### Tuples

A **tuple** is similar to a list as it can group multiple objects together but the main distinction is that it’s immutable. This means that an element can't be added to an existing tuple, but another variable is created that point to the same object. An example of how to create a tuple along with some of their functions is listed below: 

```python
>>> tuple = (100, 200, 300, 150)
>>> tuple
(100, 200, 300, 150)
>>> tuple[0]
100
>>> tuple[1:3]
(200, 300)
>>> color = ("red", "green", "blue")
>>> color[0] = "gray"

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
```
Oops! Remember, tuples are immutable so once created the elements can’t be changed. Tuples like lists can be nested, so the following is OK:
```python
>>> a = (1,2,3)
>>> b = (2,1,5)
>>> c = a, b
>>> c
((1, 2, 3), (2, 1, 5))
```
Therefore, if you're writing code in which an immutable object is required then a tuple is a good choice to consider. Tuples are commonly used as keys for dictionaries. 

### Dictionaries

According to the official Python documentation its best to think of dictionaries as sets of key value pairs with the requirement that keys are unique within one dictionary. A pair of curly braces `{}` creates an empty dictionary, and placing a comma separated list of key/value pairs inside the braces adds initial key/value pairs to the dictionary. 

Below is a demo of the dictionary data structure in Python: 
```python
>>> cars = {'Koenigsegg' : 4800000, 'Ferrari' : 3000000, 'Lamborghini' : 4500000}
>>> cars['Ferrari']
3000000
>>> del cars['Koenigsegg']
>>> cars
{'Ferrari': 3000000, 'Lamborghini': 4500000}
>>> sorted(cars)
['Ferrari', 'Lamborghini']
>>> 'Lamborghini' in cars
True
```
### Sets

Sets are a popular topic in mathematics and are taught to children at a young age. Some topics such as Venn diagrams are fun and easy to get a hang of. In Python you’ll want to use sets to represent objects in which uniqueness is prominent. If you have a duplicate object in a set then it will be ignored. There are two ways in which you can create a set in Python:

- `set()`
- Or, by assigning a variable to `{}`

Here are some examples of sets in action in Python: 
```python
>>> a = {1, 1, 2, 2, 0, 56, 98, 6, 5, 5, 77}
>>> b = {1, 2, 3, 4, 5}
>>> a | b
{0, 1, 2, 98, 3, 5, 6, 4, 77, 56}
>>> a & b
{1, 2, 5}
>>> a - b
{0, 98, 6, 77, 56}
>>> a ^ b
{0, 98, 3, 4, 6, 56, 77}
```

### Slicing

Slicing allows you to partition a list within a delineated range. The syntax for slicing a list is shown below:

    a[i:j] = b

Below are examples of how to use slicing on a List.
```python
>>> characters = ['a', 'c', 'z', 'e', 'b']
>>> characters[0:3]
['a', 'c', 'z']
>>> characters[0:-2]
['a', 'c', 'z']
>>> food = ["apples", "pasta", "potatoes", "bread", "milk", "beef"]
>>> food[0:2]
['apples', 'pasta']
```
Also, like with normal indexes you can also access negative indexes, for example, ```python food[-1]``` would equal beef. You can also generate subsets of lists by slicing it using a myriad of techniques:

```python
>>> food[1:]
['pasta', 'potatoes', 'bread', 'milk', 'beef']
>>> food[:4]
['apples', 'pasta', 'potatoes', 'bread']
>>> food[:]
['apples', 'pasta', 'potatoes', 'bread', 'milk', 'beef']
>>> food[1:-1]
['pasta', 'potatoes', 'bread', 'milk']
```
Also, if you add an additional colon then you can create a subset of the list by defining the step that you can take with each increment. 

```python
>>> b[0:6:2]
[1, 1, 1]
```

### Strings and Common Operations in Python

If you're new to programming and never heard of strings then just think of it as a bunch of text. There are three ways in which you can represent text in Python. You can use single quote strings, double quotes, or triple quotes. For example, the following are all valid ways in which you can create strings in Python. 

```python
>>> a = "Hello World"
>>> b = """Hello World"""
>>> c = 'Hello World'
>>> d = '''Hello World'''
```
To get a good idea of how strings work let's take a look at the following diagram:

<img src="https://github.com/purcellconsult/Python-Core-Basics/blob/master/strings.png">

As you can see from the above diagram, a string is like a list of characters. Each character in a string can be accessed at its index which starts at 0 and goes up to the length of the string minus one. Therefore, to access the first element of the string you can do this:
```python
>>> a[0]
'H'
```

To access the last element of a string you can use the following notation:
```python
>>> a[len(a)-1]
'd'
```
Strings are immutable which means that once they’re created they can't be changed. Below is an example of how operators can be applied to strings in Python:

```python
>>> "The" + " Cat"
'The Cat'
>>> "Salut, mes amis " * 2
'Salut, mes amis Salut, mes amis'
>>> "i" in "Ciao"
True
>>> "a" not in "Jambo"
False
```
Like lists, strings can also be sliced: 

```python
>>> message = "Hello World"
>>> message[0:5]
'Hello'
```

### if statement 

The following shows how the if-statement works in Python:

if 5 < 10:        					     
    print("CORRECT!")
			 
CORRECT!

<img src="https://github.com/purcellconsult/Python-Core-Basics/blob/master/if_statement.png" />
  		
In the above diagram the diamond represents the expression to be tested which is 5 < 10. Since it evaluates to True, 
the statements in the body are executed. 

The following code snippet represents an if-else statement in Python:

```python
if 5 > 10:
    print("CORRECT")
else:
    print("WRONG")
```

    WRONG

It's similar to the if statement except that it also has an else statement which is executed by default if the text expression evaluates to False. The below diagram illustrates how this works:

<img src="https://github.com/purcellconsult/Python-Core-Basics/blob/master/ifelse.png" />

### elif statement 

The last flavor of if statements are `elif`. There can be 0 or more `elif` statements and the else statement is completely optional. The `elif` keyword is shorthand for 'else if'. Multiple `elif` statements can be chained together to create the logic that's equivalent to a switch statement. The below code snippet illustrates `elif` statements in Python: 
```python
if 1 > 2:
    print("1 is greater than 2")
elif 1 < 2:
    print("1 is less than 2")
elif 1 == 2:
    print("1 is equal to 2")
else:
    print("Something's fishy")
```

    1 is less than 2

The below diagram illustrates the logic behind elif statements in Python: 

<img src="https://github.com/purcellconsult/Python-Core-Basics/blob/master/elif.png" />

### While loop

In plain English, the while loop states "that while something is true, then do this." A simple example from the real world is while its business hours, keep the store open. Now, let’s translate this logic into Python pseudo code:

```python
while condition is True:
	do this
```

Below are some examples that show how to use while loops in Python. 

``` python
x = 1
while x < 5:
    print("x = ", x)
    x = x + 1
    
x =  1
x =  2
x =  3
x =  4
```
Here's a list of some of the Fibonacci numbers:

    1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144,...

Here’s the Python code that will compute the first 100 Fibonacci numbers:
```python
n, a, b, count = 0, 1, 1, 1
while n <= 99:
    print("n =", count, ":", a)
    a, b = b, a + b
    n+=1
    count+=1
 ```

Here's an alternative sequence for Fibonacci numbers: 

    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, …

Here’s the corresponding `while` loop for this:

```python
n, a, b = 0, 0, 1
while n <= 100:
    print("n =",n, ":", a)
    a, b = b, a + b
    n+=1
```

### The for loop

The for loop in Python is a wee-bit different from the for loop in C-style languages such as Java that allows you to set a starting variable, condition, and then update that starting variable. Instead, Python will allow you to iterate over a sequence of numbers using the built in `range()` function. The pseudo code below illustrates the structure of a for loop in Python: 

```python
for variable in range():
    do this
 ```

Here’s a simple example of how the for loop works in Python: 
```python
for x in range(5):
    print("x =", x)
... 
x = 0
x = 1
x = 2
x = 3
x = 4
```
With the `range()` function the starting point is at 0 or less specified, and the ending point is at 5.  Note, the `range()` function will never print the endpoint, it will always stop one short of it. So, the starting point is inclusive and the ending point is exclusive. 

Here’s another example of the for loop in action:
```python
for x in range(50, 100):
    if x % 2 == 0 and x % 3 == 0:
        print("ABC")
... 
ABC
ABC
ABC
ABC
ABC
ABC
ABC
ABC
```

The above makes use of the modulus operator (%) which checks the remainder after it’s divided by a number. For example, since 50/ 2 equals 25, there’s no remainder. The loop check what numbers from 50 to 99 is divisible by 2 AND 3. If a match is found then the text "ABC" is printed. 

You can also specify the "step" in which you’ll iterate over the sequence by adding a third parameter. For example, let’s look at the following code snippet:

``` python
for x in range(1,10,2):
    print(x)
 ```
 
The output when printed is:

    1
    3
    5
    7
    9

The loop starts at 1 and goes to 10. The step in which it iterates is 2, so the loop prints 1, 3, 5, 7, 9. If you want to print all of the even numbers in the range of 0-10 including 10 then you’ll write this:

```python
for x in range(0,11,2):
    print(x)
... 
0
2
4
6
8
10
```

You can nest loops as many levels as you wish, or including a loop inside another. For example, here’s a triple loop, or two loops inside another loop: 

```python
for i in range(1,10):
    for j in range(1,3):
        for k in range(1,3):
            print("i=", i, "j=", j, "k=", k)
   ```

The output is this:

    i= 1 j= 1 k= 1
    i= 1 j= 1 k= 2
    i= 1 j= 2 k= 1
    i= 1 j= 2 k= 2
    i= 2 j= 1 k= 1
    .
    .
    .
    i= 9 j=2 k=2

### break, continue, and pass statements

Imagine that a loop you write is a contract. What you think happens if you broke the contract of the loop? One thought would be that it would be terminated. You can definitely terminate a loop by breaking it and how to do so is listed below: 

```python
x = 0
while(True):
    print(x)
    if(x == 1000):
        break
    else:
        x = x + 1
   ```

The above prints the numbers from 0 to 1000 and breaks or terminates at 1000. This is important because the condition of `while(True)` means that the loop will iterate indefinitely because that condition is always `True`. Therefore, a way to exit out of the loop is to inject a conditional that triggers the end of a loop. The `continue` statement does the opposite. It skips the body statements once the condition is `True`: 

```python
while(x < 10):
    x+=1
    if(x == 5):
        continue
    else:
        print(x)
```

    1
    2
    3
    4
    6
    7
    8
    9
    10

Also, there’s the `pass` statement which is simply a placeholder. You would use it when a statement is required syntactically but no code needs to be executed. At first glance this seems identical to the `continue` statement but to get a better understanding let’s look at the two snippets of code:

    Code a:
```python
for x in range(1,10):
    if(x == 5):
        pass
        print(x)
    else:
        print(x)
        
        1
        2
        3
        4
        5
        6
        7
        8
        9
```

     Code b:

```python
 for x in range(1,10):
    if(x == 5):
        continue
        print(x)
    else:
        print(x)
        
    1
    2
    3
    4
    6
    7
    8
    9
 ```
In code snippet `a`, the `pass` statement does nothing so the values of 1-9 are printed. In code snippet `b`, the `continue` statement is instead used which forces execution of the next iteration. Therefore, the statements following the continue statement are not executed and the numbers 1-4, and then 6-9 are printed. 

### Iterating over data structures in Python

Let’s learn how to iterate over lists in Python.
```python
>>> animals =  ["lion", "fossa", "okapi", "spider crab", "maned wolf"]

>>> for x in animals:
        print(x)
```

    lion
    fossa
    okapi
    spider crab
    maned wolf

The following code snippet checks to see if "okapi" is in the list and if it is it gets printed:

```python
animals =  ["lion", "fossa", "okapi", "spider crab", "maned wolf"]
for x in animals:
    if x == "okapi":
        print(x)
  ```

    okapi

You could alternatively use the while loop to iterate over lists. You’ll need the help of the built-in `len()` function so that you know where to increment up to. Below is an example of how you’ll accomplish this with a while loop:

```python
animals =  ["lion", "fossa", "okapi", "spider crab", "maned wolf"]
i, j = len(animals), 0
while j < i:
    print("index = ", j, ":",  animals[j])
    j+=1
```
    index =  0 : lion
    index =  1 : fossa
    index =  2 : okapi
    index =  3 : spider crab
    index =  4 : maned wolf

### Creating Functions

A function in mathematics is similar to a function in computing. You take in some input and then it spits out some output. Here’s a list of some simple functions in mathematics:

Square function: f(x) = x2 
Cube function: f(x) = x3
Square root function: f(x) = √x
Reciprocal function: f(x) = 1/x

To create a function use the following syntax:

```python
def function_name(parameters)
    insert statements
 ```
 
The word `def` is a reserved keyword which you can use to represent that you have created your function. The `return` keyword is a reserved word that reveals that the function returns a value when called. Below is a list of simple functions in mathematics converted to Python: 

```python
def square(n):
    return n * n
    
>>> square(2)
4

def triple(n):
    return n * n * n

>>> triple(4)
64

from math import sqrt
def square_root(n):
    return sqrt(n)

>>> square_root(28)
5.291502622129181

def reciprocal(n):
    return 1/n
    
>>> reciprocal(5)
0.2
```
Once you create a function you need a way to use it which in technical terms is called invoking a function. There are several ways in which you can invoke a function in Python. A simple way as you saw from the previous example is to include the function name and then pass the input aka arguments into the parentheses. Therefore, it’ll look something like the following:

    c = function(a,b)

You can also call functions using keyword arguments. When the function is invoked a specific keyword or words are used to specify the input into the function. For example, the function looks like the following: 

```python
def sounds(goat = "bleat", mice = "squeak", oxen = "moo", horses = "neigh"):
            print("Billy goats", goat)
            print("Mice", mice)
            print("Ox", oxen)
            print("Horses", horses)

>>> sounds("neigh", "oink, oink", "talk", "bark")
```

    Billy goats neigh
    Mice oink, oink
    Ox talk
    Horses bark

Python also includes two helpful conventions when it comes to creating functions which are the `*` and `**` symbols. When a single star is used then you can pass in an arbitrary number of arguments into the function. Even though `args` is typically used as the parameter, it can in fact be any name. An example of the function in action is listed below:

```python
def fun(*args):
    for x in args:
        print(x)
        
>>> fun(1, 10, 20, 30, 40, "Hippo!")
```

    1
    10
    20
    30
    40
    Hippo!

When you include two stars this means that you can use an arbitrary number of keyword arguments or `**kwargs` for short. Like with `args`, `kwargs` is simply a variable and not a reserved keyword. Below is an example of how to use `kwargs`: 

```python
def function(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)
        
>>> function(name = "Sir James", city = "Tokyo", fruit  = "Apple", animal = "Bear")
```
    name : Sir James
    city : Tokyo
    fruit : Apple
    animal : Bear

### Functional Programming in Python

In programming a lambda is a function that’s not glued to an identifier. Hence, it’s commonly referred to as an anonymous function. Lambdas are commonly used in functional programming languages like JavaScript and Scala. Let’s first look at a regular function and then we’ll translate that into an anonymous one.

```python
def algebra(x, y, z):
    return 5*x + 6*y - z
 
>>> algebra(1, 2, 3)
```

    14

The above function is a simple mathematical equation that takes in some inputs and returns a value. We can translate this into an anonymous function as follow: 

```python
>>> result = lambda x,y,z : 5*x + 6*y - z
>>> result(1,2,3)
14
```
You could compute the above without assigning it to a variable but the issue with that is that you’ll never be able to use the anonymous function again. That’s OK if you have plans on using it in a one-off fashion, but if not then assigning it to a variable is a good idea for reuse. Here’s the general syntax for lambda functions:

```python
lambda input : output 
```
The lambda keyword is a reserved one in Python and is followed by all of the input variables. A colon `(:)` is used to separate the input from the output, or what’s returned. There are also several other cool things that you can do with the aid of lambdas such as map, filter, and  reduce. For example, let’s analyze the following code fragment: 

```python
numbers = [1,2,3,4]
list = []
for x in numbers:
    list.append(x*3)
>>> list
```
    [3, 6, 9, 12]

The following code can be replicated using what’s known as a map shown below:

```python
>>> numbers = [1,2,3,4]
>>> list(map(lambda x: x*3, numbers))
[3, 6, 9, 12]
```
The lambda expression is passed to the `map()` function which returns an iterator object that applies the function to every item of the iterable. The returned result is then passed to the `list(`) function that converts the output to a list. In various programming languages a map is considered a **higher-order** function that applies a given function to every element in a list. 

A **filter** is a function that extracts each element of the sequence for which the function returns `True`. Look at how the filter is applied to the following function: 

```python
>>> data = [.0212, .789, .897, .9821, 1.020, 1.121, 1.567]
>>> list(filter(lambda x: x > 1, data))
[1.02, 1.121, 1.567]
```
The lambda accepts an input of `x` and returns `x > 1`. A list named `data` is supplied as a second argument in the lambda and then the filter function is applied to all of the elements in data; only the elements that are greater than 1 are returned. 

The **reduce** higher order function takes a list and then reduces it to a single value by applying the function. In Python3 it’s not a builtin function, but it has been sent to the `functools` module. Guido van Rossum, the creator of Python suggests that an explicit for loop is more readable than `functools.reduce()` 99% of the time. For an example, let’s say that you have a list of numbers and simply wanted to sum all of them up. One way to do this is as follows: 
```python
data = [1,1,2,2,3,4,5]
i = 0
for x in data:
    i+=x
>>> i
```

    18

However, you can make your code more compact by using the `reduce()` function. First, import `reduce()` from the `functools` module and then pass the lambda into reduce()as shown below: 
```python
>>> from functools import reduce
>>> data = [1,1,2,2,3,4,5]
>>> reduce(lambda x, y: x + y, data)
18
```
There's also something called list comprehensions which are a syntactic construct that allows for the creation of new lists based on existing ones. For example, let’s say that we want to create a list of booleans that returns `True` or `False` for the first 10 positive digits. We want to return `True` if the digit is greater than 5, and `False` any other time. One way to do this would be as follows: 

```python
truth = []
for i in range(1,11):
    if i > 5:
        truth.append("True")
    else:
        truth.append("False")

>>> truth
```

  

    ['False', 'False', 'False', 'False', 'False', 'True', 'True', 'True', 'True', 'True']

However, with list comprehensions we can get the same result b using just a single line of code: 
```python
>>> [x > 5 for x in range(1,11)]
[False, False, False, False, False, True, True, True, True, True]
```

## Coding Challenges

**Challenge 1**: Write a function named `factorial_reduce()` that computes the factorial of any positive number with the caveat being that you must use a lambda and the `reduce()` function from the `functools` package. The function should be able to compute the factorial in just a single line. Here’s the template of the code to get started:
```python
from functools import reduce
def factorial_reduce(n):
    return...
```
**Challenge 2**: Write a function named `factors()` that lists all of the factors of an integer `n`. Below is the function signature: 
```python
def factors(n):
    """lists the facts of an integer n"""
```
Here are some sample test cases so that you can test your code against: 

    >>> factors(7)
    1
    7
    
    >>> factors(14)
    1
    2
    7
    14
    
    >>> factors(20)
    1
    2
    4
    5
    10
    20
    
    >>> factors(2.1)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "<stdin>", line 3, in factors
    TypeError: 'float' object cannot be interpreted as an integer

**Challenge 3**: Write a function named `fo_shizzle_my_nizzle()` that prints a string contingent on the following conditions. The letter n is used as input. 

 - fo → n is less than 0.  
 - shizzle → n is in the range of 1-49, 1 is inclusive, and 49 is exclusive.   
 - my → n is in the range 50-100, with 50 and 100 being inclusive.  
 -  nizzle → n is even, divisible by 3, and greater than 100.  
 -  '' ''→ if none of the above conditions are met then an empty string is printed by default.
 
Write a loop that tests the input in the range of -10...150. Here’s some sample test cases: 

    -5 → 'fo'
    0 → ' '
    8 → 'shizzle'
    52 → 'my'
    150 → 'nizzle'

**Challenge 4**: Write a function called `compute_pattern()` that accepts a number `n` and then prints the following pattern: 

1 
2 3 
3 4 5 
4 5 6 7 
5 6 7 8 9 
6 7 8 9 10 11 
7 8 9 10 11 12 13 
8 9 10 11 12 13 14 15 
9 10 11 12 13 14 15 16 17 

**Challenge 5**:  Bubble sort is classic sorting algorithm. It’s not recommended to use when performance is important, but regardless of its shortcomings it’s still a nice learning exercise. Write a function named `bubble_sort()` that accepts a list and then sorts it from least to greatest order. Below is a sample list named items to test on: 

    items = [92, 7, 38, 37, 92, 37, 12, 54, 43, 67, 78, 83, 93, 101, 128, 139, 156]
    
Here's the output:
```python
>>> bubble_sort(items)
[7, 12, 37, 37, 38, 43, 54, 67, 78, 83, 92, 92, 93, 101, 128, 139, 156]
```
<h3><u><a href="https://github.com/purcellconsult/Python-Core-Basics/blob/master/PyCore_Code_Challenges.py"> Solutions to the coding challenges </a></u></h3>
