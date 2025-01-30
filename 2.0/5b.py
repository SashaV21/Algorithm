n = int(input())
data = [int(x) for x in input().split()]
prefsum = []
sum_arr = 0
for i in data:
    sum_arr += i
    if sum_arr < 0:
        sum_arr = 0
    prefsum.append(sum_arr)
if set(prefsum) == {0}:
    print(max(data))
else:
    print(max(prefsum))