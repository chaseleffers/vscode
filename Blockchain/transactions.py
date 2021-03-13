

class transaction:

    def __init__(self, user, amount, recipient, time = 0, transType = "Transaction"):
        self.user = user #This is the person sending the transaction
        self.amount = amount #This is how much $$ is being sent
        self.time = time #when the transaction was sent.
        self.type = transType # complex data type. Will make later
        self.recipient = recipient #Who the money is going to. Communities may have their own accounts.
                                    # the global ledger may too. Your balance on a community/global account
                                    # lets you perform actions without being verified, as that transaction 
                                    # had to be verfied to go through, so it can be assumed safe.
        
