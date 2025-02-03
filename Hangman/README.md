# Hangman Game in Python

## 1. Algorithm
1. Display the main menu with options to start or exit.
2. If the player chooses to start, display category selection (Animals or Birds).
3. Randomly select a word from the chosen category.
4. Initialize the game state:
   - Create a masked word with underscores (_).
   - Set attempts left and allowed hints.
   - Maintain a list of missed guesses.
5. Start the game loop:
   - Display the hangman figure and word progress.
   - Accept user input (guess, hint request, restart, or reveal answer).
   - Process input:
     - If correct, update the masked word.
     - If incorrect, update missed guesses and reduce attempts.
     - If hint requested, reveal one missing letter (up to a limit).
     - If restart requested, reset the game.
     - If reveal requested, show the correct word and end the game.
6. Check for game end conditions:
   - If the word is fully guessed, display a win message.
   - If attempts run out, display a loss message with the correct word.
7. Offer replay or return to the main menu.

## 2. Pseudocode
```
START
DISPLAY main menu
WHILE user does not choose exit:
    GET user choice
    IF choice is "Start":
        DISPLAY category menu
        GET category choice
        SELECT random word from chosen category
        INITIALIZE game state
        WHILE game is not over:
            DISPLAY current word state and hangman figure
            GET user input
            PROCESS input:
                IF input is a correct letter:
                    UPDATE displayed word
                ELSE:
                    ADD to missed guesses
                    DECREMENT attempts left
                IF input is hint request:
                    REVEAL one missing letter (if hints available)
                IF input is restart request:
                    RESTART game
                IF input is reveal request:
                    DISPLAY correct word and END game
            CHECK win/loss conditions
            IF word is fully guessed:
                DISPLAY "You win!"
            IF attempts run out:
                DISPLAY "Game over!" with correct word
        RETURN to main menu
END
```

## 3. Requirements
- Python 3.x
- Standard Python libraries: `time`, `random`

## 4. How It Works
The Hangman game allows users to guess letters to complete a word. The word is randomly chosen from a list of animals or birds. Players have a limited number of attempts to guess the correct letters before the game ends. They can also use hints, restart, or reveal the answer. The game uses ASCII art to display the hangman figure.

## 5. Usage
### Running the game:
1. Install Python 3.x if not already installed.
2. Save the script as `hangman.py`.
3. Run the script using:
   ```bash
   python hangman.py
   ```
4. Follow the on-screen instructions to play.

## 6. Complexity Analysis
| Operation            | Best Case  | Average Case  | Worst Case  |
|----------------------|------------|--------------|-------------|
| Word Selection      | O(1)       | O(1)         | O(1)        |
| Guess Processing   | O(1)       | O(n)         | O(n)        |
| Hint Processing    | O(n)       | O(n)         | O(n)        |
| Overall Game Loop  | O(n)       | O(n^2)       | O(n^2)      |

- `n` is the length of the word.
- The game loop runs based on the number of incorrect attempts and valid guesses.
- Worst case occurs when all attempts are used without guessing the word correctly.
