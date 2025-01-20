"""
Create a Simple Bank Account Class
mandatory
Score: 0.0% (Checks completed: 0.0%)
Objective: Understand the fundamentals of OOP in Python by implementing a BankAccount class that encapsulates banking operations. Use command line arguments to interact with instances of this class.

Task Description:
You will create two Python scripts: bank_account.py, which contains the BankAccount class, and main-0.py, which interfaces with the class through command line arguments to perform banking operations.

bank_account.py:
Class Definition:

Define a class named BankAccount.
Use the __init__ method to initialize an account_balance attribute. Optionally, accept an initial balance parameter, defaulting to zero.
Encapsulation and Behaviors:

Implement deposit(amount), withdraw(amount), and display_balance() methods.
deposit should add the specified amount to account_balance.
withdraw should deduct the amount from account_balance if funds are sufficient, returning True; otherwise, return False and do not alter the balance.
display_balance should print the current balance in a user-friendly format.

Implementation Notes for you:
Ensure your BankAccount class in bank_account.py correctly implements the specified functionalities and adheres to the principles of encapsulation.
Use main.py to test your BankAccount class by performing various operations. Adjust the initial balance as needed for testing different scenarios.
This task combines learning OOP concepts with practical command line interaction, enhancing your understanding of Python programming.


"""


# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0):
        """
        Initialize a BankAccount instance with an optional initial balance.
        :param initial_balance: Starting balance of the account (default is 0).
        """
        self.__account_balance = initial_balance

    def deposit(self, amount):
        """
        Deposit the specified amount into the account.
        :param amount: The amount to be added to the account balance.
        """
        if amount > 0:
            self.__account_balance += amount

    def withdraw(self, amount):
        """
        Withdraw the specified amount from the account, if sufficient funds exist.
        :param amount: The amount to be deducted from the account balance.
        :return: True if the withdrawal was successful, False otherwise.
        """
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        return False

    def display_balance(self):
        """
        Display the current account balance in a user-friendly format.
        """
        print(f"Current Balance: ${self.__account_balance:.2f}")