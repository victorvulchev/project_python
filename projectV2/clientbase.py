class Client():
    def __init__(self, name, pin, balance) -> None:
        self.name = name
        self.pin = pin
        self.balance = float(balance)

pesho = Client("Pesho", "1234", 1000)
gosho = Client("Gosho", "4321", 10000)
tosho = Client("Tosho", "5555", 6547)
misho = Client("Misho", "0000", 230)
tisho = Client("Tisho", "5678", 800)
clients = [pesho, gosho, tosho, misho, tisho]

commands = [
    "1. Withdraw",
            "2. Deposit",
            "3. Balance",
            "4. Quit"]
