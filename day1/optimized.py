ans = 0

forwardList = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
numstring = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

with open('input.txt', 'r') as file:
    for line in file:
        forward = line.strip()
        backward = forward[::-1]

        first_match = None
        last_match = None
        first_index = len(forward)
        last_index = len(backward)

        for word in forwardList:
            # Check forward
            index_forward = forward.find(word)
            if 0 <= index_forward < first_index:
                first_match = numstring.get(word, word)
                first_index = index_forward

            # Check backward
            word_reversed = word[::-1]
            index_backward = backward.find(word_reversed)
            if 0 <= index_backward < last_index:
                last_match = numstring.get(word, word)
                last_index = index_backward

        if first_match and last_match:
            num = int(f"{first_match}{last_match}")
            ans += num

print(ans)
