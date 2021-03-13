import block
import users
from transactions import transaction
chase = users.User("Chase Leffers")
chase.balance = 1500

class Blockchain: #As coded, this is a Global Ledger
    chain = []

    def __init__(self, chaintype): #chaintypes should actually be subclasses. Will change later.
        self.chain = [block.block(0, "first transaction", 755, "Transaction")]
        self.chaintype = chaintype
        self.length = 1
        self.users = {"Chase Leffers" : chase}
        self.balance = {chase: 1500}
    
    def addBlock(self, transPool, time, blocktype = "Transaction", parallelhashes = 0):
        # Verify transactions here
        # confirm transaction types here
        # Pull actual datatype here
        # Organize transactions if needed
        # Connect to parallel chains(other types) once enough verification time has passed.
        prevhash = self.chain[-1].hash
        self.chain.append(block.block(prevhash, transPool, time, blocktype))
        self.length = self.length + 1
        self.updateBalances(transPool)
    
    def updateBalances(self, transPool):#assume transactions have already been vetted. Only legit ones remain
        for trans in transPool:
            self.balance[trans.user] = self.balance[trans.user] - trans.amount
            trans.user.balance = trans.user.balance - trans.amount
            self.balance[trans.recipient] = self.balance[trans.recipient] + trans.amount
            trans.user.balance = trans.user.balance + trans.amount

    def getBlock(self, index):
        return self.chain[index]

    def balanceSheet(self): #returns a dictionary with the current wealth-distribution of users. Kinda unneeded.
        return {x.print() : self.balance[x] for x in self.balance.keys() }
    
    def addUser(self, userObject):
        self.users[userObject.nickname] = userObject
        self.balance[userObject] = 0
    



        


if __name__ == "__main__":
    transpool = []
    transpool2 = []
    alex = users.User("Alex Anderson")
    maxx = users.User("Maxx Kominowski")
    colin = users.User("Colin Cooper")
    

    transpool.append(transaction(chase, 50, alex))
    transpool.append(transaction(chase, 40, maxx))
    transpool.append(transaction(chase, 1000, colin))
    transpool2.append(transaction(alex, 30, alex))
    transpool2.append(transaction(maxx, 30, chase))
    transpool2.append(transaction(colin, 1000, chase))

    c1 = Blockchain("TestChainType")
    c1.addUser(alex)
    c1.addUser(maxx)
    c1.addUser(colin)

    c1.addBlock(transpool, 914)
    c1.addBlock(transpool2, 942)
    #print(c1.getBlock(2))
    #print(c1.getBlock(1))
    #print(c1.getBlock(0))
    print(c1.balanceSheet())
    print(alex.balance)
    
