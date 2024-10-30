def square(x):
    return x*x


for i in range(10):
    print(f"The square of {i} is {square(i)}")

name = 'Fred Scarcelli'
age = 35

first_Name = name[:4].upper()
last_Name = name[4:].lower()


def Hello(first_Name, last_Name, Age):
    print("Hello "+first_Name+""+last_Name)
    print("You have "+str(age)+" Years old")


Hello(first_Name, last_Name, age)


def multiplicate_numbers(num1, num2):
    return (num1*num2)


print(multiplicate_numbers(2, 4))


def Hello(first, middle, last):
    print(first, middle, last)


Hello(last='first', first='middle', middle='last')


def sum_numbers(*args):
    sum = 0
    print(args)
    for i in args:
        sum += i
    return sum


print(sum_numbers(2, 4, 2))
print(sum_numbers(2, 4))
print(sum_numbers(2, 4, 2, 10))


#####################################
# DECORATORS - FUNCTION ON FUNCTION

def announce(f):
    def wrapper():
        print("About to run the function...")
        f()
        print("Done with the function")
    return wrapper


@announce
def hello():
    print("Hello, World!")


hello()

#####################################
# LAMBDA FUNCTION

people = [
    {"name": "Harry", "house": "Cuiaba"},
    {"name": "Fred", "house": "Maceio"},
    {"name": "Ceci", "house": "São Paulo"},
]

# def f(person):
#    return person["name"]

# people.sort(key=f)

people.sort(key=lambda person: person["name"])
print(people)

# import math

# pi = -3.14
# x,y,z = 2,4,6

# print(round(pi))
# print(math.ceil(pi))
# print(math.floor(pi))
# print(abs(pi))
# print(pow(pi,2))
# print(max(x,y,z))
# print(min(x,y,z))


# import time

# for seconds in range (10,0,-1):
#    print (seconds)
#    time.sleep(1)

# print('Happy new year')

# rows = int(input('How much lines: '))
# columns = int(input('How much columns: '))
# symbol = input('what a symbol')

# for i in range(rows):
#    for j in range(columns):
#        print(symbol, end="")
#    print()

# while True:
#    name = input('What is your name? ')
#    if name != "":
#        break;
# print (name)

# while True:
#    name = input('What is your name? ')
#    if name != "" and name != "Fred":
#        break
#    elif name =='Fred':
#        continue
# print (name)

# phone_number = "123-456-789"

# for i in phone_number:
#    if i =='-':
#        continue
#    print(i)

# def Hello(**kwargs):
#   print('Hello '+kwargs['first']+' and '+kwargs['last'])
#    for key,value in kwargs.items():
#        print(key,value)

# Hello(first="Fred", middle="teste", last="Scarcelli")


# text = 'The {} jumped over the {}'

# print(text.format('cat','bed'))

# name = 'Frederico'
# print('My name is {}'.format(name))
# print('My name is {:20} Nice to meet you'.format(name))
# print('My name is {:<20} Nice to meet you'.format(name))
# print('My name is {:>20} Nice to meet you'.format(name))
# print('My name is {:^20} Nice to meet you'.format(name))

# pi = 3.14159
# print('The number is {:.2f}'.format(pi))
# print('The number is {:.3f}'.format(pi))

# number = 1000

# print('The number is {:,}'.format(number))
# print('The number is {:b}'.format(number))
# print('The number is {:o}'.format(number))
# print('The number is {:x}'.format(number))
# print('The number is {:e}'.format(number))

# import random

# x=random.randint(1,6)
# y=random.random() #0 to 1

# print(x)
# print(y)

# myList = ['Rock','paper', 'scissors']
# z = random.choice(myList)

# print(z)

# cards=['1','2','3','4','5','a','b','c']

# random.shuffle(cards)

# print(cards)


