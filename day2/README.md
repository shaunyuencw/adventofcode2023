# Approach

The script addresses the challenge of analyzing a series of games involving colored cubes, focusing on determining game feasibility and calculating minimum cube requirements. The process involves several key steps:

1.  **Inventory Initialization**:
    
    -   A dictionary named `inventory` is established, detailing the available quantity of each colored cube (red, green, blue).
2.  **Data Processing**:
    
    -   Game data is read from `input.txt`, with each line representing a game.
    -   The data for each game is subdivided into rounds, further broken down into individual draws of colored cubes.
3.  **Part 1: Feasibility Check**:
    
    -   The objective is to assess if each draw in a game is feasible given the inventory.
    -   We compared the cubes required in each draw against the inventory.
    -   A game is marked as impossible if any draw exceeds the available cubes for a color.
    -   The feasibility of each game is determined, and the IDs of valid games are added together.
4.  **Part 2: Minimum Requirement Calculation**:
    
    -   The goal is to identify the least number of cubes required for each color in a game.
    -   For each game, the script tracks the maximum cubes needed for each color across all rounds.
    -   The product of the max required for each color is calculated, representing the "power" of the minimum cube set for the game.
    -   The "power" values for all games are summed to derive the final outcome.
  
# --- Day 2: Cube Conundrum ---

You're launched high into the atmosphere! The apex of your trajectory just barely reaches the surface of a large island floating in the sky. You gently land in a fluffy pile of leaves. It's quite cold, but you don't see much snow. An Elf runs over to greet you.

The Elf explains that you've arrived at  _Snow Island_  and apologizes for the lack of snow. He'll be happy to explain the situation, but it's a bit of a walk, so you have some time. They don't get many visitors up here;  would you like to play a game  in the meantime?

As you walk, the Elf shows you a small bag and some cubes which are either red, green, or blue. Each time you play this game, he will hide a secret number of cubes of each color in the bag, and your goal is to figure out information about the number of cubes.

To get information, once a bag has been loaded with cubes, the Elf will reach into the bag, grab a handful of random cubes, show them to you, and then put them back in the bag. He'll do this a few times per game.

You play several games and record the information from each game (your puzzle input). Each game is listed with its ID number (like the  `11`  in  `Game 11: ...`) followed by a semicolon-separated list of subsets of cubes that were revealed from the bag (like  `3 red, 5 green, 4 blue`).

For example, the record of a few games might look like this:

```
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green

```

In game 1, three sets of cubes are revealed from the bag (and then put back again). The first set is 3 blue cubes and 4 red cubes; the second set is 1 red cube, 2 green cubes, and 6 blue cubes; the third set is only 2 green cubes.

The Elf would first like to know which games would have been possible if the bag contained  _only 12 red cubes, 13 green cubes, and 14 blue cubes_?

In the example above, games 1, 2, and 5 would have been  _possible_  if the bag had been loaded with that configuration. However, game 3 would have been  _impossible_  because at one point the Elf showed you 20 red cubes at once; similarly, game 4 would also have been  _impossible_  because the Elf showed you 15 blue cubes at once. If you add up the IDs of the games that would have been possible, you get  `_8_`.

Determine which games would have been possible if the bag had been loaded with only 12 red cubes, 13 green cubes, and 14 blue cubes.  _What is the sum of the IDs of those games?_

## --- Part Two ---

The Elf says they've stopped producing snow because they aren't getting any  _water_! He isn't sure why the water stopped; however, he can show you how to get to the water source to check it out for yourself. It's just up ahead!

As you continue your walk, the Elf poses a second question: in each game you played, what is the  _fewest number of cubes of each color_  that could have been in the bag to make the game possible?

Again consider the example games from earlier:

```
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green

```

-   In game 1, the game could have been played with as few as 4 red, 2 green, and 6 blue cubes. If any color had even one fewer cube, the game would have been impossible.
-   Game 2 could have been played with a minimum of 1 red, 3 green, and 4 blue cubes.

-   Game 3 must have been played with at least 20 red, 13 green, and 6 blue cubes.
-   Game 4 required at least 14 red, 3 green, and 15 blue cubes.
-   Game 5 needed no fewer than 6 red, 3 green, and 2 blue cubes in the bag.

The  _power_  of a set of cubes is equal to the numbers of red, green, and blue cubes multiplied together. The power of the minimum set of cubes in game 1 is  `48`. In games 2-5 it was  `12`,  `1560`,  `630`, and  `36`, respectively. Adding up these five powers produces the sum  `_2286_`.

For each game, find the minimum set of cubes that must have been present.  _What is the sum of the power of these sets?_