class Queue:
    def __init__(self):
        self.queue = []

    def push(self, n):
        self.queue.append(n)

    def pop(self):
        if len(self.queue) == 0:
            return None
        res = self.queue.pop(0)
        return res

    def front(self):
        return self.queue[0]

    def size(self):
        return len(self.queue)

    def clear(self):
        self.queue = []


def main():
    flag = 0
    q = Queue()
    while flag != 'exit':
        comm = list(input().split())
        flag = comm[0]
        match flag:
            case 'push':
                q.push(comm[-1])
                print("ok")
            case 'pop':
                res = q.pop()
                if res is None:
                    print('error')
                else:
                    print(res)
            case 'front':
                res = q.front()
                if res is None:
                    print('error')
                else:
                    print(res)
            case 'size':
                print(q.size())
            case 'clear':
                q.clear()
                print('ok')
            case 'exit':
                print('bye')


if __name__ == '__main__':
    main()
