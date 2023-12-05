import math
import multiprocessing
import time

class RangeMapper:
    def __init__(self):
        self.ranges = []

    def add_range(self, val_start, key_start, map_range):
        self.ranges.append((val_start, key_start, map_range))

    def find_destination(self, key, reverse=False):
        for val_start, key_start, map_range in self.ranges:
            if reverse:
                if val_start <= key < val_start + map_range:
                    offset = key - val_start
                    return key_start + offset
            else:
                if key_start <= key < key_start + map_range:
                    offset = key - key_start
                    return val_start + offset
        return key

def read_file(filename):
    mappers = {
        'seed-to-soil': RangeMapper(),
        'soil-to-fertilizer': RangeMapper(),
        'fertilizer-to-water': RangeMapper(),
        'water-to-light': RangeMapper(),
        'light-to-temperature': RangeMapper(),
        'temperature-to-humidity': RangeMapper(),
        'humidity-to-location': RangeMapper()
    }
    seeds = []
    seed_ranges = []

    with open(filename, 'r') as file:
        current_section = None
        for line in file:
            line = line.strip()
            if not line:
                continue

            # Check for section headers and update current_section
            if 'map:' in line:
                # Extract the section name and replace hyphens with underscores
                current_section = line.replace(" map:", "")
            elif 'seeds:' in line:
                seeds = list(map(int, line.split(":")[1].strip().split(" ")))
                for i in range(0, len(seeds), 2):
                    seed_ranges.append((seeds[i], seeds[i + 1]))
            else:
                source_range, seed_range, map_range = map(int, line.split(" "))
                if current_section in mappers:
                    mappers[current_section].add_range(source_range, seed_range, map_range)

    return mappers, seeds, seed_ranges

def find_location(seed, mappers):
    soil = mappers['seed-to-soil'].find_destination(seed)
    fertilizer = mappers['soil-to-fertilizer'].find_destination(soil)
    water = mappers['fertilizer-to-water'].find_destination(fertilizer)
    light = mappers['water-to-light'].find_destination(water)
    temperature = mappers['light-to-temperature'].find_destination(light)
    humidity = mappers['temperature-to-humidity'].find_destination(temperature)
    location = mappers['humidity-to-location'].find_destination(humidity)
    return location

def find_seed(location, mappers):
    humidity = mappers['humidity-to-location'].find_destination(location, reverse=True)
    temperature = mappers['temperature-to-humidity'].find_destination(humidity, reverse=True)
    light = mappers['light-to-temperature'].find_destination(temperature, reverse=True)
    water = mappers['water-to-light'].find_destination(light, reverse=True)
    fertilizer = mappers['fertilizer-to-water'].find_destination(water, reverse=True)
    soil = mappers['soil-to-fertilizer'].find_destination(fertilizer, reverse=True)
    seed = mappers['seed-to-soil'].find_destination(soil, reverse=True)
    return seed

def worker_process(process_id, num_processes, seed_ranges, mappers):
    min_valid_location = math.inf
    for location in range(process_id, 9999999999, num_processes):
        seed = find_seed(location, mappers)
        for seed_start, seed_range in seed_ranges:
            if seed_start <= seed < seed_start + seed_range:
                min_valid_location = min(min_valid_location, location)
                break
        if min_valid_location != math.inf:
            break
    return min_valid_location

def find_lowest_valid_location_parallel(seed_ranges, mappers, num_processes=4):
    with multiprocessing.Pool(num_processes) as pool:
        results = [pool.apply_async(worker_process, (i, num_processes, seed_ranges, mappers)) for i in range(num_processes)]
        lowest_locations = [res.get() for res in results]
        return min(lowest_locations)

def main():

    part1, part2 = math.inf, math.inf

    mappers, seeds, seed_ranges = read_file('input.txt')

    for seed in seeds:
        location = find_location(seed, mappers)

        if location < part1:
            part1 = location
    num_processes = 12

    start_time = time.time()
    part2 = find_lowest_valid_location_parallel(seed_ranges, mappers, num_processes)
    end_time = time.time()

    print(f"part1: {part1}")
    print(f"part2: {part2}, processed in {round(end_time - start_time, 2)} seconds")

if __name__ == "__main__":
    main()
