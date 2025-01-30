"""
В постфиксной записи (или обратной польской записи) операция записывается после двух операндов. Например, сумма двух
чисел A и B записывается как A B +. Запись B C + D * обозначает привычное нам (B + C) * D, а запись A B C + D * +
означает A + (B + C) * D.
Достоинство постфиксной записи в том, что она не требует скобок и дополнительных соглашений о приоритете операторов для
своего чтения.
"""

data = list(input().split())
stack = []

for item in data:
    if item == '+':
        stack.append(stack.pop(-2) + stack.pop())
    elif item == '-':
        stack.append(stack.pop(-2) - stack.pop())
    elif item == '*':
        stack.append(stack.pop(-2) * stack.pop())
    else:
        stack.append(int(item))
print(stack[0])
