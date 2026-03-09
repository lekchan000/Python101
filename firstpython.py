# In this exercise, you will practice using the built-in print() function in Python.
print('Hello, world!')

# In this exercise, you will practice how to declare a variable, set a value to it, and then print it.
a=7
b=5.5
print(a)
print(b)

# In this exercise, you will practice how to perform simple arithmetic operations on variables and print the output.
a=25 
b=100 
c=a+b
print (c)

# In this exercise, you will practice how to evaluate a variable and criteria to execute code using an If statement.
score=88
if score>90:
    print("Well done! That gets you an A+ grade")
else:
    print("Better luck next time!")

# In this exercise, you will practice how to declare a string array and print the array elements using a For-loop.
mylist= ["John", "Sam", "Adam"] 
for x in mylist: 
    print(x)

# In this exercise, you will practice how to create a break statement in a given for-loop.
mylist2 = ["computer", "monitor", "table"]
for x in mylist2:
  print(x)
  if x == "monitor":
    break
  
# In this exercise, you will practice how to declare a variable and print the variable with a while-loop.
A = 1
while A < 12:
  print(A)
  A += 2

# In this exercise, you will practice how to create a break statement in a given while-loop.
A = 1
while A < 36:
  print(A)
  if A > 20:
    break
  A += 6