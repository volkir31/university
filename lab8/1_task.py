class Stack():
    list1 = []

    def __str__(self):
        return str(self.list1)

    def push(self, item: str):
        if item in '(){}':
            self.list1.append(item)

    def pop(self):
        last_item = self.list1.pop()
        return last_item

    def is_empty(self):
        return True if len(self.list1) == 0 else False


list1 = input()
stack = Stack()
if len(list1) == 1:
    print(0)
else:
    for item in list1:
        if item in '({':
            stack.push(item)
        elif item in ')}':
            last_item = stack.pop()
            if item == ')' and last_item == '(' or item == '}' and last_item == '{':
                pass
            else:
                break
    if stack.is_empty():
        print(1)
    else:
        print(0)