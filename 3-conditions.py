n = int(input("Number:"))

if n > 0:
  print("n is positive")
elif n<0:
  print("n is negative")
else:
  print("n is zero")

age = int(input("how old are you:"))

if age>=18 and age<100:
  print ("you can drink beer")
elif(age<=0):
  print ("incorrect age are digited")
elif(age==100):
  print ("are you a century person")
else:
  print("you can\'t drink beer")
