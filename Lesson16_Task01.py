"""
Home-task 13 Class writing Practice

# write class for bank card.
# Class should reflect card lifecycle, card operations etc.
# use CVV, PIN, Name, Surname , end date, card_num as initial params
# class should have in addition to common logic some class attributes, as minimum one classmethod and
# as minimum  one staticmethod, two or more getters/setters
# do not forget about block '''if __name__ == '__main__':'''
"""

import datetime


class BankCard:
    """
    This class represents a bank card with various attributes and operations.
    """
    PIN_SIZE = 4  # Example of a class attribute

    def __init__(self, card_num, cvv, pin, name, surname, end_date):
        self.card_num = card_num
        self._cvv = cvv  # Protected attribute
        self._pin = pin  # Protected attribute
        self.name = name
        self.surname = surname
        self.end_date = end_date
        self.is_blocked = False
        self.balance = 0.0

    @staticmethod
    def generate_expiry_date():
        """
        Generate an expiry date for the card.
        """
        today = datetime.date.today()
        expiry_date = today.replace(year=today.year + 5)
        return expiry_date

    @property
    def cvv(self):
        return self._cvv

    @cvv.setter
    def cvv(self, new_cvv):
        self._cvv = new_cvv

    @property
    def pin(self):
        return self._pin

    @pin.setter
    def pin(self, new_pin):
        if len(str(new_pin)) == self.PIN_SIZE:
            self._pin = new_pin
        else:
            raise ValueError("PIN must be 4 digits")

    def block_card(self):
        """
        Block the card.
        """
        self.is_blocked = True

    def deposit(self, amount):
        """
        Deposit money into the card's balance.
        """
        if not self.is_blocked and amount > 0:
            self.balance += amount
        else:
            raise BaseException("Deposit failed")

    def withdraw(self, amount):
        """
        Withdraw money from the card's balance.
        """
        if not self.is_blocked and 0 < amount <= self.balance:
            self.balance -= amount
        else:
            raise BaseException("Withdrawal failed")

    # Getters and Setters
    def get_balance(self):
        """
        Get the current balance of the card.
        """
        return self.balance

    def get_full_name(self):
        """
        Get the full name of the card holder.
        """
        return f"{self.name} {self.surname}"


if __name__ == "__main__":
    try:
        card_num = "1234567890123456"
        cvv = "123"
        pin = "4321"
        name = "John"
        surname = "Doe"
        end_date = BankCard.generate_expiry_date()

        card = BankCard(card_num, cvv, pin, name, surname, end_date)

        print(f"Card Holder: {card.get_full_name()}")
        print(f"Card Number: {card.card_num}")
        print(f"Expiry Date: {card.end_date}")
        print(f"Current Balance: ${card.get_balance()}")

        card.deposit(500)
        print("Deposit successful. New balance:", card.get_balance())

        card.withdraw(200)
        print("Withdrawal successful. New balance:", card.get_balance())

        card.pin = "9876"
        print("PIN has been updated.")

    except BaseException as e:
        print(f"An error occurred: {e}")
