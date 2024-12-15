import random

#playWhe simulator

def winOrLose(isTrue):
    if isTrue:
        print("You Won!")
    print("You Lost :(")

def betSimulator(playerGuess)->bool:
    guess = random.randint(0, 36)
    print("Number: " + str(guess))
    if playerGuess == guess:
        return True


def play():
    while True:
        playerGuess = input("Guess a number: ")
        if playerGuess.isdigit()==False:
            break
        winOrLose(betSimulator(playerGuess))


#play() Works
def guessOpposite()->int:
    '''this function is bullshit, so don't actually use to predict numbers
    it operates on the concept of you are always guessing wrong,
    therefore since its 36 numbers that can be guessed, it will guess 35 of those numbers without replacement
    the remaining number is the prediction!'''
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
    alreadyGuessed = []
    while len(alreadyGuessed)<35:
        computerGuess = random.randint(1, 36)
        if computerGuess not in alreadyGuessed:
            alreadyGuessed.append(computerGuess)
    setN = set(numbers)
    setA = set(alreadyGuessed)
    inNumbers = setN-setA
    inNumbers = list(inNumbers)
    number = inNumbers[0]
    return number


num = guessOpposite()
print(num)