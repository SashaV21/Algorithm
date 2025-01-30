data = list(map(int, input().split()))
dry_data = set()
for num in data:
    if num not in dry_data:
        print("NO")
        dry_data.add(num)
    else:
        print("YES")