class Stackempty(Exception):
    """The stack is empty u cant pop """
    pass

class Stack():
    def __init__(self) -> None:
        self.stack= []
    
    def __repr__(self) -> str:
        return f"{self.stack}"
    def push(self,e):
        self.stack.append(e)

    def pop(self):
        assert not(self.isEmpty()) , "Stack is empty can't remove anything"

        return self.stack.pop()

    def top(self):
        value = self.stack.pop()
        self.stack.insert(len(self.stack),value)
        return (value)
    
    def size(self):
        return len(self.stack)
    
    def isEmpty(self):
        return True if Stack.size(self) == 0 else False 

    def clear(self):
        self.stack = []
    

    

