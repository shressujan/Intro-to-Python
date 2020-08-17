class MaxStack:
    """Implement a class for a stack that supports all the regular functions (push, pop) and an additional function of
      max() which returns the maximum element in the stack (return None if the stack is empty). Each method should run
      in constant time"""

    def __init__(self):
        self.stack = []
        self.max_stack = [-1]   # Initializing the max_stack variable with -1 representing NONE

    def push(self, val):
        self.stack.append(val)
        if self.stack[-1] > self.max_stack[-1]:
            self.max_stack.append(self.stack[-1])

    def pop(self):
        if self.stack[-1] == self.max_stack[-1]:
            self.max_stack.pop()
        self.stack.pop()

    def max(self):
        if self.max_stack[-1] == -1:
            return 'None'
        return self.max_stack[-1]


if __name__ == '__main__':
    s = MaxStack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(2)
    print(s.max())
    # 3
    s.pop()
    s.pop()
    print(s.max())
    # 2
