#name slicer

fullname = input("Enter Your Name : ")

sure = fullname[:fullname.index(' ')]
last = fullname[fullname.index(' ')+1:]

slicer = "Your First name is {} \nYour last name is {}".format(sure, last)
print(slicer)