data = input().split()

for i in range(len(data)):
    c = data[:i] + data[i + 1:]
    if data[i] not in c:
        print(data[i], end=' ')