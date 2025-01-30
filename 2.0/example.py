def find_simple_num(start, end):
    # item 80
    i = start
    while True:
        # item 81
        if i <= end:
            pass
        else:
            break
        # item 82
        j = 2
        # item 83
        is_prime = True
        while True:
            # item 84
            if j * j <= i and is_prime == True:
                pass
            else:
                break
            # item 85
            if i % j == 0:
                # item 86
                is_prime = False
            else:
                pass
            # item 87
            j = j + 1
        # item 88
        if is_prime == True and i > 1:
            # item 89
            print(i)
        else:
            pass
        # item 90
        i = i + 1

if __name__ == '__main__':
    find_simple_num(2, 8)