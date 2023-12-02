# Initial Approach
The primary challenge addressed in this script is the handling of overlapping number words within a text, such as in cases like:

`oneight, threeight, eightwo, eighthree`

To effectively manage this, the script follows a multi-step process:

1.  **Identify All Occurrences**: The script scans each line to find all occurrences of string representations of numbers ("one" through "nine").

2.  **Record Instances**: Each identified number word, along with its index in the line, is appended to a list named `found_matches` in a `(index, key)` tuple format.

3.  **Sort by Index**: The `found_matches` list is sorted based on the index. This sorting is crucial for processing the number words in the order they appear in the text.

4.  **Focus on First and Last Occurrences**: The main attention is given to the first and last occurrences of number words within a line, as these are pivotal in the context of the task.

5.  **Handle Special Cases**: A notable case is strings like `175rpdmxfeightwos`. A naive replacement of the first and last keys would incorrectly alter "eight" to "8", resulting in `175rpdmxf8wos`. This is not the desired outcome.

6.  **Conditional Replacement Strategy**:

- The script checks for existing numeric characters in the substring from the start of the line to the index of the first occurrence.

- If numeric characters are already present, the first occurrence is not replaced, as it is considered trivial for the final output.

- If no numeric characters are present, the script replaces both the first and last string occurrences of number words.

This approach ensures an accurate transformation of strings, like converting `175rpdmxfeightwos` to `175rpdmxfeigh2s`.

# Optimized Approach Using Bidirectional Pointer Technique

To handle complex cases like oneight and eightwo where number words overlap, the script uses a bidirectional pointer technique. This efficient method simultaneously scans each line from both ends:


**Bidirectional Pointer Technique** : The script reads each line from the start (forward) and the end (backward), acting like two pointers. This helps in quickly identifying the first and last number words.

**First and Last Occurrence Detection**: By tracking where these number words first appear in both the forward and backward scans, the script accurately finds the first and last occurrences, effectively dealing with any overlapping.

# --- Day 1: Trebuchet?! ---

Something is wrong with global snow production, and you've been selected to take a look. The Elves have even given you a map; on it, they've used stars to mark the top fifty locations that are likely to be having problems.

You've been doing this long enough to know that to restore snow operations, you need to check all  _fifty stars_  by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants  _one star_. Good luck!

You try to ask why they can't just use a  [weather machine](https://adventofcode.com/2015/day/1)  ("not powerful enough") and where they're even sending you ("the sky") and why your map looks mostly blank ("you sure ask a lot of questions")  and  hang on did you just say the sky ("of course, where do you think snow comes from") when you realize that the Elves are already loading you into a  [trebuchet](https://en.wikipedia.org/wiki/Trebuchet)  ("please hold still, we need to strap you in").

As they're making the final adjustments, they discover that their calibration document (your puzzle input) has been  _amended_  by a very young Elf who was apparently just excited to show off her art skills. Consequently, the Elves are having trouble reading the values on the document.

The newly-improved calibration document consists of lines of text; each line originally contained a specific  _calibration value_  that the Elves now need to recover. On each line, the calibration value can be found by combining the  _first digit_  and the  _last digit_  (in that order) to form a single  _two-digit number_.

For example:

```
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet

```

In this example, the calibration values of these four lines are  `12`,  `38`,  `15`, and  `77`. Adding these together produces  `_142_`.

Consider your entire calibration document.  _What is the sum of all of the calibration values?_


## --- Part Two ---

Your calculation isn't quite right. It looks like some of the digits are actually  _spelled out with letters_:  `one`,  `two`,  `three`,  `four`,  `five`,  `six`,  `seven`,  `eight`, and  `nine`  _also_  count as valid "digits".

Equipped with this new information, you now need to find the real first and last digit on each line. For example:

```
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen

```

In this example, the calibration values are  `29`,  `83`,  `13`,  `24`,  `42`,  `14`, and  `76`. Adding these together produces  `_281_`.

_What is the sum of all of the calibration values?_