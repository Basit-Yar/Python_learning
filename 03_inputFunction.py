# input() --> is used to take input from user, 
# or we can say it is used to read a line from the user's input
# ================================================================

name = input("Enter your name : ")
print("\nGood Morning Mr. " + name)
print("=====================================")
age = input("Enter your age : ")
print(name + " is " + age + " old.")
print(type(age))
age = int(age)
print(type(age))