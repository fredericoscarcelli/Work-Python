import sys

try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
except ValueError as e:
    print("Enter only number please")
    # print(e)

try:
    result = numerator/denominator
except ZeroDivisionError as e:
    print("You can't divide by zero, Idiot")
    # print(e)
    sys.exit(1)
except Exception as e:
    print('something went wrong:(')
else:
    print(result)
finally:
    print('end')
