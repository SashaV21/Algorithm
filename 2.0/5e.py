def readandsort():
    x = list(map(int, input().split()))
    for i in range(len(x)):
        x[i] = (x[i], i + 1)
    x.sort()
    return x


n, m = list(map(int, input().split()))
x = readandsort()
y = readandsort()
ynum = 0
ans = [0] * (n + 1)
for pupils, xnum in x:
    while ynum < len(y) and y[ynum][0] < pupils + 1:
        ynum += 1
    if ynum == len(y):
        break
    ans[xnum] = y[ynum][1]
    ynum += 1
print(ans)
