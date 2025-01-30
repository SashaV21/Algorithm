MAX = 101
n = int(input())
coord = [0] * MAX
dp = [0] * MAX
data = sorted(list(map(int, input().split())))
for i in range(1, n + 1):
    coord[i] = data[i - 1]

dp[2] = coord[2] - coord[1]
dp[3] = coord[3] - coord[1]
for i in range(4, n + 1):
    dp[i] = min(dp[i - 1], dp[i - 2]) + coord[i] - coord[i - 1]

print(dp[n])
