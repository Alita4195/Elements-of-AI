# Elements-of-AI
Solving the test in the courses.<br>
## Chapter 1 Getting started with AI
### Section 1<br>
Factorial e.g. 4 * 3 * 2=24<br>
By going through all the possible routes and find the most optimized one. This is using "brute-force". When the number of solutions grow large, then we need smarter techniques.<br>
### Section 2<br>
we can find local summit or local optima, but we aim for global optimum.<br>
Greedy solutions/simulated annealing<br>
prob = exp(-(S_old - S_new)/T)<br>
As (S_old - S_new)/T increases, the probability is degreasing. 
## Chapter 2 Dealing with uncertainty
### Section 1 Conditional probabilities
### Section 2 Bayes Rule
🧠
P(A∣B)= P(B∣A)*P(A)/P(B)

P(A | B) — the posterior: probability of A given B<br>
P(B | A) — the likelihood: probability of B given A<br>
P(A) — the prior: how likely A is before seeing any data<br>
P(B) — the evidence: how likely B is overall<br>
### Section 3 Naive Bayes classifier
likelyhood ratio r=P(word ∣ spam)÷P(word ∣ ham)<br>
if odds=x:y,the probability=x÷(x+y)
Posterior Odds=Prior Odds×Likelihood Ratio
​
## Chapter 3 Machine learning
### Section 1 Linear regression
Least Squares Method<br>
### Section 2 The nearest neighbor method
```
D = math.sqrt((x_hel - x_ny)**2 + (y_hel - y_ny)**2)
```





