3rd_assignment_RT2
================================

This Repository is for the third assigmnent of Research Track 2

Introduction
------------

This assignment aims to understand the appropriate method to evaluate methods based on statistics. In this assignment, I compared my Algorithm of the fisrt assignment of RT1(algorithm1) with my colleague's one(algorithm2) when the silver and golden tokens are placed at random.

Result of the assignment
------------------------------

### Hypothesis ###

I built up two hypotheses as follows;

1. Algorithm1 has a higher success rate than algorithm2.
2. Algorithm2 completes tasks faster than algorithm1.

I consider it as a success case if a golden token and a silver token are placed side by side when the robot completes the task. Since we didn't implement a function to avoid delivered tokens, the robot can move them during the task not on purpose, which is the main cause of failure. Also, In testing the second hypothesis, I didn't consider the achievement ot the tasks.

### Experiments and Results ###

I made the token location list(_lacation.txt_) by _location_maker.py_ which creates the arrays of tokens' locaion randomly. I checked the performances(completion time and final achievement) of each algorithm for the same 50 types of scenarios.

Here is the results of the experiment.

<img src="https://github.com/kazu610/3rd_assignment_RT2/assets/114085558/70080272-e7a4-4722-8c98-120b2b3bf464">
<img src="https://github.com/kazu610/3rd_assignment_RT2/assets/114085558/b4323ec3-13e9-4f49-ab24-7541616fea40">
<img src="https://github.com/kazu610/3rd_assignment_RT2/assets/114085558/491b0241-2e25-4151-a85e-9d145b2f825c">
<img src="https://github.com/kazu610/3rd_assignment_RT2/assets/114085558/99362830-53d1-444d-b798-32379ebdfeb4">

| |Success|Failure|Total|
|:----|:----|:----|:----|
|Algorithm1|20|30|50|
|Algorithm2|19|31|50|
|Total|39|61|100|

According to the above results, Algorithm1 has a slightly higher success rate and is slower than algorithm2 by 19 seconds on average. 

### Statistical Analysis ###

I applied chi-square test to the first hypothesis and paired t-test to the second hypothesis.

1. Chi-Square Test
    I computed the expacted values for each value.

    | |Algorithm1(expected value)|Algorithm2(expected value)|
    | |Success|Failure|
    |:----|:----|:----|
    |Algorithm1|20(19.5)|30(30.5)|
    |Algorithm2|19(19.5)|31(30.5)|

    Based one the above table, chi-square value is calculated as follow.
    $$
    \begin{align*}
    \chi 2 &= \Sigma \dfrac{((\textrm{actual value})-(\textrm{expected value}))^2}{(\textrm{expected value})} \\
    &= 0.0420
    \end{align*}
    $$
    Under the null hypothesis, this chi-square value follows a chi-square-distribution with 1 degrees of freedom since there are 2 rows and 2 columns.

    |$\chi 2$|Chi-square-distribution (DoF=1, α=0.05)|
    |:----|:----|
    |0.0420|3.84|

    Since the obtained chi-square value is smaller than chi-square-distribution, I can not reject the null hupothesis in this case. Therefore, the fisrt hypothesis is not accepted, algorithm1 doesn't have a higher success rate than algorithm2 _significantly_.

    <br>

2. Paired T-Test
    Based the mean difference and the standard deviation of the differences, I computed the standard error of the mean difference.
    $$
    \begin{align*}
        SE(\bar{d}) &= \dfrac{s_d}{\sqrt{n}} \\
        &= 6.546
    \end{align*} 
    $$
    T-statistic is calculated as follows.
    $$
    \begin{align*}
        T &= \dfrac{\bar{d}}{SE(\bar{d})} \\
        &= 2.931
    \end{align*}
    $$
    Under the null hypothesis, this t-statistic follows a t-distribution with n-1 degrees of freedom.

    |T|T-distribution (DoF=49, one-tail, α=0.05)|
    |:----|:----|
    |2.931|1.677|

    Since the t-statistic is larger than t-distribution, I can reject the null hypothesis$H_0$ with 5% error probability. Therefore I conclude that my second hypothesis was accepted, algorithm2 completes tasks _significantly_ faster than algorithm1.