def rsq(prefixsum, l, r):
    return prefixsum[r] - prefixsum[l - 1]


n, q = map(int, input().split())
data = [int(x) for x in input().split()]

prefixsum = [0] * (n + 1)

for i in range(1, n + 1):
    prefixsum[i] = prefixsum[i - 1] + data[i - 1]

for i in range(q):
    l, r = map(int, input().split())
    print(rsq(prefixsum, l, r))
