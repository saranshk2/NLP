# Implementation of Fairness of Exposure in Rankings #

# Summary #

The objective is to develop a framework for formulating fairness constraints on rankings, and then computing the utility-maximizing ranking subject to these fairness constraints. The fairness constraints are : **Demographic Parity, Disparate Treartment and Disparate Impact.**. This is done by linear optimization using *pulp* on two dataets - synthetic **Job-seeker dataset** and real **YOW news recommendation dataset**



# Requirements #

1. pulp
2. pandas
3. matplotlib
4. numpy
5. BvN [Repo](https://github.com/jfinkels/birkhoff)


# Results #

All the results are enclosed in jupyter notebook itself.
1. Job Seeker - _**optimisation_gender.ipynb**_ 
2. YOW NEWS Recommendation -  _**optimisation_real.ipynb**_ 
3. Path for all the ranking matrix without BvN Decomposition - \ranking\
4. Path for all the ranking matrix with BvN Decomposition - \bvn\
Results include average DCG-Discounted Cumulative Gain and rankings with BvN Decompositon.


# NOTE #
1. Ideal Settings - Run the block where variables and optimisation task are initiated before every fairness constraint code.
2. Results can not be replicated completely in *Yow News Recommendation* because of addition of Random Gaussian Noise.
3. To reproduce the results, use the data in the final block of *optimisation_real.ipynb*.


## Team Members ##

1. Raj Prabhu
2. Saransh Khandelwal
3. Anand Mooga
4. Saket Singh
5. Shivam Choudhary

