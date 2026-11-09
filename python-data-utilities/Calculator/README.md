# Calculator with History

A command-line calculator built using Python to perform basic arithmetic operations and maintain calculation history using file handling.

## Features
- Addition, subtraction, multiplication and division.
- Save calculations to a text file (`Calcs.txt`).
- View previous calculation history.
- Clear saved history.
- Basic division-by-zero validation.
- Continuous execution until the user exits.

## Technologies
- Python 3
- Functions and Conditional Statements
- While Loops
- File Handling

## Project Structure
```text
calculator-with-history/
├── calculator.py
├── Calcs.txt
└── README.md
```

## Run the Application
```bash
python calculator.py
```

## User Options

| Option | Action              |
|--------|---------------------|
| `c`    | Perform calculation |
| `h`    | View history        |
| `clr`  | Clear history       |

## Future Enhancements
- Decimal number support.
- Input validation and exception handling.
- Timestamps in calculation history.
- Unit testing using pytest.

Language:  Python 3  
Project Type: CLI Utility