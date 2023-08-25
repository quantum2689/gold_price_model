class Bank:
    def __init__(self, max_deposit_amount):
        self.customers = []
        self.max_deposit_amount = max_deposit_amount

    def open_account(self, name):
        customer = Customer(name)
        self.customers.append(customer)

    def deposit(self, account_name, amount):
        for customer in self.customers:
            if customer.name == account_name:
                if amount <= self.max_deposit_amount:
                    customer.balance += amount
                    break
                else:
                    print("The maximum deposit amount is", self.max_deposit_amount)
                    print("You passed the limits")

    def withdraw(self, account_name, amount):
        for customer in self.customers:
            if customer.name == account_name:
                if customer.balance >= amount:
                    customer.balance -= amount
                    break
                else:
                    print("Insufficient balance")

    def get_balance(self, account_name):
        for customer in self.customers:
            if customer.name == account_name:
                return customer.balance

    def transfer(self, from_account_name, to_account_name, amount):
        self.withdraw(from_account_name, amount)
        self.deposit(to_account_name, amount)


class Customer:
    def __init__(self, name):
        self.name = name
        self.balance = 0


user_name = input("enter your username bankaccount: ")
money = int(input('enter your money:'))
bank = Bank(5000)  # set the maximum deposit amount to 5000
bank.open_account(user_name)
bank.deposit(user_name, money)
print("user", user_name, ',', bank.get_balance(user_name))

