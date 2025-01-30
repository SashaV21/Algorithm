n, k = map(int, input().split())

if k >= n:
    k = n - 1

dp = [0] * n

dp[1] = 1

for i in range(2, k + 1):
    dp[i] = dp[i - 1] * 2

for i in range(k + 1, n):
    dp[i] = sum(dp[i - k:i])
print(dp[-1])


