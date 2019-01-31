user_input=str(input("Enter the name of the file you want to create dont forget to include the extension :"))
fileobj=open(user_input,'r+')
print("Chooose the options below")
print("1 for read from existed file .")
print("2 for write to existed file .")
a=int(input("Enter your choice here: "))
if a is 2:
    fileobj=open(user_input,'a+')
    string=str(input("Enter the data here :"))
    fileobj.write(string)
    print("The file after editing ")
    print(fileobj.read())
    fileobj.close()
    
if a is 1:
    print(fileobj.read())