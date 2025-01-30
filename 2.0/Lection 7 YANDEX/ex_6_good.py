def is_parking_full(cars, n):
    events = []
    for i in range(len(cars)):
        tin, tout, place_from, place_to = cars[i]
        events.append((tin, 1, place_to - place_from + 1, i))
        events.append((tout, -1, place_to - place_from + 1, i))
    events.sort()
    occupied = 0
    now_cars = 0
    min_cars = len(cars) + 1
    for i in range(len(events)):
        if events[i][1] == -1:
            occupied -= events[i][2]
            now_cars -= 1
        elif events[i][1] == 1:
            occupied += events[i][2]
            now_cars += 1
        if occupied == n:
            min_cars = min(min_cars, now_cars)

    car_nums = set()
    now_cars = 0
    for i in range(len(events)):
        if events[i][1] == -1:
            car_nums.remove(events[i][3])
            occupied -= events[i][2]
            now_cars -= 1

        elif events[i][1] == 1:
            car_nums.add(events[i][3])
            occupied += events[i][2]
            now_cars += 1
        if occupied == n and min_cars == now_cars:
            return car_nums
    return set()

