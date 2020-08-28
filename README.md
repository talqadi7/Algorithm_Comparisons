# Emperical Comparison on Supervised Learning Algorithms
Comparison of Supervised Learning Alogrithms in Binary Classification Tasks. The purpose of this project was purely educational. It proved to be extremely useful, as I learnt the ins and outs of different models. My biggest take away is the idea that no one model is best. When switching from one model to the other, regardless of the domain, it is a give-and-take type situation. 

Corresponding paper is available [here](https://uploads-ssl.webflow.com/5dd39100740f6100087d93a4/5e75c9f19105fafd22dcf3b1_COGS118A_Final_Paper%20(1).pdf).

**Contents** :


- [Introduction](#introduction)
- [Models](#Models)
- [Datasets](#dataset)
- [Results](#results)


## Introduction
This project is an emperical comparison on 3 models (Random Forests, Neural Networks, SVM) on supervised learning tasks. The following 2 points apply across all 3 of the models: (1) Compare models across 3 different partitions of the data with training data ratios at (0.2/0.5/0.8), and (2) Compare performances of models with 'best' training/test partition at (0.8/0.2) in each dataset with 5-fold cross validation. 5 metrics (F1, Average Precision Rate, Accuracy, Area under Curve, AvgScore) were produced three times for each run, and then averaged out to have a more robust view on the models true performance. **To summarize, 3 different models will be compared across 3 datasets, and 3 partitions within them, using 5 metrics.**

## Models
3 different models were tested across different datasets and training/test partitions within them. By using different types and amounts of data, we can start comparing the pros and cons of each model. 5-fold Cross Validation was done using GridSearchCV, and the best set of parameters was manually chosen based on their mean test scores, variance test scores, and runtime.

**Random Forests**: RF is a classification algorithm consisting of decision trees. Itis very robust, trains quickly, and is extremely efficient when compared to other algorithms.

**Support Vector Machines**: SVM is another model used for classification. SVM selects the hyper plane that best separates the classes which is the farthest possible from all the cases.

**Neural Networks**: One of the most widely used Machine Learning algorithms [3]. Can perform extremely well, and has many parameters to tune depending on each case. Neural Networks are best used when optimized specifically to the domain. Because of how different one model can be from others, and to hold an accurate comparison across datasets, all of the following Neural Networks will be simple and built on 2 layers. 

## Datasets
3 Different datasets varying in size and feature type in order to compare the performances of the models across different cases.

![tableinfo](https://imgur.com/XEcIyMI.png)

**Heart**: This describes diagnosing of cardiac Single Proton Emission Computed Tomography images. The SPECT images [size = 265] are processed into 22 binary features, with 79% of the Y value being positive, this data is heavily imbalanced. Original dataset was in training and test sets, I combined the two and continue with partitioning and then predicting.

![Heart](https://i.imgur.com/kH9csFc.png)

**Coverage Type**: Coverage Type dataset represents forest cover type as the dependent variable with 10 quantitative variables, and 44 binary variables. The dataset is originally a multi-class one, but reduced to a binary classification task by taking the top two cover types. Furthermore the original dataset consists of 500k+ instances, the data was shuffled and the first 50,000 instances were used, leading to a balanced dataset with 42.4% of dependent variable being positive.

![Cov_Type](https://i.imgur.com/5oAvZj0.png)

**BCI Challenge @ NER 2015**: Most complicated of the datasets tested on. Dataset collected by ’P300-Speller’ paradigm which measures Electroencephalography (EEG) signals at certain points. The goal is to detect errors during the spelling task, given the subject’s EEG values from 56 electrodes every 5 milliseconds. 

![BCI](https://i.imgur.com/b2s3fbu.png)


## Results
Visit link provided above for full explanation on methods and more visualizations. The final tables used to conclude all my results can be seen below:

![Results](https://i.imgur.com/gi8jEIF.png)
![Results2](https://i.imgur.com/kEAcFjM.png)
