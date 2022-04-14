from Stack import *
import math

def polish(stack):
    op =  (stack.pop())
    if op ==  '+': stack.push(int(stack.pop())+int(stack.pop()))
    if op ==  '-': stack.push(int(stack.pop())-int(stack.pop()))
    if op ==  '*': stack.push(int(stack.pop())*int(stack.pop()))
    if op ==  '/':stack.push(int(stack.pop())/int(stack.pop()))
    print(stack)
    return stack

def get_list():
    """Method to get a list of operators and numbers the scan ends when the user enter a '.' """
    print("Enter a numberthe operations, to finish the scan enter an '.':")
    stack =  Stack()
    while(True):
        stack.push(input())
        if stack.top() == '.':break
        if stack.top() in ['+','-','*','/']: stack = polish(stack)
        if not(str(stack.top()).isnumeric()): (stack.pop())


        
def main():
    polish(get_list())

if __name__=="__main__":
    main()