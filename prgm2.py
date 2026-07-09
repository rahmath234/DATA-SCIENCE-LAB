import random
Secret_Number = random.randint(1,10)
guess = 0
print("I'm thinking of a secret number between 1 and 10 can you guess it?")
while guess != Secret_Number:
    guess = int (input ("Enter your guess:"))
    if guess < Secret_Number:
        print ("Too low, try again")
    elif guess > Secret_Number:
        print ("Too high, try again")
    else:
        print("Correct!")