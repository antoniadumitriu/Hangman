import random

# List of predefined words and categories
words = {
    "Animals": ["elephant", "giraffe", "tiger", "penguin", "dolphin"],
    "Fruits": ["banana", "strawberry", "watermelon", "kiwi", "pineapple"],
    "Cities": ["paris", "newyork", "tokyo", "london", "dubai"]
}

# Function to select a random word from a specified category
def select_random_word(category):
    if category not in words:
        return None
    return random.choice(words[category])

# Function to initialize the game
def initialize_game():
    print("Welcome to Hangman!")
    name = input("Enter your name: ")
    print("Select a category:")
    for category in words:
        print(category)
    category = input("Category: ").title()

    word = select_random_word(category)
    if word is None:
        print("Invalid category. Please choose from the list.")
        return None, None, None

    word_length = len(word)
    display_word = ["_"] * word_length
    attempts = 6  # Number of incorrect guesses allowed
    guessed_letters = []
    score = 0

    return name, word, display_word, attempts, guessed_letters, score

# Function to display the current state of the word
def display_current_word(display_word):
    return " ".join(display_word)

# Function to play the game
def play_hangman():
    name, word, display_word, attempts, guessed_letters, score = initialize_game()

    if word is None:
        return

    print("Welcome,", name)
    print(display_current_word(display_word))

    while attempts > 0:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    display_word[i] = guess
            print("Correct guess!")
            print(display_current_word(display_word))
            score += 10
        else:
            attempts -= 1
            print("Incorrect guess. Attempts remaining:", attempts)
            print(display_current_word(display_word))

        if "_" not in display_word:
            print("Congratulations, you've guessed the word:", word)
            print("Your score:", score)
            break

    if "_" in display_word:
        print("You ran out of attempts. The word was:", word)
        print("Your score:", score)

if __name__ == "__main__":
    play_hangman()
