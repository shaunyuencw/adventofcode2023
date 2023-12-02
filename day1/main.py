import re

stringnums = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four" : "4",
    "five" : "5",
    "six" : "6",
    "seven" : "7",
    "eight" : "8",
    "nine" : "9", 
}

ans = 0
with open('input.txt', 'r') as file:
    i = 1
    for line in file:
        found_matches = []

        line = line.strip()
        for key in stringnums.keys():
            start = 0  # Initial search position
            while True:
                # Find next occurrence of the key
                index = line.find(key, start)
                if index == -1:  # No more occurrences
                    break
                found_matches.append((index, key))
                start = index + 1  # Update search position

        if len(found_matches) > 0:
            # Sort the list based on the first element of each tuple
            found_matches = sorted(found_matches, key=lambda x: x[0])

            # Check if there is number before first match
            if re.sub(r'[^\d]', '', line[0:found_matches[0][0]]) != "":
                # Ignore first match
                last = found_matches[-1][1]
                rline = line.replace(last, stringnums[last])

            else:
                first = found_matches[0][1]
                last = found_matches[-1][1]
            
                rline = line.replace(first, stringnums[first])
                rline = rline.replace(last, stringnums[last])
        
        else:
            rline = line

        nums = re.sub(r'[^\d]', '', rline)
        num = int(f"{nums[0]}{nums[len(nums)-1]}")

        ans += num

        combination = ["eightwo", "threeight", "eighthree", "oneight"]

        for c in combination:
            if c in line:
                print(f"Line {i}: {line}")
                print(f"CHECK: {c}")
                print(f"Replaced: {rline}")
                print(f"Found matches: {found_matches}")
                print(f"Number: {num}")
                print()

        i += 1

print(ans)
