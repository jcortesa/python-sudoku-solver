# 🧩 Python Sudoku Validator

A Sudoku board validator implemented in Python as a technical assignment.

## Objective

Validate whether a 9x9 Sudoku board complies with classic game rules:

- No repeated numbers in any row, column, or 3x3 block.
- Board is a 9x9 matrix of integers (0–9), where `0` means empty.

## Minimum Requirements

- Python 3.10+
- Board validation logic in a class or module.
- Unit tests using `pytest`.

## Technical Requirements

- Clear, maintainable code structure.
- Project documentation and README.
- (Optional) Hexagonal architecture.

## Optional Extras

- CLI to load boards from `.txt` files.
- Hexagonal architecture: domain, use cases, entry points.
- `Makefile` with commands: `run`, `test`, `lint`.
- Code quality tools: `black`, `flake8`, `mypy`, `pytest-cov`.
- Parametrized test suite for valid/invalid boards.

## Setup & Installation

```bash
docker compose up --build
```

## Usage Example
Validate a board from a Python script:

```python
from sudoku_validator import SudokuValidator

board = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    # ... (rest of the 9x9 board)
]

validator = SudokuValidator()
is_valid = validator.is_valid(board)
print("Valid board:", is_valid)
```

Or via CLI (if implemented):

```bash
docker compose run sudoku_validator --board "5,3,0,0,7,0,0,0,0;6,0,0,1,9,5,0,0,0;..."
```

## Run Tests

```bash
docker compose run sudoku_validator pytest
```

## Code Quality & Linting

```bash
make lint
make test
make cov
```

##  Project Structure & Technical Decisions

- Domain logic is separated for testability and clarity.
- Unit tests cover all validation rules.
- (Optional) Hexagonal architecture for maintainability.
- Code formatted with black, linted with flake8, type-checked with mypy.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.