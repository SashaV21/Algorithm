heap = []
n = int(input())

for i in range(n):
    command = list(map(int, input().split()))
    if len(command) == 1:
        print(heap[0])
        heap[0] = heap[-1]
        pos = 0
        while pos * 2 + 2 < len(heap):
            max_son = pos * 2 + 1
            if heap[max_son] < heap[max_son + 1]:
                max_son += 1
            if heap[pos] < heap[max_son]:
                heap[pos], heap[max_son] = heap[max_son], heap[pos]
                pos = max_son
            else:
                break
        heap.pop()
    else:
        heap.append(command[1])
        pos = len(heap) - 1
        while pos > 0 and heap[pos] > heap[(pos - 1) // 2]:
            heap[pos], heap[(pos - 1) // 2] = heap[(pos - 1) // 2], heap[pos]
            pos = (pos - 1) // 2

