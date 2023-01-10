print("Welcome To the Login Screen")
print()
print(" Please log in")
username = input("Username:")
password = input("Password:")
if username == "mouse" and password == "cheese":
  print ("Welcome online Mr.",username)
elif username == "cat" and password == "toys":
    print ("Welcome online Ms.",username)
else:
    print("You are not Mr.Mouse or Ms. Cat. Leave!")
