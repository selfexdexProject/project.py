class CryptoTransaction:
    def __init__(self, sender, receiver, amount):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount

class CryptoPlatform:
    def __init__(self):
        self.users = {}
        self.transactions = []

    def create_user(self, username):
        self.users[username] = 100  # Give new users an initial balance of 100 tokens

    def make_transaction(self, sender, receiver, amount):
        if sender in self.users and receiver in self.users and self.users[sender] >= amount:
            self.users[sender] -= amount
            self.users[receiver] += amount
            transaction = CryptoTransaction(sender, receiver, amount)
            self.transactions.append(transaction)
            return True
        else:
            return False

    def get_balance(self, username):
        if username in self.users:
            return self.users[username]
        else:
            return 0

# Main program
crypto_platform = CryptoPlatform()
crypto_platform.create_user("Alice")
crypto_platform.create_user("Bob")

crypto_platform.make_transaction("Alice", "Bob", 30)

print("Alice's balance:", crypto_platform.get_balance("Alice"))
print("Bob's balance:", crypto_platform.get_balance("Bob"))

print("Transactions:")
for transaction in crypto_platform.transactions:
    print(f"{transaction.sender} sent {transaction.amount} to {transaction.receiver}")
