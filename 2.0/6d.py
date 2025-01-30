a, k, b, m, x = map(int, input().split())
l = 0
r = x * 2 // a + 1
while l < r:
    med = (r + l) // 2
    if (med - med // k) * a + (med - med // m) * b < x:
        l = med + 1
    else:
        r = med
print(l)