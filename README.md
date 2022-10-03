# Call me master of business

## Calculate the most efficient way of dealing with enemy in HuBiao events

**Enemy** : [num1, num2, num3, num4, num5] = $Y_{1-5}$

**Ours**: [num1, ... num5] = $X_{1-5}$ 

We want $X_{1-5}$ >= $Y_{1-5}$  by a rule of at three larger number in position wins.

$Y_{1-5}$ is usually known (If we don't fight against others on purpose)

While each number in $X$ is chosen from a list of number $\{x_1, x_2 ,... x_n\}$ .

Our ***Objective*** is to minimize $\sum_{i=1\rightarrow5}X_i$  and make sure $X > Y$ at least at chance of percentage of **95*%***.
