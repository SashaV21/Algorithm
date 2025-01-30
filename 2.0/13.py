len_of_sitting, num_of_coord = map(int, input().split())
data_coord = list(map(int, input().split()))

"""
Условием равноевесия явлеяется тот факт, что опоры должны быть по обе стороны от середины плиты.
Либо может остаться одна плита если длина нечет, и координата ее равна len//coord
"""

if len_of_sitting // 2 in data_coord and len_of_sitting % 2 == 1:
    print(len_of_sitting // 2)
else:
    data1 = []
    data2 = []
    for i in range(num_of_coord):
        if data_coord[i] < len_of_sitting // 2:
            data1.append(data_coord[i])
        else:
            data2.append(data_coord[i])
    print(data1[-1], data2[0])


