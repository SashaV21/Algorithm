num_of_el = int(input())
arr = sorted(list(map(int, input().split())))
msg = int(input())
res = []
for i in range(msg):
    l, r = map(int, input().split())
    if arr[0] <= l <= arr[-1] or arr[0] <= r <= arr[-1]:
        '''
        Левый бинпоиск
        '''
        left = 0
        right = len(arr) - 1
        while left < right:
            medium = (left + right) // 2
            if arr[medium] >= l:
                right = medium
            else:
                left = medium + 1
        res.append(-left)
        '''
        Правый бинпоиск
        '''
        left = 0
        right = len(arr) - 1
        while left < right:
            medium = (left + right + 1) // 2
            if arr[medium] <= r:
                left = medium
            else:
                right = medium - 1

        res[-1] += (left + 1)
    else:
        res.append(0)
print(*res)
