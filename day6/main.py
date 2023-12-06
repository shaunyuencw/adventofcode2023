import time
def calculate_ways_to_beat(race_time, record):
    # Calculate the square root part of the quadratic formula
    sqrt = ((((race_time / 2) ** 2) - record) ** 0.5)
    
    # Calculate the upper and lower bounds of hold times that beat the record
    upper_bound = int(sqrt + race_time / 2)
    lower_bound = int(race_time / 2 - sqrt)
    
    # Calculate the number of ways to beat the record by finding the range between upper_bound and lower_bound
    number_of_ways = upper_bound - lower_bound
    
    return number_of_ways

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
