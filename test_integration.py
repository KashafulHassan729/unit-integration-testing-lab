import pytest
from bank_app import deposit, withdraw, transfer, calculate_interest

def test_transfer_valid():
    bal_from, bal_to = transfer(500, 200, 100)
    assert bal_from == 400
    assert bal_to == 300

def test_transfer_insufficient():
    with pytest.raises(ValueError):
        transfer(100, 200, 150)

def test_transfer_then_interest():
    bal_from, bal_to = transfer(1000, 500, 200)
    interest = calculate_interest(bal_to, 5, 1)
    assert interest == 700 * 1.05
