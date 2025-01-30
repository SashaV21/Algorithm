n = int(input())
ans = set(range(1, n + 1))

while (data := input()) != 'HELP':
    massage = input()
    pwd = set([int(x) for x in data.split()])
    if massage == "YES":
        ans &= pwd
    else:
        ans -= pwd

print(*sorted(ans))