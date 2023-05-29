3rd_assignment_RT2
================================

This Repository is for the third assigmnent of Research Track 2

Introduction
------------

This assignment aims to understand the appropriate method to evaluate methods based on statistics. In this assignment, I compared my Algorithm of the fisrt assignment of RT1(algorithm1) with my colleague's one(algorithm2) when the silver and golden tokens are placed at random.

Result of Statistical Analysis
------------------------------

### Hypothesis ###

I built up two hypotheses as  follows;

1. Algorithm1 has higher success rate than algorithm2.
2. Algorithm2 completes tasks faster than algorithm2.

I consider it as a success case if a golden token and a silver token are placed side by side when the robot completes the task. Since we didn't implement a function to avoid delivered tokens, the robot can move them during the task not on purpose, which is the main cause of failure. Also, In testing the second hypothesis, I didn't consider the achievement ot the tasks.

### Experiments and Results ###

I made the token location list(`lacation.txt`) by `location_maker.py` which creates the arrays of tokens' locaion randomly. I checked the performances(completion time and final achievement) of each algorithm for the same 50 types of scenarios.

