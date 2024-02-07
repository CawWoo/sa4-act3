number = 10

print("I'm thinking of a number...")
guess = (input("What number am I thinking of? "))

while guess != number:

    if guess == 'q':
        print(f'The number was {number}...')
        break

    guess = int(guess)
    
    if guess < number:
        guess = (input('Too low. Try again: '))
    elif guess > number: 
        guess = (input('Too high. Try again: '))
    else:
        print("Congratulations! You guessed the right number.")
        break

   




