# We have to see [and] [or] conditions in pythons :
#[and] remember if both the conditions true than output will be true !!! if it's one of condition wrong than it's cames false ----> !!
#[or] remember one of the condition if it's true than its will be came  true conditions -----> !!

#<-----[and]------>
name = "python"
pass1 = "abc123456"
username = input("Enter the username : ")
password = input("Enter your password : ")
if username == name and password == pass1:   
  print("Line A")
  print("Login Successfully")
else:                                          
  print("invalid username and password")
#<-----[and]------>
#<-----[or]------>
name = "python"
pass1 = "abc123456"
username = input("Enter the username : ")
password = input("Enter your password : ")
if username == name or password == pass1:   
  print("Line A")
  print("Login Successfully")
else:                                          
  print("invalid username and password")
#<-----[or]------>
