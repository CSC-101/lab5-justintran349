import data

# Write your functions for each part in the space below.

# Part 1
   # The function for Part 1 should be within the class in data.py.


# Part 2
   # The function for Part 2 should be within the class in data.py.


# Part 3
def time_add(time1: data.Time, time2: data.Time) -> data.Time:
    second = time1.second + time2.second
    minute = time1.minute + time2.minute
    hours = time1.hour + time2.hour
    if second >= 60:
        minute += second// 60
        second %= 60
    if minute >= 60:
        hours += minute // 60
        minute %= 60
    return data.Time(hours, minute, second)


# Part 4
def is_descending(numbers: list[float]) -> bool:
    for i in range(1, len(numbers)):
        if numbers[i] >= numbers[i - 1]:
            return False
    return True

# Part 5
def largest_between(numbers: list[int], lower: int, upper: int) -> int:
    if lower > upper:
        return None
    lower = max(0, lower)
    upper = min(len(numbers) - 1, upper)
    max_index = lower
    for i in range(lower, upper + 1):
        if numbers[i] > numbers[max_index]:
            max_index = i
    return max_index

# Part 6
def furthest_from_origin(points: list['Point']) -> int:
    if not points:
        return None
    max_distance_squared = -1
    max_index = 0
    for i, point in enumerate(points):
        distance_squared = point.x ** 2 + point.y ** 2
        if distance_squared > max_distance_squared:
            max_distance_squared = distance_squared
            max_index = i
    return max_index