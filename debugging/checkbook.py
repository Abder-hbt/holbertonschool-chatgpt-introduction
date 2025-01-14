#!/usr/bin/python3

class Checkbook:
    """
    A class representing a checkbook with basic operations like deposit, withdrawal, and balance checking.

    Methods:
        deposit(amount): Deposits a specified amount to the balance.
        withdraw(amount): Withdraws a specified amount from the balance.
        get_balance(): Displays the current balance.
    """
    
    def __init__(self):
        """
        Initializes a new Checkbook instance with a balance of 0.0.
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Deposits the given amount into the checkbook.

        Parameters:
            amount (float): The amount to deposit into the checkbook.

        Returns:
            None
        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Withdraws the given amount from the checkbook if sufficient funds are available.

        Parameters:
            amount (float): The amount to withdraw from the checkbook.

        Returns:
            None
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Displays the current balance in the checkbook.

        Returns:
            None
        """
        print("Current Balance: ${:.2f}".format(self.balance))

def main():
    """
    Main function to run the checkbook program. Allows the user to deposit, withdraw, or check the balance.

    It handles invalid input gracefully and ensures the user provides valid numeric input.
    """
    cb = Checkbook()

    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ")
        if action.lower() == 'exit':
            break
        elif action.lower() == 'deposit':
            try:
                amount = float(input("Enter the amount to deposit: $"))
                if amount < 0:
                    print("Amount must be positive. Please try again.")
                else:
                    cb.deposit(amount)
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        elif action.lower() == 'withdraw':
            try:
                amount = float(input("Enter the amount to withdraw: $"))
                if amount < 0:
                    print("Amount must be positive. Please try again.")
                else:
                    cb.withdraw(amount)
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        elif action.lower() == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
