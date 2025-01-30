n = int(input())
events = []
for i in range(n):
    t, l = map(int, input().split())
    events.append((t, 1))
    events.append((t + l, -1))
events.sort()
count = 0
max_count = 0
for event in events:
    if event[1] == 1:
        count += 1
    else:
        count -= 1
    max_count = max(count, max_count)

print(max_count)