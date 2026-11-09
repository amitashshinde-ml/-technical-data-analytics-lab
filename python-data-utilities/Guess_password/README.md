# 🔐 Password Guessing Game (Python)

A simple command-line Python game where users try to guess a randomly selected password based on three difficulty levels: Easy, Medium, and Hard.

## Features

- **Three difficulty levels:** Easy, Medium, and Hard.
- **Random password selection** using Python's `random` module.
- **Limited attempts:** Maximum of 3 guesses per password.
- **Character matching:** Displays correctly guessed characters in their respective positions.
- **Duplicate character handling:** Prevents the same password character from being matched more than once.
- **Replay option:** Allows users to guess another password.

## How to Run

1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```

2. Navigate to the project directory:
   ```bash
   cd password-guessing-game
   ```

3. Run the Python program:
   ```bash
   python main.py
   ```

## How to Play

1. Select a difficulty level: Easy, Medium, or Hard.
2. Enter your password guess.
3. Correctly guessed characters are revealed in their matching positions.
4. You have a maximum of 3 attempts.
5. Choose whether to retry or start a new game.

## Python Concepts Used

- Variables and data types
- Lists and list manipulation
- Conditional statements (`if/elif/else`)
- Loops (`while` and `for`)
- Functions and return values
- Random selection (`random.choice()`)
- String and list operations
- List copying and duplicate character handling

## Future Improvements

- Hide the password instead of displaying it before guessing.
- Add input validation and improved error handling.
- Introduce a scoring system.
- Store game history and statistics.

---

**Project Type:** Beginner Python CLI Project  
**Language:** Python 3  
**External Dependencies:** None (uses Python standard library)