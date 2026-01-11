import pytest
from bank_app import deposit, withdraw, calculate_interest, check_loan_eligibility

def test_deposit_valid():
    assert deposit(100, 50) == 150

def test_deposit_invalid():
    with pytest.raises(ValueError):
        deposit(100, -50)

def test_withdraw_valid():
    assert withdraw(100, 50) == 50

def test_withdraw_insufficient():
    with pytest.raises(ValueError):
        withdraw(100, 150)

def test_calculate_interest_valid():
    assert calculate_interest(1000, 10, 2) == 1000*(1+10/100)**2

def test_calculate_interest_negative_balance():
    with pytest.raises(ValueError):
        calculate_interest(-100, 10, 2)

def test_loan_eligible():
    assert check_loan_eligibility(6000, 720) == True

def test_loan_not_eligible():
    assert check_loan_eligibility(4000, 650) == False
