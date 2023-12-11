from random import randint

class Bank:
    def __init__(self, name):
        self.wallets = {}
        self.name = name

    def __repr__(self):
        return f'<Bank: {self.name}>'

class Wallet:
    def __init__(self, bank):
        self.bank = bank
        while True:
            self.id = randint(1000000, 9999999)
            if self.id not in self.bank.wallets.keys():
                self.bank.wallets[self.id] = 0
                break

    def __repr__(self):
        return f'<Wallet id {self.id}: amt=J${self.bank.wallets[self.id]}, bank={self.bank}>'

    def deposit(self, amt):
        self.bank.wallets[self.id] += amt

    def withdraw(self, amt):
        self.bank.wallets[self.id] -= amt

    def transfer_to(self, other_wallet, amt): #!!!
        Wallet.withdraw(self, amt)
        Wallet.deposit(other_wallet, amt)

class BrandedWallet(Wallet):
    def __init__(self, bank, brand):
        super().__init__(bank)
        self.brand = brand

    def __repr__(self):
        return f'<BrandedWallet id {self.id}: amt=J${self.bank.wallets[self.id]}, bank={self.bank}, brand={self.brand}>'

JigglypuffBank = Bank('JigglypuffBank')
LJMS_Daniel = BrandedWallet(JigglypuffBank, 'Treasury of High Jigglypuff')
Comrade_Dylan = Wallet(JigglypuffBank)
Comrade_Aloythius = Wallet(JigglypuffBank)
print(LJMS_Daniel, Comrade_Dylan, Comrade_Aloythius)

Comrade_Dylan.transfer_to(LJMS_Daniel, 10000000)
Comrade_Aloythius.transfer_to(LJMS_Daniel, 10000000)
LJMS_Daniel.deposit(9999999999999999999999)

print(LJMS_Daniel, Comrade_Dylan, Comrade_Aloythius)