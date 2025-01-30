data = input()
book = {}
l = 0
length = 0
for r in range(len(data)):
    symbol = data[r]
    if symbol in book and book[symbol] >= l:
        l = book[symbol] + 1
    else:
        length = max(length, r - l + 1)
    book[symbol] = r
print(length)