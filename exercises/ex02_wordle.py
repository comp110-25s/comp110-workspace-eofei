"""Program to help create a wordle game."""

__author__: str = "730574267"


def contains_char(word: str, letter: str) -> bool:
    """Check if word contains certain letter."""
    assert len(letter) == 1, f"len('{letter}') is not 1"
    x = 0
    while x < len(word):
        """Checks each index to see which letters match up."""
        if word[x] == letter:
            return True
        x = x + 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Represent letters as emojis."""
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    string: str = ""
    assert len(guess) == len(secret), "Guess must be same length as secret"
    """Checks the length of the guess."""
    x = 0
    while x < len(guess):
        """Emojifies the guessed word."""
        if guess[x] == secret[x]:
            string += GREEN_BOX
        elif contains_char(secret, guess[x]) is True:
            string += YELLOW_BOX
        else:
            string += WHITE_BOX
        x = x + 1
    return string


def input_guess(expected_length: int) -> str:
    guess: str = input(f"Enter a {expected_length} character word:")
    """Stores the guessed word."""
    while len(guess) != expected_length:
        guess = input(f"That wasn't {expected_length} chars! Try again: ")
        """Prompts the user to guess again."""
    return guess


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turns = 1
    max_turns = 6

    while turns <= max_turns:
        """Keeps track of turns."""
        print(f"=== Turn {turns}/{max_turns} ===")
        guess = input_guess(len(secret))
        print(emojified(guess, secret))

        if guess == secret:
            print(f"You won in {turns}/{max_turns} turns!")
            return None
        else:
            turns += 1
    print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="heart")
