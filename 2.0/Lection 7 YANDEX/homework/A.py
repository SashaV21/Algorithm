n = int(input())
events = []
for i in range(n):
    l, r = map(int, input().split())
    events.append((l, 1))
    events.append((r, -1))
events.sort()
count = 0
length = 0
start = events[0][0]
for event in events:
    if count > 0:
        length += event[0] - start
    start = event[0]
    count += event[1]
print(length)

