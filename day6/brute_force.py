import time
def calculate_ways_to_beat(race_time, record):
    ways_to_beat = 0
    max_holding_time = race_time // 2

    # Iterate up to the midpoint
    for hold_time in range(1, max_holding_time): # Does not include the midpoint
        my_distance = (race_time - hold_time) * hold_time
        if my_distance > record:
            ways_to_beat += 2  # Counting for both this time and its symmetrical counterpart

    # Calculate the midpoint distance
    midpoint_distance = max_holding_time * (race_time - max_holding_time)

    # Adjust for the midpoint
    if (race_time + 1) % 2 == 0:
        # Even race time: if the midpoint beats the record, add 2 (for both midpoints)
        if midpoint_distance > record:
            ways_to_beat += 2
    else:
        # Odd race time: if the midpoint beats the record, add 1
        if midpoint_distance > record:
            ways_to_beat += 1

    print(f"Race time: {race_time}, record: {record}, ways to beat: {ways_to_beat}")
    return ways_to_beat

part1, part2 = 1, 0
time_list = []
distance_list = []

with open('input.txt', 'r') as file:
    for line in file:
        parts = line.split()
        if 'Time' in line:
            time_list = [int(p) for p in parts[1:]]
        elif 'Distance' in line:
            distance_list = [int(p) for p in parts[1:]]

for i in range(len(time_list)):
    ways_to_beat = calculate_ways_to_beat(time_list[i], distance_list[i])
    part1 *= ways_to_beat
print(f"Part 1: {part1}")

# Part 2: Combining all values
c_time = int("".join(map(str, time_list)))
c_record = int("".join(map(str, distance_list)))
start_time = time.time()
part2 = calculate_ways_to_beat(c_time, c_record)
end_time = time.time()
print(f"Part 2: {part2}, processed in {round(end_time - start_time, 2)} seconds")
