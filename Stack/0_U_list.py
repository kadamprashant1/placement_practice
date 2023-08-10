class stack(object):
    def __init__(self) -> None:
        self.items=[]
    def push(self, item) -> None:
        self.items.append(item)
    def pop(self) ->None:
        self.items.pop()
    def peek(self):
        if self.items:
            return self.items[-1]
        else:
            return "Stack is empty"
    def size(self):
        if self.items:
            return len(self.items)
        else:
            return None
    
if __name__ == "__main__":
    stack = stack()
    stack.push("10")
    stack.push("8")
    stack.push("3")
    stack.push("9")
    print(stack.size())
    stack.pop()
    print(stack.size())
    stack.pop()
    print(stack.peek())
