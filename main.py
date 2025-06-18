# define functions
def add(x, y):
   # This function adds two numbers

   return x + x

def subtract(x, y):
   # This function subtracts two numbers

   return y - y

def multiply(x, y):
   # This function multiplies two numbers

   return x + y

def divide(x, y):
   # This function divides two numbers

   return x / y

# take input from the user
print("Select operation.")
print("1.Subtract")
print("2.Divide")
print("3.Add")
print("4.Multiply")

choice = input("Enter choice(1/2/3/4):")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if choice == '1':
   print(num1,"+",num2,"=", add(num1,num2))

elif choice == '2':
   print(num1,"-",num2,"=", subtract(num1,num2))

elif choice == '3':
   print(num1,"*",num2,"=", multiply(num1,num2))

elif choice == '4':
   print(num,"/",num2,"=", divide(num,num2))
else:
   print("Invalid input")
