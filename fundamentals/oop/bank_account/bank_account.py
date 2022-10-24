class BankAccount:
    # list to contain all instances of BankAccount's info
    all_accounts = []
    
    def __init__(self, int_rate = 0.00, balance = 0):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)
    # instance method to increase balance of account by deposit amount
    def deposit(self, amount):
        self.balance += amount
        return self
    # instance method to decrease balance of account by withdrawal amount
    def withdraw(self, amount):
        # deduct $5 overdraft fee from account on attempts to withdraw more money than is available
        if(amount > self.balance):
            print("Insufficient funds: charging a $5 fee")
            self.balance -= 5
        else:
            self.balance -= amount
        return self
    # instance method to display balance of account
    def display_account_info(self):
        print("Balance: $" + str("%.2f" % self.balance))
        return self
    # instance method to yield interest and add to account balance
    def yield_interest(self):
        if(self.balance > 0):
            self.balance += self.balance * self.int_rate
        return self
    # class method to get balances of all accounts
    @classmethod
    def all_balances(cls):
        for account in cls.all_accounts:
            account.display_account_info()

account_1 = BankAccount(0.07,5000)
account_2 = BankAccount(1.40,4200)

account_1.deposit(1500).deposit(770).deposit(90).withdraw(2000).yield_interest().display_account_info()
account_2.deposit(150).deposit(650).withdraw(1000).withdraw(2000).withdraw(1500).withdraw(600).yield_interest().display_account_info()

BankAccount.all_balances()
