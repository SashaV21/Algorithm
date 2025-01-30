"""
Из шахматной доски по границам клеток выпилили связную (не распадающуюся на части) фигуру без дыр. Требуется определить ее периметр.

Формат ввода
Сначала вводится число N (1 ≤ N ≤ 64) – количество выпиленных клеток. В следующих N строках вводятся координаты выпиленных клеток, разделенные пробелом (номер строки и столбца – числа от 1 до 8). Каждая выпиленная клетка указывается один раз.

Формат вывода
Выведите одно число – периметр выпиленной фигуры (сторона клетки равна единице).
"""

def neighbour(x: int, y: int, data: int) -> int:
    Neighboor = 0

    for example in data:
        if abs(x - example[0]) == 1 and y == example[1]:
            Neighboor += 1
        elif abs(y - example[1]) and x == example[0]:
            Neighboor += 1
    return Neighboor


data = []
amount = int(input())
sum = 0
for i in range(amount):
    example = list(map(int, input().split()))
    number = neighbour(example[0], example[1], data)
    if number == 0:
        sum += 4
    elif number == 1:
        sum += 2
    elif number == 3:
        sum -= 2
    data += [example]
print(sum)
