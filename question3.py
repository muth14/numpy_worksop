#write a program to find the factorial of a nummber


number = int(input("Enter a number: "))
result = 1
if number == 0 or number == 1:
    print(f"The factorial of {number} is 1.")
else:
    
    for i in range(2, number + 1):
        result *= i
    print(f"The factorial of {number} is {result}.")
