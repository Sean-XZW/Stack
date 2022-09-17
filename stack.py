class Stack(object):
    def __init__(self):
        self.items = []
        self.pointer = 0

    def is_empty(self):
        if self.pointer == 0:
            return False

    def push(self, item):
        self.items.append(item)
        self.pointer = self.pointer + 1

    def pop(self):
        self.items.pop()
        self.pointer = self.pointer - 1

my_stack = Stack()
my_stack.push('h')
my_stack.push('a')
my_stack.push('z')
my_stack.push('e')
my_stack.push('m')
print(my_stack.pop())
print(my_stack.pop())