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

class User:
    def __init__(self, name="", email=""):
        self.name = name
        self.email = email
        self.accounts = {}
        self.accounts['Savings'] = BankAccount(int_rate=0.02, balance=0)
    # instance method to make a deposit to a specified user account
    def make_deposit(self, amount, accountName='Savings'):
        self.accounts[accountName].deposit(amount)
        return self
    # instance method to make a withdrawal from a specified user account
    def make_withdrawal(self, amount, accountName='Savings'):
        self.accounts[accountName].withdraw(amount)
        return self
    # instance method to display the balance of a specified user account
    def display_user_balance(self, accountName='Savings'):
        print("User: " + self.name + ", " + accountName + " Balance: $" + str(self.accounts[accountName].balance))
        return self
    # instance method to transfer money from one user's account to another
    def transfer_money(self, amount, other_user):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)
        return self

# create 2 user accounts
user_1 = User("Dwight", "dschrute@dundermifflin.com")
user_2 = User("Jim", "jhalpert@dundermifflin.com")
# display the initial balances of both user accounts
user_1.display_user_balance()
user_2.display_user_balance()
# deposit $10000 into user 1's account, display the new balance, transfer $4000 into user 2's account, then display user 1's new balance
user_1.make_deposit(10000).display_user_balance().transfer_money(4000,user_2).display_user_balance()
# display user 2's new balance
user_2.display_user_balance()
# create a Checking account for user 1 with an improved interest rate of 0.03
user_1.accounts['Checking'] = BankAccount(int_rate=0.03, balance=0)
# withdraw $5000 from user 1's Savings account and transfer it to their Checking account, display the updated balances
user_1.make_withdrawal(5000,'Savings').make_deposit(5000,'Checking').display_user_balance('Savings').display_user_balance('Checking')
