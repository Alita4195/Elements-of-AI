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
### Section 3 Natural language processing(NLP)
Term Frequency-Inverse Document Frequency.<br> 
The logic behind it is it places less weight on frequent words such as on, the, is etc.<br> 

tf−idf=tf×log(1÷df)<br> 
The document frequency of a word is the number of documents that contain at least one occurrence of the word.
### Section 4 Overfitting
leave-one-out cross-validation<br> 
Splitting the data into n different sets, and train the model n times – each time with a different combination of n - 1 sets, with the remaining set being used as a test set. 

## Chapter 4 Neural networks
### Section 1 Logistic regression
First linear function then the results pass through the sigmoid function<br> 
s(z)=1÷(1+exp(−z))<br> 
note: z is input number.<br> 
Application: modeling factors affect voting decisions.Marketing, who will click an ad. <br>
### Section 2 From logistic regression to neural networks
neural network<br>
Input-hidden layer-output
### Section 3 Deep learning
Convolutional neural networks<br>
Recurrent neural networks (RNNs) :feedback loops<br>
Transformer networks
## Chapter 5 Conclusion
### Section 1 Summary
Using AI technology to make a world a better place.<br>
My AI idea<br>
