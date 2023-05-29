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

| |>  |>  | Completion time [s] |> | Success(s)/Failure(f) |
|:----|:----|:----|:----|:----|:----|
|No.|Algorithm1|Algorithm2|difference|Algorithm1|Algorithm2|
|1|151.08|127.1|23.98|f|s|
|2|100.55|103.02|-2.47|f|f|
|3|120.49|90.73|29.76|f|f|
|4|119.78|104.3|15.48|f|f|
|5|178.13|144.23|33.9|f|f|
|6|156.19|124.84|31.35|s|f|
|7|166.69|98.97|67.72|s|s|
|8|146.34|99.26|47.08|f|s|
|9|136.61|127.65|8.96|f|f|
|10|149.11|103.77|45.34|f|s|
|11|139.04|101.25|37.79|s|s|
|12|118.29|110.53|7.76|s|f|
|13|168.03|101.28|66.75|f|f|
|14|143.86|119.38|24.48|s|f|
|15|125.52|99.24|26.28|f|f|
|16|153.92|113.54|40.38|s|f|
|17|90.47|110.59|-20.12|f|s|
|18|138.06|136.22|1.84|s|s|
|19|143.06|203.45|-60.39|s|f|
|20|120.52|359.59|-239.07|f|s|
|21|162.86|109.54|53.32|f|s|
|22|225.23|117.24|107.99|f|f|
|23|151.05|122.58|28.47|f|s|
|24|136.09|95.28|40.81|f|f|
|25|137.74|130.86|6.88|s|s|
|26|152.34|118.29|34.05|f|f|
|27|159.61|101.55|58.06|f|s|
|28|130.59|107|23.59|s|s|
|29|149.85|96.4|53.45|f|f|
|30|122.56|96.49|26.07|s|s|
|31|162.58|117.32|45.26|s|f|
|32|135.29|120.06|15.23|s|s|
|33|95.23|146.4|-51.17|s|f|
|34|141.08|131.61|9.47|f|f|
|35|164.14|128.33|35.81|f|f|
|36|142.61|119.98|22.63|f|f|
|37|110.85|80.16|30.69|f|f|
|38|122.05|114.66|7.39|f|f|
|39|158.92|129.55|29.37|f|f|
|40|118.6|99.43|19.17|f|f|
|41|175.93|156.45|19.48|f|f|
|42|164.3|144.21|20.09|s|s|
|43|149.3|108.84|40.46|s|f|
|44|122.42|109.22|13.2|s|s|
|45|174.49|131.13|43.36|f|f|
|46|146.74|121.45|25.29|s|f|
|47|147.21|122.3|24.91|f|f|
|48|161.45|163.17|-1.72|f|f|
|49|141.91|153.29|-11.38|s|s|
|50|116.74|114.36|2.38|s|s|
