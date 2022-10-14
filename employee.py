"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

from typing import Optional
from abc import ABCMeta, abstractmethod

##### Abstract Classes #####

class Commission(metaclass=ABCMeta):
    @abstractmethod
    def __str__(self) -> str:
        raise NotImplementedError()

    """
    Returns Monthly pay from commission
    """
    @abstractmethod
    def get_pay(self) -> int:
        raise NotImplementedError()

class BasePay(metaclass=ABCMeta):

    @abstractmethod
    def __str__(self) -> str:
        raise NotImplementedError()

    """
    Returns Monthly pay from base pay
    """
    @abstractmethod
    def get_pay(self) -> int:
        raise NotImplementedError()

##### CONCRETE IMPLEMENTATIONS #####

## Commission implementation

class BonusCommission(Commission):
    __amount: int

    def __init__(self, amount) -> None:
        self.__amount = amount

    def __str__(self) -> str:
        return f"bonus commission of {self.__amount}"

    def get_pay(self) -> int:
        return self.__amount

class ContractComission(Commission):
    __amount_per: int
    __contracts: int

    def __init__(self, amount_per, contracts) -> None:
        self.__amount_per = amount_per
        self.__contracts = contracts

    def __str__(self) -> str:
        return f"commission for {self.__contracts} contract(s) at {self.__amount_per}/contract"

    def get_pay(self) -> int:
        return self.__amount_per * self.__contracts


## BasePay implementations

class SalaryPay(BasePay):
    __monthly_pay: int

    def __init__(self, monthly_pay: int) -> None:
        self.__monthly_pay = monthly_pay

    def __str__(self) -> str:
        return f"monthly salary of {self.__monthly_pay}"

    def get_pay(self) -> int:
        return self.__monthly_pay


class ContractPay(BasePay):
    __hours: int
    __per_hour: int

    def __init__(self, hours, per_hour) -> None:
        self.__hours = hours
        self.__per_hour = per_hour
    
    def __str__(self) -> str:
        return f"contract of {self.__hours} hours at {self.__per_hour}/hour"
    
    def get_pay(self) -> int:
        return self.__hours * self.__per_hour

#### EMPLOYEE IMPLEMENTATION ####

class Employee:
    __name: str
    __base: BasePay
    __commission: Optional[Commission]

    def __init__(self, name: str, base: BasePay, commission: Optional[Commission] = None) -> None:
        self.__name = name
        self.__base = base
        self.__commission = commission

    def get_pay(self) -> int:
        pay = self.__base.get_pay()
        if self.__commission is not None:
            pay += self.__commission.get_pay()
        return pay

    def __str__(self) -> str:
        string = f"{self.__name} works on a {self.__base}"
        if self.__commission is not None:
            string += f" and receives a {self.__commission}"
        string += f".  Their total pay is {self.get_pay()}." # Double space! Eeeew!
        return string
    

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee(
    'Billie',
    SalaryPay(4000)
)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee(
    'Charlie',
    ContractPay(100, 25)
)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee(
    'Renee',
    SalaryPay(3000),
    commission = ContractComission(200, 4)
)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee(
    'Jan',
    ContractPay(150, 25),
    commission=ContractComission(220, 3)
)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee(
    'Robbie',
    SalaryPay(2000),
    commission=BonusCommission(1500)
)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee(
    'Ariel',
    ContractPay(120, 30),
    commission=BonusCommission(600)
)
