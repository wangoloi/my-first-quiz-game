screte_number = 9
guess_count = 0
guess_limit = 3
while guess_count <= guess_limit:
    guess_count = int(input("Guess the number: "))
    if guess_count == 9:
        print("You won!")
        break
else:
    print("You failed!")
