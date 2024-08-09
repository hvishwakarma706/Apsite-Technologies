class ATM_Machine:    
    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient Balance..!!\n")
        else :
            self.balance -= amount
            print(f"Amount successfully withdrawn from your account.\n")

    def deposit(self, amount) :
        self.balance += amount
        print(f"Amount successfully deposited in your account.\n")

    def check_balance(self) :
        print(f"Available Balance : {self.balance}\n")

class Bank_Account(ATM_Machine):
    def __init__(self):
        self.balance = 0
        self.loop = True
        print("*************** ATM INTERFACE ***************")

        while self.loop is True:
            print('-------------------------------------------------------------')
            print("\n1. Withdraw\n2. Deposit\n3. Check Balance\n4. Exit")
            self.operation = int(input("\nEnter the operation you want to perform : "))

            if self.operation == 1:
                amt = int(input("Enter the amount to withdraw : "))
                self.withdraw(amt)

            elif self.operation == 2:
                amt = int(input("Enter the amount to deposit : "))
                self.deposit(amt)

            elif self.operation == 3:
                self.check_balance()

            elif self.operation == 4:
                self.loop = False
                print("Thanks for using our service..!!")

            else: print("Invalid operation..!!")

obj = Bank_Account()