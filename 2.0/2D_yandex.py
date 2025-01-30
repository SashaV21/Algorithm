"""
На столе лежали две одинаковые верёвочки целой положительной длины.
Петя разрезал одну из верёвочек на N частей, каждая из которых имеет целую положительную длину, так что на
столе стало N+1 верёвочек. Затем в комнату зашла Маша и взяла одну из лежащих на столе верёвочек.
По длинам оставшихся на столе N верёвочек определите, какую наименьшую длину может иметь верёвочка, взятая Машей.
"""


def main():
    _ = int(input())
    data = list(map(int, input().split()))
    data.sort()
    max = data[-1]
    if max <= (sum(data) - max):
        return sum(data)
    else:
        return (2 * max - sum(data))




if __name__ == '__main__':
    print(main())