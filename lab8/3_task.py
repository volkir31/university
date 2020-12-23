class Stack():
    list1 = []

    def __str__(self):
        return str(self.list1)

    def push(self, item: int):
        self.list1.append(item)

    def pop(self):
        last_item = self.list1.pop()
        return last_item

    def is_empty(self):
        return True if len(self.list1) == 0 else False


line = input().split()
stack = Stack()
for item in line:
    if item.isdigit():
        stack.push(int(item))
    else:
        if item == '*':
            stack.push(stack.pop() * stack.pop())
        elif item == '/':
            first = stack.pop()
            second = stack.pop()
            stack.push(second // first)
        elif item == '+':
            stack.push(stack.pop() + stack.pop())
        elif item == '-':
            first = stack.pop()
            second = stack.pop()
            stack.push(second - first)
        elif item == '^':
            first = stack.pop()
            second = stack.pop()
            stack.push(second // first)
print(stack.pop())
