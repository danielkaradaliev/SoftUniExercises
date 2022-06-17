number = int(input())
intersections = []

for _ in range(number):
    current_intersections = input().split("-")
    first_intervals = current_intersections[0].split(",")
    first_interval_start = int(first_intervals[0])
    first_interval_end = int(first_intervals[1]) + 1
    first_set = set(range(first_interval_start, first_interval_end))

    second_intervals = current_intersections[1].split(",")
    second_interval_start = int(second_intervals[0])
    second_interval_end = int(second_intervals[1]) + 1
    second_set = set(range(second_interval_start, second_interval_end))

    intersections.append(first_set.intersection(second_set))

longest_intersection = sorted(intersections, key=len, reverse=True)[0]

print(f"Longest intersection is {list(longest_intersection)} with length {len(longest_intersection)}")
