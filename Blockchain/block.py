import hashers


class block:

    def __init__(self, prevhash, transPool, time, blocktype): #transPool is a bunch of Transactions.
        #self.hash = hash #Not needed?
        self.prevhash = prevhash
        self.transPool = transPool
        self.time = time
        self.blocktype = blocktype
        self.hash = self.hashblock()

    def toHashString(self):
        return str(self.prevhash) + str(self.transPool) + str(self.time) + str(self.blocktype)
    
    def hashblock(self):
        return hashers.hash(self.toHashString())
    
    def __str__(self):
        return str(self.prevhash) + str(self.transPool) + str(self.time) + str(self.blocktype) + str(self.hash)


if __name__ == "__main__":

    b1 = block(0, "first transaction", 755, "Transaction")
    b2 = block(0, "first transaction", 755, "Transaction")
    b3 = block(0, "second transaction", 800, "PageView")
    if b1.hashblock() == b2.hashblock() != b3.hashblock():
        print("success!")
