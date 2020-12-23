class Stack():
    list1 = []

    def __str__(self):
        return str(self.list1)

    def push(self, item: str):
        if item in '(){}*/+-':
            self.list1.append(item)

    def pop(self):
        last_item = self.list1.pop()
        return last_item

    def is_empty(self):
        return True if len(self.list1) == 0 else False

    def get_len(self):
        return len(self.list1)


line = input()
stack = Stack()
count_item = 0
line_list = []
priorety_dict = {
    '^': 3, '*': 2, '/': 2, '+': 1, '-': 1, '(': 0
}
for item in line:
    if item == ' ':
        continue
    elif item.isdigit() or item.isalpha():
        if not line_list:
            line_list.append(item)
        else:
            last_elem = line_list[-1]
            if last_elem.isdigit():
                line_list[-1] = last_elem + item
            else:
                line_list.append(item)
    else:
        line_list.append(item)

out_list = []
current_operator = ''
for item in line_list:
    if item.isdigit() or item.isalpha():
        out_list.append(item)
    elif item in '*+-^/(':
        if not stack.is_empty():
            last_operator = stack.pop()
            try:
                while priorety_dict[last_operator] >= priorety_dict[item] and item != '(':
                    out_list.append(last_operator)
                    last_operator = stack.pop()
            except IndexError:
                pass
                stack.push(item)
            else:
                stack.push(last_operator)
                stack.push(item)
        else:
            stack.push(item)
    elif item == ')':
        last_item = stack.pop()
        while last_item != '(':
            out_list.append(last_item)
            last_item = stack.pop()
while not stack.is_empty():
    out_list.append(stack.pop())

print(' '.join(out_list))


