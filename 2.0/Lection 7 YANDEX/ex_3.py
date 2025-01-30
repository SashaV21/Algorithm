def boss_count(n, tin, tout, m, t_boss):
    events = []
    for i in range(n):
        events.append((tin[i], -1))
        events.append((tout[i], 1))
    for i in range(m):
        events.append((t_boss, 0))
    events.sort()
    online = 0
    boss_ans = []
    for event in events:
        if event[1] == -1:
            online += 1
        elif event[1] == 1:
            online -= 1
        else:
            boss_ans.append(online)
    return boss_ans

