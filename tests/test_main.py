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

    @pytest.mark.parametrize("board, expected", [
        pytest.param(
            [
                [1,2],
                [3,4]
            ],
            True,
            id="2x2 valid"
        ),
        pytest.param(
            [
                [1,1],
                [3,4]
            ],
            False,
            id="2x2 invalid"
        )
    ])
    def test_is_valid_sudoku(self, board, expected):
        assert is_valid_sudoku(board) == expected
