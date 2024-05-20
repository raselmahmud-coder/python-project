# 1. Write a program that swaps the values of two variables.
user_1 = "Rasel"
user_2 = "Mahmud"
user_1, user_2 = user_2, user_1
# print("swap value: ", user_1, user_2)


# 2. Write a program that calculates the area of a rectangle given its length and width.
length = 23
width = 10
area = length * width
# print("Area is:", area)


# 3. Write a program that converts temperature from Fahrenheit to Celsius.
fahrenheit = 122
celsius = ((fahrenheit - 32) * 5/9)
# print("Celsius is:", celsius)


# 4. Write a program that calculates the volume of a sphere given its radius.
radius = 3
pi = 3.1416
volume = (4/3)*pi*pow(radius, 3)
# print("Volume of:", volume)


# 5. Write a program that finds the average of three numbers.
def find_avg(user_age1, user_age2, user_age3):

    avg = (user_age1 + user_age2 + user_age3) / 3
    return avg

# print("Average Age Is:", find_avg(22, 25, 29))


# 6. Write a program that determines if a number is even or odd.
num = 7
if num % 2 == 0:
    print("Even")
else:
    print("Odd")


# 7. Write a program that finds the maximum of three numbers.
def max_of_three(a, b, c):
    return max(a, b, c)


# print("Maximum of 5, 10, and 3 is:", max_of_three(5, 10, 3))


# 8. Write a program that determines if a year is a leap year or not.
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(year, "is a leap year")
    else:
        print(year, "is not a leap year")


# is_leap_year(2024)


# 9. Write a program that determines if a number is positive, negative, or zero.
def check_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"


# Example usage:
number = -7
# print(number, "is", check_number(number))


# 10. Write a program that calculates the grade based on a given percentage.
def calculate_grade(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    else:
        return "F"


percentage = 85
# print("Grade for", percentage, "% is:", calculate_grade(percentage))


# 11. Write a program that prints the first `n` natural numbers.
def print_natural_numbers(n):
    for i in range(1, n + 1):
        print(i, end=" ")


n = 10
# print_natural_numbers(n)


# 12. Write a program that calculates the factorial of a number.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


number = 5
# print("Factorial of", number, "is:", factorial(number))


# 13. Write a program that generates a Fibonacci sequence of length `n`.
def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence


length = 10
# print("Fibonacci sequence of length", length, "is:", fibonacci(length))


# 14. Write a program that checks if a given number is prime or not.
def is_prime(num):
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True


number = 17
""" if is_prime(number):
    print(number, "is prime")
else:
    print(number, "is not prime") """


# 15. Write a program that prints the multiplication table of a given number.
def multiplication_table(number):
    for i in range(1, 11):
        print(number, "x", i, "=", number * i)


num = 7
multiplication_table(num)


# 16. Write a program that finds the sum of all even numbers between 1 and `n`.
def sum_of_evens(n):
    total = 0
    for i in range(2, n + 1, 2):
        total += i
    return total


n = 10
# print("Sum of even numbers between 1 and", n, "is:", sum_of_evens(n))


# 17. Write a program that reverses a given number.
def reverse_number(number):
    reversed_num = 0
    while number > 0:
        remainder = number % 10
        reversed_num = reversed_num * 10 + remainder
        number = number // 10
    return reversed_num


# Example usage:
num = 12345
print("Reverse of", num, "is:", reverse_number(num))


# 18. Write a program that checks if a given string, is a palindrome.
def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]

# Example usage:
string = "Madam"
if is_palindrome(string):
    print(string, "is a palindrome")
else:
    print(string, "is not a palindrome")


# 19. Write a program that generates a random number and allows the user to guess it.
import random

def guess_number():
    target = random.randint(1, 100)
    guess = None
    while guess != target:
        guess = int(input("Guess the number (between 1 and 100): "))
        if guess < target:
            print("Too low, try again!")
        elif guess > target:
            print("Too high, try again!")
    print("Congratulations! You guessed it.")

# Example usage:
guess_number()




# 20. Write a program that finds the greatest common divisor (GCD) of two numbers.
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Example usage:
num1 = 36
num2 = 48
print("GCD of", num1, "and", num2, "is:", gcd(num1, num2))
