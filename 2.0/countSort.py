def countSort(seq):
    minval = min(seq)
    maxval = max(seq)
    k = maxval - minval + 1
    count = [0] * k
    for new in seq:
        count[new - minval] += 1
    nowpas = 0
    for i in range(0, k):
        for j in range(count[i]):
            seq[nowpas] = i + minval
            nowpas += 1

if __name__ == '__main__':
    seq = list(map(int, input().rstrip().split()))
    countSort(seq)
    print(*seq)
