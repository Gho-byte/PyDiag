import gc

class CompteBancaire:
    def __init__(self, initial_solde=0, owner_name='', bank_name='Bank PyDiag'):
        self.__amount = initial_solde
        self.__bank_name = bank_name
        self.__owner_name = owner_name

    @property
    def accountAmount(self):
        return self.__amount

    @property
    def accountBank(self):
        return self.__bank_name

    @property
    def accountOwner(self):
        return self.__owner_name

    @classmethod
    def openAccounts(self):
        return len([obj for obj in gc.get_objects() if isinstance(obj, self)])

    def deposer(self, amount):
        if amount > 0:
            self.__amount += amount
            return True
        return False

    def retirer(self, amount):
        if amount <= self.__amount:
            self.__amount -= amount
            return True
        return False

    @staticmethod
    def devise(amount, taux):
        if amount < 0 or taux < 0: return False
        return amount * taux
    # def devise_transfer(source_account, destination_account):
    #     if source_account.accountAmount <= 0: return False
    #     destination_account.deposer(source_account.accountAmount)
    #     source_account.retirer(source_account.accountAmount)
    #     return True


# account1 = CompteBancaire('CIH')
# account2 = CompteBancaire('BankaLik')
# account3 = CompteBancaire('BMCE')
# print(f'[+] {account1.openAccounts()} accounts are open')
compte = CompteBancaire(owner_name="Ali", initial_solde=100)
compte.deposer(50)
compte.retirer(30)
print(compte.accountAmount)
