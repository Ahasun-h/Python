select_number  = 10

guess_count = 0
guess_limit = 3


while guess_count < guess_limit :
    guess_number = int(input('Enter your Guess Number :'))
    guess_count += 1
    if guess_number == select_number:
        print("You win !")
        break
else:
    print("Sorry!You lose the game. \n Try aging,Bey")


