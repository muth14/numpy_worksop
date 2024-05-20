# find if the given number is a palindrome or not?

def is_palindrome(number):
    num_str = str(number)
    if num_str == num_str[::-1]:
        return True
    else:
        return False
number = int(input("Enter a number: "))
if is_palindrome(number):
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")
