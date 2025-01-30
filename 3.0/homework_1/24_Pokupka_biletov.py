num_of_people = int(input())
MAX_TIME = 3700
a = [MAX_TIME] * (num_of_people + 3)
b = [MAX_TIME] * (num_of_people + 3)
c = [MAX_TIME] * (num_of_people + 3)
dp = [0] * (num_of_people + 3)
for i in range(3, num_of_people + 3):
    a[i], b[i], c[i] = map(int, input().split())

for i in range(3, num_of_people + 3):
    dp[i] = min(dp[i - 1] + a[i], dp[i - 2] + b[i - 1], dp[i - 3] + c[i - 2])

print(dp[-1])