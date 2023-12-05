import math
part1, part2 = math.inf, math.inf

seeds = []
seed_ranges = []

class RangeMapper:
    def __init__(self):
        self.ranges = []

    def add_range(self, val_start, key_start, map_range):
        self.ranges.append((val_start, key_start, map_range))

    def find_destination(self, key):
        # Iterate through the ranges
        for val_start, key_start, map_range in self.ranges:
            if key >= key_start and key <= key_start + map_range:
                offset = key - key_start
                return val_start + offset

        # If the number is not in any range, it maps to itself
        return key
    
seed_to_soil_mapper = RangeMapper()
soil_to_fertilizer_mapper = RangeMapper()
fertilizer_to_water_mapper = RangeMapper()
water_to_light_mapper = RangeMapper()
light_to_temperature_mapper = RangeMapper()
temperature_to_humidity_mapper = RangeMapper()
humidity_to_location_mapper = RangeMapper()

# Open and read the file
with open('input.txt', 'r') as file:
    current_section = None

    # Process each line in the file
    for ln, line in enumerate(file):
        line = line.strip()
        # Skip empty lines
        if not line:
            continue

        # Check for section headers
        if 'seeds:' in line:
            seeds.extend(map(int, line.split(":")[1].strip().split(" ")))

            for i in range(0, len(seeds), 2):
                seed_start = seeds[i]
                seed_range = seeds[i + 1]
                seed_ranges.append((seed_start, seed_range))
                    
        elif 'seed-to-soil map:' in line:
            current_section = 'seed_to_soil'
        elif 'soil-to-fertilizer map:' in line:
            current_section = 'soil_to_fertilizer'
        elif 'fertilizer-to-water map:' in line:
            current_section = 'fertilizer_to_water'
        elif 'water-to-light map:' in line:
            current_section = 'water_to_light'
        elif 'light-to-temperature map:' in line:
            current_section = 'light_to_temperature'
        elif 'temperature-to-humidity map:' in line:
            current_section = 'temperature_to_humidity'
        elif 'humidity-to-location map:' in line:
            current_section = 'humidity_to_location'
        else:
            source_range, seed_range, map_range = [int(l) for l in line.split(" ")]
            
            if current_section == "seed_to_soil":
                seed_to_soil_mapper.add_range(source_range, seed_range, map_range)
            elif current_section == "soil_to_fertilizer":
                soil_to_fertilizer_mapper.add_range(source_range, seed_range, map_range)
            elif current_section == "fertilizer_to_water":
                fertilizer_to_water_mapper.add_range(source_range, seed_range, map_range)
            elif current_section == "water_to_light":
                water_to_light_mapper.add_range(source_range, seed_range, map_range)
            elif current_section == "light_to_temperature":
                light_to_temperature_mapper.add_range(source_range, seed_range, map_range)
            elif current_section == "temperature_to_humidity":
                temperature_to_humidity_mapper.add_range(source_range, seed_range, map_range)
            elif current_section == "humidity_to_location":
                humidity_to_location_mapper.add_range(source_range, seed_range, map_range)

def find_location(seed):
    soil = seed_to_soil_mapper.find_destination(seed)
    fertilizer = soil_to_fertilizer_mapper.find_destination(soil)
    water = fertilizer_to_water_mapper.find_destination(fertilizer)
    light = water_to_light_mapper.find_destination(water)
    temperature = light_to_temperature_mapper.find_destination(light)
    humidity = temperature_to_humidity_mapper.find_destination(temperature)
    location = humidity_to_location_mapper.find_destination(humidity)

    # print(f"Seed: {seed}, Soil: {soil}, Fertilizer: {fertilizer}, Water: {water}, Light: {light}, Temperature: {temperature}, Humidity: {humidity}, Location: {location}")

    return location

for seed in seeds:
    location = find_location(seed)

    if location < part1:
        part1 = location

for seed_start, seed_range in seed_ranges:
    for seed in range(seed_start, seed_start + seed_range + 1):
        location = find_location(seed)

        if location < part2:
            part2 = location

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")