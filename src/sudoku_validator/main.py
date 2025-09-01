BOARD_SIZE = 2


def is_valid_sudoku(board: list[list[int]]) -> bool:
        """
        Validates if a given Sudoku board is valid, according to Sudoku rules.


        Args:
            board (list[list[int]]): A 2x2 nested list representing the Sudoku board.
                                    Each cell contains integers from 0-4, where 0 represents an empty cell.

        Returns:
            bool: True if the board is valid, False otherwise.

        Raises:
            ValueError: If the board dimensions are not valid (2x2) or contain invalid value types.
        """

        # Check if the board is proper size (2x2)
        check_valid_board_size(board, BOARD_SIZE)

        return None

def check_valid_board_size(board: list[list[int]], size: int) -> bool:
    if size != len(board) or any(len(row) != size for row in board):
        raise ValueError("Board must be {}x{}.".format(size, size))
    return True