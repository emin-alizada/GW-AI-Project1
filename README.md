# A* Search - Group 2


[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)


## Usage
Application requires [Python](https://www.python.org/downloads/) 3.0+ to run.

Run using :
```sh
python AI_project1.py 
```

## Write up
After we read input from text files, we call the A_star function which takes pitcher capacities as a list and a single target value which is an integer.  The first thing we do is to check if the case provided is impossible to solve. If the target is not divisible by the greatest common divisor of pitcher capacities, then it is impossible to solve the problem, in this case -1 is returned.

Then we proceed to initialize the states. The state is a tuple that contains tuples of current water capacity pairs. It also contains two infinite pitchers out of which one always contains an infinite amount of water, and one initially contains 0, which is our target pitcher.

After that, we initialize the scores and two sets (open and closed) and start iterating till we have reached the goal or there are no unvisited states. First, we pop the state with the lowest f score, which is the sum of g score and h score, from the open set and print the path and the number of steps if we have reached the target. If we have not reached the target yet, we add the state we selected to the closed set and start iterating over the states that can be generated from the current state. 

We also check if we have reached the next step of our current state before, and at more cost, then we replace it and its path with the next step and next step’s path.



## Heuristic 

The heuristic we selected is a simple one:
- Calculate the absolute value of the distance between the target value and the amount of water contained in our target pitcher
- Divide the result by the capacity of the pitcher with a maximum capacity
- Multiply it by 2 to account for emptying the pitcher to infinite pitcher

This way we calculate the lower bound by which target can be reached.
