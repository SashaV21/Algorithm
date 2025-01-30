import math

data = input().split()
stack = []
for item in data:
    if item == '+':
        op2 = int(stack.pop())
        op1 = int(stack.pop())
        stack.append(op1 + op2)
        print(op1 + op2)
    elif item == '-':
        op2 = int(stack.pop())
        op1 = int(stack.pop())
        stack.append(op1 - op2)
        print(op1 - op2)
    elif item == '/':
        op2 = int(stack.pop())
        op1 = int(stack.pop())
        res = round(op1 / op2)
        stack.append(res)
        print(res)
    elif item == '*':
        op2 = int(stack.pop())
        op1 = int(stack.pop())
        stack.append(op1 * op2)
        print(op1 * op2)
    else:
        stack.append(int(item))
print(*stack)
