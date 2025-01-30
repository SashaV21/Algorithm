def is_parking_full(cars, n):
    events = []
    for car in cars:
        tin, tout, place_from, place_to = car
        events.append((tin, 1, place_to - place_from + 1))
        events.append((tout, -1, place_to - place_from + 1))
    events.sort()
    occupied = 0
    for i in range(len(events)):
        if events[i][1] == -1:
            occupied -= events[i][2]
        elif events[i][1] == 1:
            occupied += events[i][2]
        if occupied == n:
            return True
    return False
