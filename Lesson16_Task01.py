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
import datetime


class BankCard:
    """
    This class represents a bank card with various attributes and operations.
    """

    def __init__(self, card_num, cvv, pin, name, surname, end_date):
        self.card_num = card_num
        self.cvv = cvv
        self.pin = pin
        self.name = name
        self.surname = surname
        self.end_date = end_date
        self.is_blocked = False
        self.balance = 0.0

    @classmethod
    def generate_expiry_date(cls):
        """
        Generate an expiry date for the card.
        """
        today = datetime.date.today()
        expiry_date = today.replace(year=today.year + 5)
        return expiry_date

    @staticmethod
    def validate_card_number(card_num):
        """
        Validate the card number.
        """
        return len(card_num) == 16 and card_num.isdigit()

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
            return True
        return False

    def withdraw(self, amount):
        """
        Withdraw money from the card's balance.
        """
        if not self.is_blocked and 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False

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

    def set_pin(self, new_pin):
        """
        Set a new PIN for the card.
        """
        if len(str(new_pin)) == 4:
            self.pin = new_pin
            return True
        return False


if __name__ == "__main__":
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

    if card.validate_card_number(card.card_num):
        print("Card number is valid.")
    else:
        print("Invalid card number.")

    if card.deposit(500):
        print("Deposit successful. New balance:", card.get_balance())
    else:
        print("Deposit failed.")

    if card.withdraw(200):
        print("Withdrawal successful. New balance:", card.get_balance())
    else:
        print("Withdrawal failed.")

    if card.set_pin("9876"):
        print("PIN has been updated.")
    else:
        print("Failed to update PIN.")
