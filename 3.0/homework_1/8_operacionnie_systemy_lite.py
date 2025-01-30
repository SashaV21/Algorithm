k = int(input())
points_x = []
points_y = []
for _ in range(k):
    x, y = map(int, input().split())
    points_x.append(x)
    points_y.append(y)

print(min(points_x), min(points_y), max(points_x), max(points_y))