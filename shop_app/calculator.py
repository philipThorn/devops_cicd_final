
class Calculator:

    def __init__(self, first_number, second_number):
        self.first_number = first_number
        self.second_number = second_number

    def add(self):
        result = self.first_number + self.second_number
        return result

    def multiply(self):
        result = self.first_number * self.second_number
        return result