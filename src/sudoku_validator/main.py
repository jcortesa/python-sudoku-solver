BOARD_SIZE = 2


def is_valid_sudoku(board: list[list[int]]) -> bool:
        """
        Validates if a given Sudoku board is valid, according to Sudoku rules.


        Args:
            board (list[list[int]]): A 2x2 nested list representing the Sudoku board.
                                    Each cell contains integers from 1-4.

        Returns:
            bool: True if the board is valid, False otherwise.

        Raises:
            ValueError: If the board dimensions are not valid (2x2) or contain invalid value types.
        """

        # Check if the board is proper size (2x2)
        check_valid_board_size(board, BOARD_SIZE)

        # Check if all values are integers between 1 and BOARD_SIZE^2
        check_valid_values(board)

        are_unique_row_values: bool = check_unique_values_in_rows(board)

        if not are_unique_row_values:
            return False

        are_unique_column_values: bool = check_unique_values_in_columns(board)

        if not are_unique_column_values:
            return False

        return None

def check_valid_board_size(board: list[list[int]], size: int) -> bool:
    if size != len(board) or any(len(row) != size for row in board):
        raise ValueError("Board must be {}x{}.".format(size, size))
    return True

def check_valid_values(board: list[list[int]]) -> bool:
    valid_values = range(1, (BOARD_SIZE**2)+1)  # For board size of 2x2, valid values are 1, 2, 3, 4

    for row in board:
        for value in row:
            if not isinstance(value, int) or value not in valid_values:
                raise ValueError("Board values must be integers between 1 and {}.".format(BOARD_SIZE**2))
    return True

def check_unique_values_in_rows(board: list[list[int]]) -> bool:
    for row in board:
        seen = set()
        for value in row:
            if value in seen:
                return False
            seen.add(value)
    return True

def check_unique_values_in_columns(board: list[list[int]]) -> bool:
    for col in range(BOARD_SIZE):
        seen = set()
        for row in range(BOARD_SIZE):
            value = board[row][col]
            if value in seen:
                return False
            seen.add(value)
    return True