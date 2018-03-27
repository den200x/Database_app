#OOP practice
class Account:   #classs or prototype

    def __init__(self, filepath):
        self.filepath = filepath         #instance variable
        with open(filepath, 'r') as file:
            self.balance=int(file.read())

    def withdraw(self, amount):
        self.balance = self.balance - amount

    def deposit(self, amount):
        self.balance = self.balance + amount

    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))


class Checking(Account):
    '''This class generates checking account objects'''
    type = "checking" #Class Variable,data memeber

    def __init__(self,filepath,fee): #construtor 
        Account.__init__(self,filepath) #inheritance
        self.fee = fee

    def transfer(self,amount): # class method
        self.balance = self.balance - amount - self.fee

checking = Checking("ba_OOP//balance.txt",1) #a object instance
checking.deposit(110)
checking.transfer(100)
print(checking.balance)
checking.commit()    

gil_checking = Checking("ba_OOP//gil.txt",1) #a object instance
gil_checking.deposit(110)
gil_checking.transfer(100)
print(gil_checking.balance)
gil_checking.commit() 

john_checking = Checking("ba_OOP//john.txt",1) #a object instance,instantiation
john_checking.deposit(110)
john_checking.transfer(100)
print(john_checking.balance)
john_checking.commit() 
#account = Account("ba_OOP//balance.txt")    
#print(account.balance)    
#account.withdraw(100)
#print(account.balance)  
#account.commit()