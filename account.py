class account:
    """
    A class representing a bank account.
    """

    def __init__(self,name: str) -> str:
        """
        Initializes an Account object with the given name and a balance of 0.

        :param name: The name of the account holder.
        """

        self.__acount_name = name
        self.__acount_balance = 0

    def deposit (self,amount:float) -> bool:
        """
        Deposits the given amount into the account.

        :param amount: The amount to deposit.
        :return: True if the deposit was successful, False otherwise.
        """
        
        if amount >0:
            self.__acount_balance += amount
            return True 
        elif amount <= 0:
            return False

    def withdraw(self,amount:float) -> bool:
        """
        Withdraws the given amount from the account, if the balance is sufficient.

        :param amount: The amount to withdraw.
        :return: True if the withdrawal was successful, False otherwise.
        """
         
        if amount <= 0 or amount > self.__acount_balance:
            return False
            
        else:
            self.__acount_balance -= amount
            return True

    def balance(self)  -> float:
        """
        Returns the current balance of the account.

        :return: The current balance of the account.
        """
        
        return self.__acount_balance 
    
    def get_name(self)  -> str:
        """
        Returns the name of the account holder.

        :return: The name of the account holder.
        """
        
        return self.__acount_name
