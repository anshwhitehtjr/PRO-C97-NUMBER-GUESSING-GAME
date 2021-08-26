import random

chances = 5

while chances <= 5 and chances >= -1:
    chances -= 1
    randomNumber = random.randrange(1, 9)
    userInput = int(input("Guess a random number and type it below: \n"))

    if chances == 0:
        print("You ran out of chances\n")
        newUserInput = int(
            input("Please enter the number of chances below: \n"))
        chances = newUserInput

    elif userInput == randomNumber:
        print("You guessed it correctly, Congratulations!!!")

    elif userInput != randomNumber:
        print("No, The Number is", randomNumber)

    else:
        print("Sorry! We had a problem")
