'''
TextProcessor: Utility class to handle text parsing of HTML text content
'''
import re

class TextProcessor:
    def __init__(self):
        self.NumberPattern = r'\b\d{1,3}(?:,\d{3})*(?:\.\d+)?\b|\b\d+\.\d+\b|\b\.\d+\b'
        self.WordPattern = r'\b[a-zA-Z]+(?:-[a-zA-Z]+)*\b'

    def findNumbers(self, content):
        '''
        Finds numbers in a string. Numbers can:
            1) Be integers
            2) Non-whole number (has decimals)
            3) Have a comma in it
        '''
        # Get string matches
        matches = re.findall(self.NumberPattern, content)

        # Convert from string to float, handling commas
        numbers = []
        for match in matches:
            clean = match.replace(',', '')
            numbers.append(float(clean))

        return numbers
    
    def firstDigit(self, num):
        '''
        Return the first digit of a number
        '''
        return float(str(num)[0])

    def findWords(self, text):
        '''
        Find all words in a set of text. For this use-case, we're
        only considering alphabetic text. Can also support considering
        hyphenated words as one word
        '''
        return re.findall(self.WordPattern, text)
    
    def firstLetter(self, text):
        '''
        Extract the first letter from a set of text
        '''
        return text[0]
