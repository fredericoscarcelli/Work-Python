"""
name = 'Fredmoraes'
name2 = 'Moraes'


print (len(name))
print ("teste "+str(int))
print(name.capitalize()) first carcter upper
print(name.find('F'))
print (name.upper())
print (name.lower())
print (name2.isdigit())
print (name2.isalpha())
print (name.count('e'))
print (name.replace("e","u"))
print (name)

x = 2
y = 3.0
z = '4'

y=int(y)

print(x)
print(y)
print(z*3)
"""

name = input('Whats your name: ')
age = int(input('How old are you: '))
height = float(input('How tall are you: '))

# format function
# print('Your name is: '+name)
print(f"Your name is {name}")
# print('You have '+str(age)+' years old')
print(f'You have {str(age)} years old')
# print('You have '+str(height)+' cm tall')
print(f'You have {str(height)} cm tall')
