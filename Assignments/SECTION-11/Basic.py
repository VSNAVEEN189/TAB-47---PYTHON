'''Comprehension Basics

Turning loops into list comprehensions
Using list comprehensions over the numbers 1 to 50, build:
• a list of their squares
• a list of only the even numbers
• a list of (number, "prime" / "not prime") tuples'''


def is_prime(number):
    if number < 2:
        return False
    for divisor in range(2, number):
        if number % divisor == 0:
            return False
    return True


squares = [number ** 2 for number in range(1, 51)]

even_numbers = [
    number for number in range(1, 51)
    if number % 2 == 0
]
prime_status = [
    (number, "prime" if is_prime(number) else "not prime")
    for number in range(1, 51)
]


print("====The square from 1 to 50 is====")
print(squares)
print("====The even numbers from 1 to 50 is====")
print(even_numbers)
print("====The list of prime numbers 1 to 50 is====")
print(prime_status)