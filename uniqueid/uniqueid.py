import random

class uniqueid():
    
    def __init__(self):
        
        # lower case alphabets
        self.lower_alphabets = []
        for i in range(97, 123):
            self.lower_alphabets.append(i)
        self.lower_alphabets = tuple(self.lower_alphabets)

        # upper case alphabets
        self.upper_alphabets = []
        for i in range(65, 91):
            self.upper_alphabets.append(i)
        self.upper_alphabets = tuple(self.upper_alphabets)

        # numbers
        self.numbers = []
        for i in range(48, 58):
            self.numbers.append(i)
        self.numbers = tuple(self.numbers)

        # symbols
        self.symbols = (33, 35, 36, 37, 38, 43, 45, 61, 63, 64, 95)

        # brackets
        self.brackets = (40, 41, 91, 93, 123, 125)

        # hexadecimal
        self.hexadecimal = tuple(self.lower_alphabets + self.numbers)


    def generate_UUID(self):
        # UUID(8-4-4-4-12) -> xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
        self.uuid = ""
        for i in range(8):
            self.uuid += chr(random.choice(self.hexadecimal))
        self.uuid += "-"
        for _ in range(3):
            for i in range(4):
                self.uuid += chr(random.choice(self.hexadecimal))
            self.uuid += "-"
        for i in range(12):
            self.uuid += chr(random.choice(self.hexadecimal))
        return self.uuid
