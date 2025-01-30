def max_visitors_online(n, tin, tout):
    events = []
    for i in range(n):
        events.append((tin[i], -1))  # вход
        events.append((tout[i], 1))  # выход
    events.sort()
    online = 0
    max_online = 0
    for event in events:
        if event[1] == -1:
            online += 1
        else:
            online -= 1
        max_online = max(online, max_online)
    return max_online
