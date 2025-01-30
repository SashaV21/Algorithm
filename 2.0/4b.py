
dis = dict()
kand = input().split()
while kand:
    if kand[0] not in dis:
        dis[kand[0]] = int(kand[1])
    else:
        dis[kand[0]] += int(kand[1])
    kand = input().split()

for name, in sorted(dis):
    print(name, dis[name])
