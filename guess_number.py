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
        if guess < number:
            guess = (input('Too low. Try again: '))
        elif guess > number: 
            guess = (input('Too high. Try again: '))        
        tries -= 1
        print(f'You have {tries} guesses left')

    elif guess == number:
        print("Congratulations! You guessed the right number.")

if tries == 0:  
    print(f'Sorry, you ran out of tries. The number was {number}')


    


   




