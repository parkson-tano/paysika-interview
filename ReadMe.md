"""
    We are tasked with implementing a money transfer system between users, supporting different 
    currencies and currency conversion. The system should be able to handle transfers between 
    accounts with the same currency, transfers between accounts with different currencies 
    (requiring currency conversion), and should raise appropriate exceptions for scenarios 
    such as transferring to a nonexistent user or attempting to transfer more money than the sender has.
    The system maintains two dictionaries: users_accounts for storing user account balances and 
    conversion_rate for storing currency conversion rates.
    The transfer_money function takes the sender's ID, receiver's ID, transfer amount, sender's 
    currency, and receiver's currency. It should deduct the amount from the sender's account, perform 
    any necessary currency conversion, and add the converted amount to the receiver's account. 
    If the transfer is of the same currency, no conversion is needed. If the currencies are different, 
    conversion should take place. If the receiver does not have the transfer currency, a new entry 
    should be created for that currency, with the initial amount being the appropriate transfer amount. 
    Otherwise, the transfer amount should be added to the existing currency value for the receiver.
    The provided TestSuite contains test cases to validate the correctness of the transfer_money function. 
    These tests cover scenarios like transferring between accounts with the same currency, transferring 
    between accounts with different currencies (testing currency conversion), transferring to a nonexistent 
    user, and attempting to transfer more money than the sender has.
"""