import datetime
import pytz


class Account:
    """ a simple account class with __balance"""

    @staticmethod
    def _current_time():
        utc_time=datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self,_name,__balance):
        self.__balance=__balance
        self._name=_name
        self._transaction_list=[]
        print("account created for {} ".format(self._name))
        self._transaction_list.append((Account._current_time(),__balance))

    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount
            self.show___balance()
            self._transaction_list.append((Account._current_time(),amount))

    def withdraw(self,amount):
        if 0<amount<=self.__balance:
            self.__balance-=amount
            self._transaction_list.append((Account._current_time(),-amount))
        else:
            print("Check the amount u have entered")

    def show__transaction(self):
        for date,amount in self._transaction_list:
            if amount>0:
                tran_type="deposit"
            else:
                tran_type="withdraw"
                amount*=-1
            print("{:6} {} on {} local time was {} ".format(amount,tran_type,date,date.astimezone()))

    def show___balance(self):
        print("remainig money is {} ".format(self.__balance))


if __name__=="__main__":
    manish=Account("Manish",5000)
    #    manish.show__transaction() # u donot need to type this now cuz its mentioned in line23
    manish.withdraw(599)
    manish.show__transaction()
    print()
    manish.show___balance()
    manish.__balance = 200 # to prevent like this things we add underscore in front
    print(manish.__dict__)
    manish._Account__balance = 7 # but like this u can change ur account balance in banks
    manish.show___balance()
