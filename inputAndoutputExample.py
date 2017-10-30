print("So this is an easy example of input and output in python")
username = input("What is your name: ")
userphone = int(input("What is your phone number: "))
useraddress = input("What is your address: ")
usercurrentlocation = input("What is your current location: ")
userdata = [username, userphone, useraddress, usercurrentlocation]
userinput = input("So you wanna know how much i know you (y)or(n)")
while userinput == y :
  for data in userdata :
    print("So Here is my {}".format(userdata[data]))
    
