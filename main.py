import random
from getGuess import getGuess

alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
strikes = 6
num = random.randint(0, 9)
wordlist = ["CANADA", "PIZZA", "GUITAR", "FUTURE", "BACKPACK", "IGNITE", "QUARTER", "PIANO", "LEAGUE", "SANDWICH"]
word = wordlist[num]
wordLength = len(word)
wordArray = list(word)

print("Word has been chosen!")
underscores = ["_" for x in range(wordLength)]
print(" ".join(underscores))

guess = getGuess(alphabet)

while underscores != wordArray:
    if guess not in wordArray:
        strikes -= 1
        if strikes == 0:
            print("Game over! You lose!")
            break
        print(f"Wrong! {strikes} tries left!")
    else:
        positions = []
        for index, letter in enumerate(wordArray):
            if letter == guess:
                positions.append(index)
        for position in positions:
            underscores[position] = guess
        if len(positions) == 1:
            print(f"There is {len(positions)} {guess} in the word.")
        else:
            print(f"There are {len(positions)} {guess}'s in the word.")
    
    print(" ".join(underscores))
    
    if underscores == wordArray:
        break
    
    guess = getGuess(alphabet)

if underscores == wordArray:
    print("Congratulations! You won!")
