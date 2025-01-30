def isDigitCount(x, y):
    def countdifit(num):
        digitcount = [0] * 10
        while num > 0:
            digitcount[num % 10] += 1
            num = num // 10
        return digitcount

    digitx = countdifit(x)
    digity = countdifit(y)
    for i in range(10):
        if digitx[i] != digity[i]:
            print("No oke")
            break
    print("Oke")

if __name__ == '__main__':
    x, y = map(int, input().split())
    print(isDigitCount(x, y))
