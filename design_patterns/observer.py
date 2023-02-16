"""
Consider a scenario where you have a stock market and 
you want to create a system that notifies investors whenever the stock price changes. 
You can implement this scenario using the observer pattern as follows:
"""

class Stock:
    def __init__(self, price):
        self._price = price
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self)
            print(observer.name)


    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        self._price = price
        self.notify()

class Investor:
    def __init__(self, name):
        self.name = name

    def update(self, stock):
        print(f"Notified: stock price changed to {stock.price}, Notification for investor: {self.name}")

stock = Stock(100)

investor1 = Investor('A')
investor2 = Investor('B')
investor3 = Investor('C')

stock.attach(investor1)
stock.attach(investor2)
stock.attach(investor3)

stock.price = 120
stock.price = 121
stock.price = 111
stock.price = 142
stock.price = 99
stock.price = 210
stock.price = 120

# Output:
# Notified: stock price changed to 120, Notification for investor: A
# Notified: stock price changed to 120, Notification for investor: B
# Notified: stock price changed to 120, Notification for investor: C
# Notified: stock price changed to 121, Notification for investor: A
# Notified: stock price changed to 121, Notification for investor: B
# Notified: stock price changed to 121, Notification for investor: C
# Notified: stock price changed to 111, Notification for investor: A
# Notified: stock price changed to 111, Notification for investor: B
# Notified: stock price changed to 111, Notification for investor: C
# Notified: stock price changed to 142, Notification for investor: A
# Notified: stock price changed to 142, Notification for investor: B
# Notified: stock price changed to 142, Notification for investor: C
# Notified: stock price changed to 99, Notification for investor: A
# Notified: stock price changed to 99, Notification for investor: B
# Notified: stock price changed to 99, Notification for investor: C
# Notified: stock price changed to 210, Notification for investor: A
# Notified: stock price changed to 210, Notification for investor: B
# Notified: stock price changed to 210, Notification for investor: C
# Notified: stock price changed to 120, Notification for investor: A
# Notified: stock price changed to 120, Notification for investor: B
# Notified: stock price changed to 120, Notification for investor: C

"""
In this example, the Stock class represents a stock in the stock market, 
and it acts as the subject that is being observed. 
The Investor class represents an investor, 
and it acts as the observer that is notified whenever the stock price changes. 
The Stock class keeps a list of its observers 
and notifies them whenever its price changes. 
The client code can create instances of both Stock and Investor, 
and connect them by calling the attach method on the Stock instance 
and passing the Investor instance as an argument. 
The Stock instance will then notify the Investor instance whenever its price changes.
"""