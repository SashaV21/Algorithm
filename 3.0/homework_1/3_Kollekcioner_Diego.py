"""Диего увлекается коллекционированием наклеек. На каждой из них написано число, и каждый коллекционер мечтает собрать
наклейки со всеми встречающимися числами. Диего собрал N наклеек, некоторые из которых, возможно, совпадают.
Как-то раз к нему пришли K коллекционеров. i-й из них собрал все наклейки с номерами не меньшими, чем pi.
Напишите программу, которая поможет каждому из коллекционеров определить, сколько недостающих ему наклеек есть у Диего.
Разумеется, гостей Диего не интересуют повторные экземпляры наклеекa."""

n = int(input())
di = list(map(int, input().split()))
k = int(input())
kol = list(map(int, input().split()))

uniq_di = sorted(list(set(di)))

if len(uniq_di) == 1:
    for item in kol:
        if uniq_di[0] < item:
            print(1)
        else:
            print(0)
else:
    for item in kol:
        left = 0
        right = len(uniq_di) - 1
        if uniq_di[left] >= item:
            print(0)
            continue
        while left < right:
            medium = (left + right + 1) // 2
            if uniq_di[medium] < item:
                left = medium
            else:
                right = medium - 1
        print(left + 1)



