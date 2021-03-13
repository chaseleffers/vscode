

class User:

    def __init__(self, nickname, publicKey = 0, privateKey = 0):
        self.nickname = nickname
        self.publicKey = publicKey
        self.privateKey = privateKey
        self.balance = 0
        self.tribe = [] # All the other users you trust enough to believe.
    
    def print(self):
        return self.nickname
    
    #method to sign a transaction here
