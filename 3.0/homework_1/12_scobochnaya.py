def is_valid(s):
    stack = []
    for sym in s:
        if sym in '({[':
            stack.append(sym)
        else:
            if not stack or (sym == ')' and stack[-1] != '(') or (sym == ']' and stack[-1] != '[') or (
                    sym == '}' and stack[-1] != '{'):
                return False
            stack.pop()
    return not stack


def main():
    s = input()
    ans = is_valid(s)
    if ans is True:
        print('yes')
    else:
        print('no')


if __name__ == "__main__":
    main()
