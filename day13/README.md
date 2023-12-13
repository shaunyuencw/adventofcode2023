
# Approach

In addressing "Day 11: Cosmic Expansion," my approach was focused on spatial symmetry analysis and minor modifications to adapt to different puzzle requirements.

## Spatial Symmetry Analysis in Puzzle Patterns

-   **Matrix-Based Puzzle Representation**: I conceptualized each puzzle as a matrix, where each cell represents a part of the pattern. This matrix representation was instrumental in simplifying my approach towards identifying symmetrical lines.
-   **Row and Column-wise Symmetry Checking**: The core of my solution involved checking for symmetry across specified rows and columns. For columns, I efficiently reused the row-wise symmetry logic by transposing the matrix, thus converting column checks into row checks.
-   **Handling Asymmetrical Splits**: In cases where a line split the puzzle into unequal halves, my solution focused on the smaller section, comparing it with the corresponding part of the larger section, thus maintaining the integrity of the symmetry check.

## Adjustments for Smudges in Part Two

-   **Extension for Single Smudge Identification**: Building on the symmetry checking logic from part one, I introduced a new function `is_smudged`. This function was designed to detect if exactly one change (a smudge) could make two otherwise asymmetrical sections symmetric.
- 
## Reflection

This challenge sharpened my pattern recognition and matrix manipulation skills, highlighting the need for flexible algorithms. It evolved from simple symmetry analysis in part one to subtle, smudge-based adjustments in part two, blending logical reasoning with creative problem-solving.

# --- Day 13: Point of Incidence ---

With your help, the hot springs team locates an appropriate spring which launches you neatly and precisely up to the edge of  _Lava Island_.

There's just one problem: you don't see any  _lava_.

You  _do_  see a lot of ash and igneous rock; there are even what look like gray mountains scattered around. After a while, you make your way to a nearby cluster of mountains only to discover that the valley between them is completely full of large  _mirrors_. Most of the mirrors seem to be aligned in a consistent way; perhaps you should head in that direction?

As you move through the valley of mirrors, you find that several of them have fallen from the large metal frames keeping them in place. The mirrors are extremely flat and shiny, and many of the fallen mirrors have lodged into the ash at strange angles. Because the terrain is all one color, it's hard to tell where it's safe to walk or where you're about to run into a mirror.

You note down the patterns of ash (`.`) and rocks (`#`) that you see as you walk (your puzzle input); perhaps by carefully analyzing these patterns, you can figure out where the mirrors are!

For example:

```
#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#

```

To find the reflection in each pattern, you need to find a perfect reflection across either a horizontal line between two rows or across a vertical line between two columns.

In the first pattern, the reflection is across a vertical line between two columns; arrows on each of the two columns point at the line between the columns:

```
123456789
    ><   
#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.
    ><   
123456789

```

In this pattern, the line of reflection is the vertical line between columns 5 and 6. Because the vertical line is not perfectly in the middle of the pattern, part of the pattern (column 1) has nowhere to reflect onto and can be ignored; every other column has a reflected column within the pattern and must match exactly: column 2 matches column 9, column 3 matches 8, 4 matches 7, and 5 matches 6.

The second pattern reflects across a horizontal line instead:

```
1 #...##..# 1
2 #....#..# 2
3 ..##..### 3
4v#####.##.v4
5^#####.##.^5
6 ..##..### 6
7 #....#..# 7

```

This pattern reflects across the horizontal line between rows 4 and 5. Row 1 would reflect with a hypothetical row 8, but since that's not in the pattern, row 1 doesn't need to match anything. The remaining rows match: row 2 matches row 7, row 3 matches row 6, and row 4 matches row 5.

To  _summarize_  your pattern notes, add up  _the number of columns_  to the left of each vertical line of reflection; to that, also add  _100 multiplied by the number of rows_  above each horizontal line of reflection. In the above example, the first pattern's vertical line has  `5`  columns to its left and the second pattern's horizontal line has  `4`  rows above it, a total of  `_405_`.

Find the line of reflection in each of the patterns in your notes.  _What number do you get after summarizing all of your notes?_

Your puzzle answer was  `42974`.

## --- Part Two ---

You resume walking through the valley of mirrors and -  _SMACK!_  - run directly into one. Hopefully  nobody  was watching, because that must have been pretty embarrassing.

Upon closer inspection, you discover that every mirror has exactly one  _smudge_: exactly one  `.`  or  `#`  should be the opposite type.

In each pattern, you'll need to locate and fix the smudge that causes a  _different reflection line_  to be valid. (The old reflection line won't necessarily continue being valid after the smudge is fixed.)

Here's the above example again:

```
#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#

```

The first pattern's smudge is in the top-left corner. If the top-left  `#`  were instead  `.`, it would have a different, horizontal line of reflection:

```
1 ..##..##. 1
2 ..#.##.#. 2
3v##......#v3
4^##......#^4
5 ..#.##.#. 5
6 ..##..##. 6
7 #.#.##.#. 7

```

With the smudge in the top-left corner repaired, a new horizontal line of reflection between rows 3 and 4 now exists. Row 7 has no corresponding reflected row and can be ignored, but every other row matches exactly: row 1 matches row 6, row 2 matches row 5, and row 3 matches row 4.

In the second pattern, the smudge can be fixed by changing the fifth symbol on row 2 from  `.`  to  `#`:

```
1v#...##..#v1
2^#...##..#^2
3 ..##..### 3
4 #####.##. 4
5 #####.##. 5
6 ..##..### 6
7 #....#..# 7

```

Now, the pattern has a different horizontal line of reflection between rows 1 and 2.

Summarize your notes as before, but instead use the new different reflection lines. In this example, the first pattern's new horizontal line has 3 rows above it and the second pattern's new horizontal line has 1 row above it, summarizing to the value  `_400_`.

In each pattern, fix the smudge and find the different line of reflection.  _What number do you get after summarizing the new reflection line in each pattern in your notes?_

Your puzzle answer was  `27587`.