n = int(input())
book = dict()

for i in range(n):
    d, a = map(int, input().split())
    if d not in book:
        book[d] = a
    else:
        book[d] += a

for color in sorted(book):
    print(color, book[color])

