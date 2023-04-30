class account:
    def __init__(self,name: str) -> str:
        self.__acount_name = name
        self.__acount_balance = 0

    def deposit (self,amount:float) -> bool:
        if amount >0:
            self.__acount_balance += amount
            return True 
        elif amount <= 0:
            return False

    def withdraw(self,amount:float) -> bool:
        if amount <=0 or amount > self.__acount_balance:
            return False        
        else:
            self.__acount_balance -= amount
            return True

    def balance(self)  -> float:
        return self.__acount_balance 
    
    def get_name(self)  -> str:
        return self.__acount_name
