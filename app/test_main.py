import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected",
    [
        (0, [0, 0, 0, 0]),
        (1 , [1, 0, 0, 0]),
        (6 , [1, 1, 0, 0]),
        (17 , [2, 1, 1, 0]),
        (50 , [0, 0, 0, 2]),

    ]
)
def test_get_coin_combination(cents, expected):
    assert get_coin_combination(cents) is expected
    assert isinstance (get_coin_combination(cents), list)
    assert len(expected) == 4


@pytest.mark.parametrize("bad_input",
                         [
                             3.5,
                             "10",
                             None,
                             [1],
                             {"word": 10}
                         ]
                         )
def test_get_coin_combination_errors(bad_input: object):
    with pytest.raises(TypeError):
        get_coin_combination(bad_input)
