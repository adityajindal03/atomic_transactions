
class Connection:

    def __init__(self , starting_balance):
        self.balance_sheet = []
        starting_dict = {
            "Previous Balance":0,
            "Final Balance":starting_balance,
            "Transaction Type":"________"

        }
        self.balance_sheet.append(starting_dict)



    def commit_transaction(self,transaction_info):
        self.balance_sheet.append(transaction_info)
        print "Balance sheet updated"

    def rollback_transaction(self):
        print "Transastion failed"

