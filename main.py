import json
import random
from hangman_stages import hangman_stages


MAX_CHANCES = len(hangman_stages)  # Ensures it matches the imported stages


def display_game_state(dashes, stage_num, chances, guessed_letters):
    """Displays the current state of the game."""
    print("\nHangman Stage:")
    print(hangman_stages[stage_num])
    print(f"You have {chances} chances left.\n")
    print(f"Used letters: {', '.join(guessed_letters).upper()}")
    print(f"Current Word: {' '.join(dashes)}")


def get_valid_letter(guessed_letters):
    """Prompts the user until a valid, unused letter is entered."""
    while True:
        user_input = input("\nGuess a letter: ").lower()

        if not user_input.isalpha() or len(user_input) != 1:
            print("❌ Please enter a single valid letter (A-Z).")
            continue

        if user_input in guessed_letters:
            print("⚠️ You've already guessed that letter. Try another.")
            continue

        return user_input


def hangman(word):
    """Main function to run the Hangman game."""
    dashes = ["_"] * len(word)
    stage_num = 0
    chances = MAX_CHANCES
    guessed_letters = []

    print(f"\n🎮 Guess the {len(word)}-letter word!")

    while chances > 0:
        if "_" not in dashes:
            print("\n🎉 Congratulations! You guessed the word correctly.")
            print(f"The word was: {word.upper()}")
            return

        display_game_state(dashes, stage_num, chances, guessed_letters)
        guess = get_valid_letter(guessed_letters)
        guessed_letters.append(guess)

        if guess in word:
            print("✅ Correct guess!")
            for idx, char in enumerate(word):
                if char == guess:
                    dashes[idx] = guess.upper()
        else:
            print("❌ Wrong guess.")
            chances -= 1
            stage_num += 1

    print("\n💀 You lost! The word was:", word.upper())


if __name__ == '__main__':
    try:
        with open('words.json', 'r') as file:
            data = json.load(file)

        words_list = data['words']
        word = random.choice(words_list).lower()
        hangman(word)

    except FileNotFoundError:
        print("❌ Error: 'words.json' file not found.")
    except json.JSONDecodeError:
        print("❌ Error: Failed to decode JSON from 'words.json'.")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
