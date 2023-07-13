print("Hello, You Are Wellcome To My Game!")

playing = input("Do you want to play? ")

if playing != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("what is Ug in full? ")
if answer == "Uganda":
    print("correct!")
    score += 1
else:
    print("incorrect!")

answer = input("How many Sub Counties are in Uganda? ")
if answer == "1488":
    print("correct!")
    score += 1
else:
    print("incorrect!")

answer = input("How nany Counties are in Uganda? ")
if answer == "322":
    print("correct!")
    score += 1
else:
    print("incorrect!")

answer = input("How many Districts are in Uganda? ")
if answer == "146":
    print("correct!")
    score += 1
else:
    print("incorrect!")

answer = input("How many Municipalities are in Uganda? ")
if answer == "39":
    print("correct!")
    score += 1
else:
    print("incorrect!")

answer = input("How many Cities are in Uganda? ")
if answer == "15":
    print("correct!")
    score += 1
else:
    print("incorrect!")

answer = input("What is the biggest and Capital City in Uganda? ")
if answer == "Kampala":
    print("correct!")
    score += 1
else:
    print("incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 7) * 100) + "%.")
