n = int(input())
arr = list(map(int, input().split()))
m = int(input())
search = list(map(int, input().split()))

for element in search:
    res = [0, 0]
    if arr[0] <= element <= arr[-1]:
        l = 0
        r = len(arr) - 1
        while l < r:
            medium = (l + r) // 2
            if arr[medium] >= element:
                r = medium
            else:
                l = medium + 1
        res[0] = l + 1

        l = 0
        r = len(arr) - 1
        while l < r:
            m = (l + r + 1) // 2
            if arr[m] <= element:
                l = m
            else:
                r = m - 1
        res[1] = l + 1
    if res[0] > res[1]:
        res = [0, 0]
    print(*res)
