# You’re building part of a rental platform. Create a TenantLedger class to keep track of a tenant’s rent payments and charges.

# Class: TenantLedger
# Each tenant has:

# name (str)

# ledger (list of transactions)

# Each transaction is:

# A dictionary with keys: "type" (either "CHARGE" or "PAYMENT"), and "amount" (positive float)

from typing import Dict, List


LEDGER_TYPE = {"CHARGE", "PAYMENT"}

class TenantLedger:
    def __init__(self, name: str):
        self.name = name.title()
        self.ledger: List[Dict[str, float]] = []
    
    def __repr__(self):
        ledger_str = ', '.join([f"{tx['type']}: ${tx['amount']}" for tx in self.ledger])
        return f"Name={self.name}, Ledger=[{ledger_str}]"

    
    def add_charge(self, amount: float) -> None:
        self.ledger.append({"type": "CHARGE", "amount": amount})

    def add_payment(self, amount: float) -> None:
        self.ledger.append({"type": "PAYMENT", "amount": amount})
    
    def balance(self) -> float:
        total = 0.0
        for tx in self.ledger:
            if tx["type"] == "CHARGE":
                total += tx["amount"]
            else:  # PAYMENT
                total -= tx["amount"]
        return total

    def statement(self) -> List[str]:
        return [f"{tx['type']}: ${tx['amount']}" for tx in self.ledger]

Danny = TenantLedger('danny')

Danny.add_charge(1000)
Danny.add_charge(200)
Danny.add_charge(50)

print(Danny)
print(Danny.balance())

Danny.add_payment(1250)

print(Danny)
print(Danny.balance())
print(Danny.statement())



        