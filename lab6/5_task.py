class StringInOut:
    def getString(self):
        self.input_str = input()
    def printUpperString(self):
        print(self.input_str.upper())


if __name__ == '__main__':
    a = StringInOut()
    a.getString()
    a.printUpperString()
