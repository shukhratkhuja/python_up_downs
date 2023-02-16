"""
Strategy Pattern:
The Strategy Pattern allows you to define a family of algorithms, 
encapsulate each one as an object, and make them interchangeable. 
This lets the algorithm vary independently from the clients that use it.


Example: 
Suppose you have a sorting function that 
needs to support different algorithms (bubble sort, quick sort, etc.). 
You can implement a Strategy Pattern to encapsulate 
each sorting algorithm as a separate class. 
Here's some sample code in Python:
"""

class SortStrategy:
    def sort(self, data):
        pass

class BubbleSort(SortStrategy):
    def sort(self, data):
        # bubble sort implementation
        pass

class QuickSort(SortStrategy):
    def sort(self, data):
        # quick sort implementation
        pass

class Sorter:
    def __init__(self, strategy):
        self.strategy = strategy

