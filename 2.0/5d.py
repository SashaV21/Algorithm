data = input()

count = 0
flag = 0
for i in data:
    if i == '(':
        count += 1
    else:
        count -= 1
    if count < 0:
        print("NO")
        flag = 1
        break

if count == 0:
    print("YES")
elif count != 0 and flag != 1:
    print("NO")