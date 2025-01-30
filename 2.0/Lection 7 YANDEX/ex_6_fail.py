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
    car_nums = set()
    best_car_nums = set()
    for i in range(len(events)):
        if events[i][1] == -1:
            occupied -= events[i][2]
            now_cars -= 1
            car_nums.remove(events[i][3])
        elif events[i][1] == 1:
            occupied += events[i][2]
            now_cars += 1
            car_nums.add(events[i][3])
        if occupied == n and now_cars < min_cars:
            best_car_nums = car_nums.copy()
            min_cars = now_cars
    return best_car_nums
