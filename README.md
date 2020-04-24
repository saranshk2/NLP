Implementation of <Fairness of Exposure in Rankings>

#Summary
<The objective is to develop a framework for formulating fairness constraints on rankings, and then computing the utility-maximizing ranking subject to these fairness constraints. The fairness constraints are : **Dempgraphic Parity, Disparate Treartment and Disparate Impact.**. This is done by linear optimization techniques on two dataets - synthetic **Job-seeker dataset** and real **YOW news recommendation dataset**>



#Requirements
<1.numpy
2.pandas
3.matplotlib
4.pulp
5.BvN [Repo](https://github.com/jfinkels/birkhoff)>


#Results
<All the results are enclosed in juyter notebook itself.
1.optimisation_gender.pynb - Job Seeker 
2.optimisation_real.ipynb - YOW NEWS Recommendation
3.All the ranking matrix without BvN Decomposition - \ranking\
4.All the ranking matrix with BvN Decomposition - \bvn\>
<Results include average DCG-Discounted Cumulative Gain and rankings with BvN Decompositon.>
<Ideal Settings - Run the block where variables and optimisation task are initiated before every fairness constraint code.>


#NOTE
<1. Results can not be replicated completely in *Yow News Recommendation* because of addition of Random Gaussian Noise.
2. To reproduce the results, use the data in the final block of *optimisation_real.ipynb>


##Team Members
<1. Raj Prabhu
2. Saransh Khandelwal
3. Anand Mooga
4. Saket Singh
5.Shivam Choudhary>

