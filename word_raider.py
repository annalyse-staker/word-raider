import random
#Colors
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

play_again = True
print("                             WORD RAIDER        ")
print("========================================================================")
wins = 0
games = 0
while play_again:
    word_book = []
    title = "Word Raider"
    with open("words.txt", "r") as file:
        for line in file:
            word_book.append(line.strip().lower())

    random_word = random.choice(word_book)
    misplaced = []
    incorrect = []
    prev_guesses = []

    current_turn = 0
    max_turn = 5
    print("Welcome to ", title, "!")
    print("The word has ", len(random_word), " letters, Goodluck!")

    while current_turn < max_turn:
        print(f"You have {max_turn - current_turn} chances to guess the word before the game will end.")
        guess = input("what is your guess? ").lower()
        remaining_letters = list(random_word)
        colors = [""] * len(guess)
        if len(guess) != len(random_word):
            print("Error, entered word length does not match actual word length")
            continue
        elif not guess.isalpha():
            print("Error, the entered word contains elements that aren't in the alphabet")
            continue

        #Guess is valid, check guessed word against actual word
        else:
            """First Pass: mark all correctly placed letters (green) &
                remove correct letters from remaining available letters"""
            for i, letter in enumerate(guess):
                if letter == random_word[i]:
                    colors[i] = f"{GREEN}{letter}{RESET}"
                    remaining_letters[i] = None

            """Second Pass: check unmatched letters for misplaced (yellow) &
                mark the remaining unused letters (red)"""
            for i, letter in enumerate(guess):
                if colors[i] != "":
                    continue
                if letter in remaining_letters:
                    colors[i] = (f"{YELLOW}{letter}{RESET}")
                    remaining_letters.remove(letter)
                else:
                    colors[i] = (f"{RED}{letter}{RESET}")
                    if letter not in incorrect:
                        incorrect.append(letter)
            hint = "".join(colors)
            prev_guesses.append((guess, hint))
            current_turn += 1
        print(f"Incorrect Letters: {incorrect}")
        for i, (guess, hint) in enumerate(prev_guesses, start=1):
            print(f"Guess {i}. {guess} Hint: {hint}")
        if guess == random_word:
            print(f"{GREEN} Congratulations! {RESET} you've correctly guessed {random_word}!")
            print("The game is now over")
            wins += 1
            games += 1

            break
        if current_turn == max_turn and guess != random_word:
            print("You didn't guess the word correctly, the word is: ", random_word)
            print("Better luck next time!")
            games += 1
    print("=================================")
    print("           Statistics            ")
    print("=================================")
    print("Games played: ", games)
    print("Wins: ", wins)
    print(f"Win Rate: {(wins/games) * 100:.1f}%")
    print("=================================")
    play_again = input("Would you like to play again? ").lower()
    if play_again.lower() in ["yes", "y","continue", "yes please","true"]:
        play_again = True
    else:
        print("Thanks for playing!")
        play_again = False
