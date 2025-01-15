def getGuess(alphabet):
    guess = input("Guess a letter: ").upper()
    while len(guess) != 1 or guess not in alphabet:
        if len(guess) == 0:
            guess = input("Input cannot be empty. Choose a letter: ").upper()
        elif len(guess) > 1:
            guess = input("Invalid input, choose a single letter: ").upper()
        else:
            guess = input("Invalid letter. Choose a valid letter: ").upper()
    return guess