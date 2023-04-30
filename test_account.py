from account import *
import pytest

class TestAccount:
    def test_deposit(self):
        acc = account("John Smith")
        assert acc.deposit(100.00) == True
        assert acc.balance() == 100.00

        assert acc.deposit(0) == False
        assert acc.balance() == 100.00

        assert acc.deposit(-100.00) == False
        assert acc.balance() == 100.00

    def test_withdraw(self):
        acc = account("John Smith")
        acc.deposit(100.00)

        assert acc.withdraw(0) == False
        assert acc.balance() == 100.00

        assert acc.withdraw(100000.00) == False
        assert acc.balance() == 100.00

        assert acc.withdraw(100.00) == True
        assert acc.balance() == 0

        assert acc.withdraw(-100.00) == False
        assert acc.balance() == 0

    def test_init(self):
        acc = account("John Smith")
        
        assert acc.get_name() == "John Smith"
        assert acc.balance() == 0


