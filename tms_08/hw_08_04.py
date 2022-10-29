from enum import Enum
import uuid

class Currency(Enum):
    blr = 'BLR'
    usd = 'USD'
    rub = 'RUB'
    eur = 'EUR'


class Account:
    def __init__(self, person_id, currency, amount):
        self.person_id = person_id
        self.currency = currency
        self.amount = amount

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, new_amount):
        self.check_value(new_amount)
        self._amount = new_amount

    @staticmethod
    def check_value(value):
        if value < 0:
            raise Exception ('Value must be possitive')

    def info(self):
        return self.person_id, self.currency, self.amount


Petr = Account(str(uuid.uuid4()), Currency.usd.value, 333)
print(Petr.info())
