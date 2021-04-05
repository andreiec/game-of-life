# Conway's Game of Life
A program written in Python to simulate [Conway's Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life) on a 110x110 surface.

## How to run
1. Either fork or download the repository
2. Install pygame dependency using `npm i` command
3. Run the program

## How does it work
1. Generate an empty matrix (Generation 0)
2. Start with some initial values (can be written by user)
3. Calculate the next generation based on 3 rules
    * Any live cell with two or three live neighbors survives.
    * Any dead cell with three live neighbors becomes a live cell.
    * All other live cells die in the next generation. Similarly, all other dead cells stay dead.
4. Draw new matrix
5. Loop steps 3 and 4 until program is terminated.

## Examples
<p>Below you can find some example of a standard setup.</p>
<img src="/example/example.gif" alt="iamge not found" width="420">

