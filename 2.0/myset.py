import os

clear = lambda: os.system('clear')


def init_set(size):
    my_set = [[] for _ in range(size)]
    return my_set


def find(myset, size, x):
    for name in myset[x % size]:
        if name == x:
            return True
    return False


def add(myset, size, x):
    if find(myset, size, x):
        print("Sorry. That's element in set now")
        return
    else:
        myset[x % size].append(x)
        print("Successfully done!")


def delete(myset, size, x):
    if not find(myset, size, x):
        print("Sorry, that's element not in set now")
    else:
        xlist = myset[x % size]
        for i in range(len(xlist)):
            if xlist[i] == x:
                xlist[i] = xlist[len(xlist) - 1]
                xlist.pop()
                return


def print_set(myset, size):
    for i in range(size):
        print(f'{i}: ', end='')
        for j in range(len(myset[i])):
            print(myset[i][j], end=' ')
        print()


def main():
    print("Please, enter size of set!")
    size = int(input())
    my_set = init_set(size)
    clear()
    print("Set successfully done!")
    flag = -1
    while flag != 0:
        print('-------------------------------------')
        print('1. Enter "1" for add element')
        print('2. Enter "2" for find element')
        print('3. Enter "3" for delete element')
        print('4. Enter "4" for show your set')
        print('5. Enter "0" for exit')
        print('-------------------------------------')
        print('Enter your chose:')
        flag = int(input())
        clear()
        match flag:
            case 1:
                print("Enter element")
                x = int(input())
                add(my_set, size, x)
            case 2:
                print("Enter element")
                x = int(input())
                if find(my_set, size, x):
                    print("Element found!")
                else:
                    print("Not found element!")
            case 3:
                print("Enter element")
                x = int(input())
                delete(my_set, size, x)
            case 4:
                print("Your set:")
                print_set(my_set, size)
            case 0:
                print("Bye :)")

    pass


if __name__ == '__main__':
    main()
