import random
import enchant
import os

D = enchant.Dict("en_US")

WORDS = (
    "treehouse",
    "python",
    "learner"
)

def promt_for_words(player,challenge):
    guesses = set()
    print("{} turn:".format(player))
    print("What words can you find in the word '{}'".format(challenge.upper()))
    print("(Enter 'Q' to quit)")
    while True:
        guess = input("{} words   > ".format(len(guesses)))
        if guess.upper() == 'Q':
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        for letter in guess:
            if letter not in challenge:
                print("That letter isn't in the word! Try again..")
                continue
            else:
                if D.check(guess.lower()) and len(guess) >= 2:
                    guesses.add(guess.lower())
                else:
                    print("That is not a valid word! Try again..")
    return guesses

def output_results(results):
    index = 1
    for word in results:
        print("{}. {}".format(index + 1, word))
        index += 1

challenge_word = random.choice(WORDS)
player1_words = promt_for_words("Player 1", challenge_word)
player2_words = promt_for_words("Player 2", challenge_word)

player1_unique = player1_words - player2_words
player2_unique = player2_words - player1_words

shared_guesses = player1_words & player2_words

print("\nPlayer 1 Results:")
print("{} guesses \n{} were unique".format(len(player1_words), len(player1_unique)))
print("\n---------------")
print("\nPlayer 2 Results")
print("{} guesses \n{} were unique".format(len(player2_words), len(player2_unique)))
print("\n---------------")
print("\nShared Guesses:")
print(output_results(shared_guesses))
