#write a program to find the sum of digits of a given number'

number = input("Enter a number: ")
digit_sum = 0
for digit in number:
    digit_sum += int(digit)
print(f"The sum of the digits of {number} is {digit_sum}.")
