#Parent Class
class User():
    def __init__(self,name,age,gender):
        self.name = name
        self.age  = age
        self.gender = gender

    def show_details(self):
        print("Personal Details")
        print("")
        print("Name: ", self.name)
        print("Age:  ", self.age)
        print("Gender: ", self.gender)

    
#Child Class
class Bank(User):
    def __init__(self,name,age,gender):
        super().__init__(name,age,gender)
        self.balance = 0

    def deposit(self,amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print("Account balance has been updated : Rs. ", self.balance)

    def withdraw(self,amount):
        self.amount = amount
        if self.amount > self.balance:
            print("Insufficient Funds | Balance Available : Rs. ", self.balance)
        else:
            self.balance = self.balance - self.amount
            print("Account balance has been updated : Rs. ", self.balance)
    
    def view_balance(self):
        self.show_details()
        print("Account balance: Rs. ", self.balance)



if __name__=="__main__":
    print("Welcome to Mini Bank\n")
    name = input("Your Name: ")
    age = input("Your Age: ")
    gender = input("Your Gender: ")
    name = Bank(name,age,gender)
    while(True):
        print("\n1.View Details\n2.Deposite Money\n3.Withdraw Money\n")
        x = int(input("Enter Your Choice: "))
        if(x==1):
            name.show_details()
        elif(x==2):
            sum = int(input("How much do you want to Deposite ?"))
            name.deposit(sum)
        elif(x==3):
            sum = int(input("How much do you want to Withdraw ?"))
            name.withdraw(sum)