'''
while loops, break, and tracking state
The program picks a secret number between 1 and 100 (use the random module). 
The user guesses repeatedly. After each guess, say "Too high" or "Too low". 
When they get it right, congratulate them, report how many attempts it took, and add a comment on their performance 
(e.g. 5 or fewer = excellent, 8 or fewer = good, otherwise keep practicing).

Example:

I'm thinking of a number between 1 and 100.
Your guess: 50  -> Too high
Your guess: 25  -> Too low
Your guess: 37  -> Correct!
You got it in 3 attempts. Excellent!
'''

import random

# Pick a secret number between 1 and 100
secret_number = random.randint(1, 100)
attempts = 0

print("I'm thinking of a number between 1 and 100.")

while True:
    guess = int(input("Your guess: "))
    attempts += 1

    if guess < secret_number:
        print("Too low")
    elif guess > secret_number:
        print("Too high")
    else:
        print(f"Correct! You got it in {attempts} attempts.")

        # Give performance feedback
        if attempts <= 5:
            print("Excellent!")
        elif attempts <= 8:
            print("Good!")
        else:
            print("Keep practicing!")

        break
