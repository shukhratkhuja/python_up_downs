"""
Facade Pattern:
The Facade Pattern provides a simplified interface to a complex system. 
The Facade class defines a high-level interface 
that makes the subsystem easier to use.


Example: 
Suppose you have a complex API for performing various financial calculations. 
You can implement a Facade Pattern to provide 
a simpler interface to these calculations. Here's some sample code in Python:
"""

class FinancialCalculator:
    def calculate_interest(self, principal, rate, time):
        # complex interest calculation
        pass

    def calculate_payment(self, principal, rate, time):
        # complex payment calculation
        pass

class SimpleFinancialCalculator:
    def __init__(self):
        self.calculator = FinancialCalculator()

    def calculate_interest(self, principal, rate, time):
        return self.calculator.calculate_interest(principal, rate, time)

    def calculate_payment(self, principal, rate, time):
        return self.calculator.calculate_payment(principal, rate, time)
