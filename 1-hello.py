import functions #import entire module
# from functions import square #import just function of module

print('hello world')

# for i in range(10):
#    print(f"The square of {i} is {square(i)}")

for i in range(10):
    print(f"The square of {i} is {functions.square(i)}")
