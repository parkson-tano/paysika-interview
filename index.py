import unittest

users_accounts = {"1": {"GBP": 100}, "2": {"EUR": 100}}
conversion_rate = {("GBP", "EUR"): 1.17}



class UserNotFoundException(Exception):
    pass


class SameAccountException(Exception):
    pass

class NotEnoughFundsException(Exception):
    pass

class CurrencyConvertionRateNotFoundException(Exception):
    pass

class MoneyTransfer:
    def __init__(self, user_accounts=None, conversion_rates=None):
        self.users_accounts = users_accounts if users_accounts is not None else {}
        self.conversion_rates = conversion_rate if conversion_rate is not None else {}


    def transfer_money(self, sender_id, receiver_id, amount, sender_currency, receiver_currency):
        if sender_id not in self.users_accounts:
            raise UserNotFoundException(f"Sender {sender_id} not found")
        
        if receiver_id not in self.users_accounts:
            raise UserNotFoundException(f"Receiver {receiver_id} not found")
        
        if sender_id == receiver_id:
            raise SameAccountException(f"Can not send to same account")
        

        if sender_currency in self.users_accounts[sender_id]:
            if self.users_accounts[sender_id][sender_currency] < amount:
                raise NotEnoughFundsException("Sender does not have enough funds")
            
        else:
            raise NotEnoughFundsException("Sender does not have enough funds")
        

        # if sender_currency != receiver_currency:
        #     conversion_key = (sender_currency, receiver_currency)

        #     if conversion_key in conversion_rate:
        #         converted_amount = amount * self.conversion_rate[conversion_key]

        #     else:
        #         raise ValueError(f"Conversion rate not available for {sender_currency} to {receiver_currency} ")
            
        # else:
        #     converted_amount =  amount

        converted_amount = self._convert_currency(amount, sender_currency, receiver_currency)

        users_accounts[sender_id][sender_currency] -= amount
        # self.users_accounts[receiver_id][receiver_currency] += converted_amount

        if receiver_currency in self.users_accounts[receiver_id]:
            users_accounts[receiver_id][receiver_currency] += converted_amount

        else:
            users_accounts[receiver_id][receiver_currency] = converted_amount


    def _convert_currency(self, amount, from_currency, to_currency):
        if from_currency == to_currency:
            return amount
        conversion_key = (from_currency, to_currency)

        if conversion_key in conversion_rate:
            return amount * conversion_rate[conversion_key]

        raise CurrencyConvertionRateNotFoundException(f'Conversion rate not available for {from_currency} to {to_currency}')
        



moneyTransfer = MoneyTransfer(user_accounts=users_accounts, conversion_rates=conversion_rate)


class TestSuite(unittest.TestCase):
    @staticmethod
    def reset_accounts():
        global users_accounts
        users_accounts = {"1": {"GBP": 100}, "2": {"EUR": 100}}

    def test_same_currency_transfer(self):
        self.reset_accounts()
        moneyTransfer.transfer_money("1", "2", 10, "GBP", "GBP")
        self.assertEqual(users_accounts["1"]["GBP"], 90)
        self.assertEqual(users_accounts["2"]["GBP"], 10)

    def test_transfer_to_nonexistent_user(self):
        with self.assertRaises(UserNotFoundException):
            moneyTransfer.transfer_money("1", "3", 10, "GBP", "GBP")

    def test_currency_conversion(self):
        self.reset_accounts()
        moneyTransfer.transfer_money("1", "2", 10, "GBP", "EUR")
        self.assertEqual(users_accounts["1"]["GBP"], 90)
        self.assertEqual(users_accounts["2"]["EUR"], 111.70)

    def test_not_enough_funds(self):
        with self.assertRaises(NotEnoughFundsException):
            moneyTransfer.transfer_money("1", "2", 110, "GBP", "GBP")


if __name__ == "__main__":
    unittest.main()