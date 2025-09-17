'''
In a file called interpreter.py, implement a program that prompts the user for an arithmetic expression and then calculates and outputs the result as a floating-point value formatted to one decimal place. Assume that the user’s input will be formatted as x y z, with one space between x and y and one space between y and z, wherein:

x is an integer
y is +, -, *, or /
z is an integer

For instance, if the user inputs 1 + 1, your program should output 2.0. Assume that, if y is /, then z will not be 0. '''


## exemplo de input: x y z = resultado

x, y, z = input("Expression:" ).split(" ")

x = float(x)
z = float(z)

##Calculando

if y == "+":
    print(x + z)
elif y == "-":
     print(x - z)
elif y == "/":
    print(x / z)
elif y == "*":
    print(x * z)




