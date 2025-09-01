import pytest

from sudoku_validator.main import is_valid_sudoku

class TestSudokuValidator:
    @pytest.mark.parametrize("board", [
        pytest.param(
            [
                [1,2],
                [3,4],
                [1,2]
            ],
            id="2x3 invalid size"
        ),
        pytest.param(
            [
                [1,1,1],
                [3,4]
            ],
            id="3x2 invalid size"
        )
    ])
    def test_is_invalid_size(self, board):
        with pytest.raises(ValueError): is_valid_sudoku(board)

    @pytest.mark.parametrize("board", [
        pytest.param(
            [
                ['a', 6, 9, 7, 4, 3, 2, 8, 1],
                [7, 8, 3, 1, 9, 2, 4, 5, 6],
                [1, 2, 4, 6, 5, 8, 7, 9, 3],
                [6, 3, 1, 2, 7, 9, 8, 4, 5],
                [2, 4, 7, 5, 8, 1, 3, 6, 9],
                [8, 9, 5, 3, 6, 4, 1, 2, 7],
                [4, 7, 2, 9, 1, 6, 5, 3, 8],
                [9, 5, 8, 4, 3, 7, 6, 1, 2],
                [3, 1, 6, 8, 2, 5, 9, 7, 4]
            ],
            id="invalid type string"
        ),
        pytest.param(
            [
                [0, 6, 9, 7, 4, 3, 2, 8, 1],
                [7, 8, 3, 1, 9, 2, 4, 5, 6],
                [1, 2, 4, 6, 5, 8, 7, 9, 3],
                [6, 3, 1, 2, 7, 9, 8, 4, 5],
                [2, 4, 7, 5, 8, 1, 3, 6, 9],
                [8, 9, 5, 3, 6, 4, 1, 2, 7],
                [4, 7, 2, 9, 1, 6, 5, 3, 8],
                [9, 5, 8, 4, 3, 7, 6, 1, 2],
                [3, 1, 6, 8, 2, 5, 9, 7, 4]
            ],
            id="invalid value out of range, zero"
        ),
        pytest.param(
            [
                [10, 6, 9, 7, 4, 3, 2, 8, 1],
                [7, 8, 3, 1, 9, 2, 4, 5, 6],
                [1, 2, 4, 6, 5, 8, 7, 9, 3],
                [6, 3, 1, 2, 7, 9, 8, 4, 5],
                [2, 4, 7, 5, 8, 1, 3, 6, 9],
                [8, 9, 5, 3, 6, 4, 1, 2, 7],
                [4, 7, 2, 9, 1, 6, 5, 3, 8],
                [9, 5, 8, 4, 3, 7, 6, 1, 2],
                [3, 1, 6, 8, 2, 5, 9, 7, 4]
            ],
            id="invalid value out of range, ten"
        )
    ])
    def test_is_valid_values(self, board):
        with pytest.raises(ValueError): is_valid_sudoku(board)

    @pytest.mark.parametrize("board, expected", [
        pytest.param(
            [
                [5, 6, 9, 7, 4, 3, 2, 8, 1],
                [7, 8, 3, 1, 9, 2, 4, 5, 6],
                [1, 2, 4, 6, 5, 8, 7, 9, 3],
                [6, 3, 1, 2, 7, 9, 8, 4, 5],
                [2, 4, 7, 5, 8, 1, 3, 6, 9],
                [8, 9, 5, 3, 6, 4, 1, 2, 7],
                [4, 7, 2, 9, 1, 6, 5, 3, 8],
                [9, 5, 8, 4, 3, 7, 6, 1, 2],
                [3, 1, 6, 8, 2, 5, 9, 7, 4]
            ],
            True,
            id="9x9 valid"
        ),
        pytest.param(
            [
                [5, 5, 9, 7, 4, 3, 2, 8, 1],
                [7, 8, 3, 1, 9, 2, 4, 5, 6],
                [1, 2, 4, 6, 5, 8, 7, 9, 3],
                [6, 3, 1, 2, 7, 9, 8, 4, 5],
                [2, 4, 7, 5, 8, 1, 3, 6, 9],
                [8, 9, 5, 3, 6, 4, 1, 2, 7],
                [4, 7, 2, 9, 1, 6, 5, 3, 8],
                [9, 5, 8, 4, 3, 7, 6, 1, 2],
                [3, 1, 6, 8, 2, 5, 9, 7, 4]
            ],
            False,
            id="9x9 invalid, duplicate in row"
        ),
        pytest.param(
            [
                [5, 6, 9, 7, 4, 3, 2, 8, 1],
                [5, 8, 3, 1, 9, 2, 4, 5, 6],
                [1, 2, 4, 6, 5, 8, 7, 9, 3],
                [6, 3, 1, 2, 7, 9, 8, 4, 5],
                [2, 4, 7, 5, 8, 1, 3, 6, 9],
                [8, 9, 5, 3, 6, 4, 1, 2, 7],
                [4, 7, 2, 9, 1, 6, 5, 3, 8],
                [9, 5, 8, 4, 3, 7, 6, 1, 2],
                [3, 1, 6, 8, 2, 5, 9, 7, 4]
            ],
            False,
            id="9x9 invalid, duplicate in column"
        )
    ])
    def test_is_valid_sudoku(self, board, expected):
        assert is_valid_sudoku(board) == expected
