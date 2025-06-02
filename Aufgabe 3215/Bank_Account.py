from Class_Account import BankAccount, account01, account02

print()

print(account01)
account01.deposit(200)
account01.interest_rate(1.8)
account01.withdraw(50)
account01.account_balance()

print()

print(account02)
account02.deposit(500)
account02.interest_rate(1.8)
account02.withdraw(100)
account02.account_balance()

print()

account01.withdraw(500)

print()

account02.withdraw(1000)
