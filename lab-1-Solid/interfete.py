import numpy as np
from abc import ABC, abstractmethod

# The Single-Responsibility Principle (SRP)
# The Open-Closed Principle (OCP)
# The Liskov Substitution Principle (LSP)
# The Interface Segregation Principle (ISP)
# The Dependency inversion Principle (DIP)
class InputData(ABC):
    
    @abstractmethod
    def get_data(self) -> list:
        pass
    
class UserInput(InputData):
    
    def get_data(self) -> list:
        data_str = input("Enter a list of numbers separated by commas: ")
        data = [float(x.strip()) for x in data_str.split(",")]
        return data
    
class Progresie(ABC):
    @abstractmethod
    def progresie(self, list_: list) -> tuple:
        pass

class Ascendent(Progresie):
    def progresie(self, list_: list) -> tuple:
        return sorted(list_), sorted(list_)[0]

class Descendent(Progresie):
    def progresie(self, list_: list) -> tuple:
        return sorted(list_, reverse=True), sorted(list_)[-1]
    

class Operations(ABC):
    
    @abstractmethod
    def operation(self, list_: list) -> float:
        pass
    
class Mean(Operations):
    
    def operation(self, list_):
        return np.mean(list_)

class Max(Operations):
    
    def operation(self, list_):
        return np.max(list_)
    
class NumberList:
    
    def __init__(self, data):
        self.data = data
    
    def display_list(self):
        print("The numbers in the list are: ", self.data)
        
class Calculator:
    def __init__(self, number_list: NumberList, operations: list):
        self.number_list = number_list
        self.operations = operations
        
    def calculate(self):
        list_ = self.number_list.data
        for operation in self.operations:
            if isinstance(operation, Operations):
                print(f"The {operation.__class__.__name__} is {operation.operation(list_)}")
          
class Prg:
    def __init__(self, number_list: NumberList, progresie: list):
        self.number_list = number_list
        self.progresie = progresie
    
    def prg(self):
        list_ = self.number_list.data
        for p in self.progresie:
            if isinstance(p, Progresie):
                print(f"The {p.__class__.__name__} is {p.progresie(list_)}")


if __name__ == "__main__":
    
    user_input = UserInput()
    num_list = NumberList(user_input.get_data())
    num_list.display_list()
  
    calculator = Calculator(num_list, [Mean(), Max()])
    calculator.calculate()
    
    prg = Prg(num_list,[Ascendent(), Descendent()])
    prg.prg()
    