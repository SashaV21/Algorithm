class Stack:
    def __init__(self):
        self.stack = []

    def push(self, n):
        self.stack.append(n)

    def pop(self):
        if len(self.stack) == 0:
            return None
        res = self.stack.pop()
        return res

    def back(self):
        if len(self.stack) == 0:
            return None
        return self.stack[-1]

    def size(self):
        return len(self.stack)

    def clear(self):
        self.stack = []


def main():
    flag = 0
    s = Stack()
    while flag != 'exit':
        comm = list(input().split())
        flag = comm[0]
        match flag:
            case 'push':
                s.push(comm[-1])
                print("ok")
            case 'pop':
                res = s.pop()
                if res is None:
                    print('error')
                else:
                    print(res)
            case 'back':
                res = s.back()
                if res is None:
                    print('error')
                else:
                    print(res)
            case 'size':
                print(s.size())
            case 'clear':
                s.clear()
                print('ok')
            case 'exit':
                print('bye!')


if __name__ == '__main__':
    main()