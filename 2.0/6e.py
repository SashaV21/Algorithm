num_of_points, num_of_sec = map(int, input().split())

points = sorted(list(map(int, input().split())))

l = 0
r = points[-1] - points[0]

while l < r:
    m = (l + r) // 2
    value = points[0] + m
    num = 1
    for i in points:
        if value < i:
            num += 1
            value = i + m
    if num > num_of_sec:
        l = m + 1
    else:
        r = m
print(l)