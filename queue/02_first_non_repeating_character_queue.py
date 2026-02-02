class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def is_empty(self):
        return len(self.stack1) == 0

    def enqueue(self, value):
        while self.stack1:
            self.stack2.append(self.stack1.pop())

        self.stack1.append(value)

        while self.stack2:
            self.stack1.append(self.stack2.pop())

    def dequeue(self):
        if self.is_empty():
            return None
        return self.stack1.pop()

    def front(self):
        if self.is_empty():
            return None
        return self.stack1[-1]


def first_non_repeating(stream):
    freq = {}
    result=[]
    q=MyQueue()
    for ch in stream:
        freq[ch]=freq.get(ch,0)+1
        q.enqueue(ch)
        while not q.is_empty() and freq[q.front()]>1:
            q.dequeue()
    if not q.is_empty():
       result.append(q.front())
    else:
        result.append(-1)
    return result

stream = input("Enter the character stream: ")
output = first_non_repeating(stream)
print("First non-repeating characters:")
print(output)
