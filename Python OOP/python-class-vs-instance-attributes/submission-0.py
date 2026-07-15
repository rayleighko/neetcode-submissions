class BankAccount: 
    # TODO: Add class and instance attributes at their appropriate places
    total_accounts = 0
    total_balance = 0
    def __init__(self, name: str, balance: int) -> None:
        self.__name = name
        self.__balance = balance
        BankAccount.total_accounts += 1
        BankAccount.total_balance += balance
        pass
    @property
    def name(self) -> str:
        return self.__name
    @property
    def balance(self) -> str:
        return self.__balance

# TODO: Create two accounts
alice = BankAccount('Alice', 1000)
bob = BankAccount('Bob', 2000)
# TODO: Print the information using the mentioned format
print(f"{alice.name}'s balance: ${alice.balance}")
print(f"{bob.name}'s balance: ${bob.balance}")
print(f"Total Accounts: {BankAccount.total_accounts}")
print(f"Total Balance: ${BankAccount.total_balance}")
