class Queue:
    """Implement a queue class using two stacks.
     A queue is a data structure that supports the FIFO protocol (First in = first out).
     Your class should support the enqueue and dequeue methods like a standard queue."""
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, val):
        while len(self.stack1) != 0:
            self.stack2.append(self.stack1[-1])
            self.stack1.pop()

        self.stack1.append(val)

        while len(self.stack2) != 0:
            self.stack1.append(self.stack2[-1])
            self.stack2.pop()

    def dequeue(self):
        if len(self.stack1) != 0:
            return self.stack1.pop()


if __name__ == '__main__':
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    # 1 2 3