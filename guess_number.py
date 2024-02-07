number = 10
tries = 5

print("I'm thinking of a number...")
guess = (input("What number am I thinking of? "))
tries -= 1
print(f'You have {tries} guesses left')

while guess != number and tries != 0:

    if guess == 'q':
        print(f'The number was {number}...')
        break

    guess = int(guess)
    
    if guess != number:
        guess = (input('Nope! Try again! '))
        tries -= 1
        print(f'You have {tries} guesses left')

    if guess == number:
        print("Congratulations! You guessed the right number.")

print(f'Sorry, you ran out of tries. The number was {number}')


    


   




