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

Here is the result of the experiment.

![a1](https://github.com/kazu610/3rd_assignment_RT2/assets/114085558/70080272-e7a4-4722-8c98-120b2b3bf464)
![a2](https://github.com/kazu610/3rd_assignment_RT2/assets/114085558/b4323ec3-13e9-4f49-ab24-7541616fea40)
![dif](https://github.com/kazu610/3rd_assignment_RT2/assets/114085558/491b0241-2e25-4151-a85e-9d145b2f825c)
![mean](https://github.com/kazu610/3rd_assignment_RT2/assets/114085558/99362830-53d1-444d-b798-32379ebdfeb4)


| |Success|Failure|Total|
|:----|:----|:----|:----|
|Algorithm1|20|30|50|
|Algorithm2|19|31|50|
|Total|39|61| |


