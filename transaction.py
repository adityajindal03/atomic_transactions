from connection import Connection
import contextlib

class Transaction(Connection):

    @contextlib.contextmanager
    def credit_account(self):

        try:
            previous_transaction = self.balance_sheet[-1]

            yield previous_transaction
            new_transaction = {
                "Previous Balance":previous_transaction["Final Balance"],
                "Final Balance": self.final_balance,
                "Transaction Type":"Credited"
                }
            self.commit_transaction(new_transaction)
        except:

            self.rollback_transaction()
            self.print_transactions()
            raise

        self.print_transactions()



    @contextlib.contextmanager
    def debit_account(self):
        try:
            previous_transaction = self.balance_sheet[-1]

            yield previous_transaction

            new_transaction = {
                "Previous Balance": previous_transaction["Final Balance"],
                "Final Balance": self.final_balance,
                "Transaction Type": "Debited"
            }
            self.commit_transaction(new_transaction)
        except:

            self.rollback_transaction()
            self.print_transactions()
            raise

        self.print_transactions()

    def print_transactions(self):
        for a_transaction in self.balance_sheet:
            print "Transaction Type:" + a_transaction["Transaction Type"] + "  Previous Balance:" + str(a_transaction["Previous Balance"]) + "  Final Balance:"+ str(a_transaction["Final Balance"])

    def add_money(self,amount):
        with self.credit_account() as w:
            self.final_balance = w["Final Balance"] + amount



    def remove_money(self,amount):
        with self.credit_account() as w:
            self.final_balance = w["Final Balance"] - amount







