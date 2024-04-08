import random

# List of words to guess
words = ['programming', 'debugger', 'software', 'algorithm', 'python', 'variable']

# Randomly choose a word from the list
chosen_word = random.choice(words)
word_display = ['_' for _ in chosen_word]  # Create a list of underscores
attempts = 5  # Number of allowed attempts

print("Welcome to Hangman!")
print(f"You have {attempts} attempts to guess the word.")

while attempts > 0 and '_' in word_display:
    print("\n" + ' '.join(word_display))
    guess = input("Guess a letter: ").lower()

    # Check if the guessed letter is in the chosen word
    if guess in chosen_word:
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                word_display[index] = guess  # Reveal the letter
    else:
        attempts -= 1
        print("Incorrect guess. You have", attempts, "attempts remaining.")

# Game conclusion
if '_' not in word_display:
    print("You guessed the word!")
    print(' '.join(word_display))
    print("You survived!")
else:
    print("Sorry! You ran out of attempts. The word was: " + chosen_word)
    print("You lost!")