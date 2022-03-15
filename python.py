class User:
    
    def __init__(self, name):
        self.name = name
        self.amount = 0
        
    def make_deposit(self, amount):
        self.amount += amount
        
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.amount}")
        
    def make_withdrawal(self, amount):
        self.amount -= amount
        

josh = User("Josh")
kyle = User("Kyle")
jeremy = User("Jeremy")

josh.make_deposit(100)
josh.make_deposit(200)
josh.make_deposit(50)
josh.make_withdrawal(45)
josh.display_user_balance()
kyle.make_deposit(100)
kyle.make_deposit(200)
kyle.make_deposit(50)
kyle.make_withdrawal(45)
kyle.make_withdrawal(110)
kyle.display_user_balance()
jeremy.make_deposit(100)
jeremy.make_withdrawal(20)
jeremy.make_withdrawal(50)
jeremy.make_withdrawal(45)
jeremy.display_user_balance()