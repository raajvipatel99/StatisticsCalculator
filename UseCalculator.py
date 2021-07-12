from calculator import Calculator

c = Calculator()

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Square")
print("6.Square Root")

choice = input("Enter your choice: ")
if choice in ('1', '2', '3', '4'):
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
elif choice in ('5', '6'):
    num1 = float(input("Enter a number: "))

if choice == '1':
    print(num1, "+", num2, "=", c.add(num1, num2))

elif choice == '2':
    print(num1, "-", num2, "=", c.subtract(num1, num2))

elif choice == '3':
    print(num1, "*", num2, "=", c.multiply(num1, num2))

elif choice == '4':
    print(num1, "/", num2, "=", c.divide(num1, num2))

elif choice == '5':
    print("Square of ", num1, "=", c.square(num1))

elif choice == '6':
    print("Square Root of", num1, " = ", c.squareroot(num1))