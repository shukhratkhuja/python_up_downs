"""
Consider a scenario where you have a basic text editor 
and you want to add different features to it, 
such as bold text, italic text, and underlined text. 
You can implement this scenario using the decorator pattern as follows:
"""


class TextEditor:
    def __init__(self, text):
        self._text = text

    def get_text(self):
        return self._text

class BoldDecorator:
    def __init__(self, text_editor):
        self._text_editor = text_editor

    def get_text(self):
        return f"<b>{self._text_editor.get_text()}</b>"

class ItalicDecorator:
    def __init__(self, text_editor):
        self._text_editor = text_editor

    def get_text(self):
        return f"<i>{self._text_editor.get_text()}</i>"

class UnderlineDecorator:
    def __init__(self, text_editor):
        self._text_editor = text_editor

    def get_text(self):
        return f"<u>{self._text_editor.get_text()}</u>"

text_editor = TextEditor("Hello, World!")
bold_text_editor = BoldDecorator(text_editor)
italic_text_editor = ItalicDecorator(bold_text_editor)
underline_text_editor = UnderlineDecorator(italic_text_editor)

print(underline_text_editor.get_text())

# Output: <u><i><b>Hello, World!</b></i></u>

"""
In this example, the TextEditor class represents the basic text editor, 
and the Bold Decorator, ItalicDecorator, and UnderlineDecorator classes represent the different features 
that can be added to the text editor. 
Each decorator class takes a TextEditor instance as an argument in its constructor 
and adds the desired feature by wrapping the text with HTML tags. 
The get_text method of each decorator class simply returns the text with the added feature.

"""