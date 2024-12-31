# Guess the Number Game

This is a Python-based **Guess the Number** game where the computer randomly selects a number within a user-specified range. The player must guess the number within a limited number of chances. The game provides feedback on whether the guessed number is too low or too high, and calculates the maximum chances based on the range.

## Features
- User-defined range for the random number.
- Maximum chances calculated using binary search logic.
- Feedback for each guess (`LOWER`, `HIGHER`).
- Option to play multiple rounds.

## How to Play
1. The user specifies a lower and upper limit for the range of the random number.
2. The program calculates the maximum number of guesses allowed.
3. The user guesses the number within the specified range.
4. Feedback is provided after each guess:
   - "LOWER" if the guess is less than the number.
   - "HIGHER" if the guess is greater than the number.
5. The game ends when the user guesses the number correctly or runs out of chances.
6. After the game ends, the user can choose to play again or exit.

## Algorithm

1. **User Input**: Get the lower and upper limits from the user.
   - Validate that lower < upper and both are integers.

2. **Generate Random Number**:
   - Use Python's `random.randint()` to generate a random number within the range.

3. **Calculate Chances**:
   - Calculate the maximum chances.
     
4. **Game Loop**:
   - Repeat until the user guesses correctly or runs out of chances:
     - Get the user's guess and validate it.
     - Provide feedback (`LOWER`, `HIGHER`).
     - Track the guesses and decrement chances.

5. **End Game**:
   - Announce the result (win or lose) and reveal the number if the user loses.

6. **Replay**:
   - Ask the user if they want to play again and restart or exit.

## Requirements
- Python 3.x

## Running the Program
1. Save the code in a file named `guess_number.py`.
2. Run the program using the command:
   ```bash
   python guess_number.py
   ```

## Example

### Gameplay Output
```plaintext
Enter lower limit: 1
Enter higher limit: 100

You have 7 chances
Guess a number: 50
You guessed 'LOWER'

You have 6 chances
Guess a number: 75
You guessed 'HIGHER'

You guessed the number 64 right, you WON!
Do you want to play again (Y/N)? N

Thank You for playing
```
