

# import os

# path='C:\\Users\\scarcelli.fosm\\Desktop\\novo1.txt'

# if os.path.exists(path):
#    print ('That location exists')
#    if os.path.isfile(path):
#        print ('That is a file')
#    elif os.path.isdir(path):
#        print ('That is a directory')
# else:
#   print ('That location doesn\'t exists')

# try:
#    with open (path) as file:
#        print(file.read())
# except FileExistsError:
#    print('The file has not exists ')
# except FileNotFoundError:
#    print('The file has not encoutred')


# text = 'Yooooooooooooooooooooo\nThis is some text\nHave a good one!'
# text = 'This text has been overwritten'

# with open('test.txt','a') as file:
#    file.write(text)


# import shutil

# hutil.copyfile('test.txt','copy.txt')
# import os

# try:
#    os.remove('copy.txt')
# except FileNotFoundError:
#    print("file not found")
# except PermissionError:
#    print("You has not permission to remove this file")

# module

# import messages as print_messages

# print_messages.hello()
# print_messages.bye()

# from messages import bye

# bye()