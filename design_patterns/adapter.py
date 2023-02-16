"""
Adapter Pattern:
The Adapter Pattern allows you to convert the interface of one class into another 
interface that the client expects. 
This is useful when you have an existing class that 
doesn't quite match what the client needs.


Example: 
Suppose you have a legacy Printer class that only supports printing plain text.
You want to use this class to print HTML documents. 
You can create an adapter that takes an HTML document 
and converts it to plain text that the Printer can understand. 
Here's some sample code in Python:

"""

def convert_to_plain_text():
    ...


class Printer:
    def print_text(self, text):
        print(text)

class HtmlPrinterAdapter(Printer):
    def print_html(self, html):
        # convert html to plain text
        text = convert_to_plain_text(html)
        # call the existing print_text method
        self.print_text(text)
