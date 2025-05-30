class BankAccount:
    def __init__(self, accountuser, overdraft=-100.0):
        self.accountuser = accountuser
        self.balance = 0.0
        self.overdraft = overdraft

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount:.2f} € wurden eingezahlt.")
        else:
            print("Betrag muss positiv sein.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Betrag muss positiv sein.")
            return

        if self.balance - amount >= self.overdraft:
            self.balance -= amount
            print(f"{amount:.2f} € wurden abgehoben.")
        else:
            print("Abhebung nicht möglich: Überziehungslimit überschritten.")

    def account_balance(self):
        print(f"Aktueller Kontostand: {self.balance:.2f} €")

    def interest_rate(self, interest_rate):
        if self.balance > 0:
            intrate = self.balance * (interest_rate / 100)
            self.balance += intrate
            print(f"Zinsen in Höhe von {intrate:.2f} € wurden gutgeschrieben.")
        else:
            print("Keine Zinsen berechnet, da der Kontostand nicht positiv ist.")

    def __str__(self):
        return f"Konto von {self.accountuser}\nKontostand: {self.balance:.2f} €, Überziehungslimit: {self.overdraft:.2f} €"

account01 = BankAccount("Rainer Zufall")

account02 = BankAccount("Andi Bar")

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
