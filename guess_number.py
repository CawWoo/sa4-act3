number = 10

print("I'm thinking of a number...")
guess = (input("What number am I thinking of? "))

while guess != number:

    if guess == 'q':
        print(f'The number was {number}...')
        break

    guess = int(guess)
    
    if guess != number:
        guess = (input('Nope! Try again! '))
    else:
        print("Congratulations! You guessed the right number.")
        break

   




