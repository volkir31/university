class StringInOut:
    def getString(self):
        self.input_str = input()
    def printUpperString(self):
        print(self.input_str.upper())


a = StringInOut()
a.getString()
a.printUpperString()
