s = input()

stack = []

for sym in s:
    if sym in '({[':
        stack.append(sym)
    else:
        if not stack or (sym == ')' and stack[-1] != '(') or (sym == ']' and stack[-1] != '[') or (
                sym == '}' and stack[-1] != '{'):
            print("False")
            break
        stack.pop()
print(f'not stack')
