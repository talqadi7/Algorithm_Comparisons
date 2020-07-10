# Emperical Comparison on Supervised Learning Algorithms
Comparison of Supervised Learning Alogrithms in Binary Classification Tasks. The purpose of this project was purely educational. It proved to be extremely useful, as I was allowed to gain an understanding on working optimally across different datasets/models/partitions with a certain pipleline in mind. 

Corresponding paper is available [here](https://uploads-ssl.webflow.com/5dd39100740f6100087d93a4/5e75c9f19105fafd22dcf3b1_COGS118A_Final_Paper%20(1).pdf).

**Contents** :


- [Introduction](#introduction)
    - [Datasets](#dataset)
- [Results](#results)


## Introduction
This project is an emperical comparison on 3 models (Random Forests, Neural Networks, SVM). on a supervised learning task. The following 2 points apply across all 3 of the models: (1) Compare models across 3 different partitions of the data with training data ratios at (0.2/0.5/0.8), and (2) Compare performances of models with 'best' training/test partition at (0.8/0.2) in each dataset with 5-fold cross validation. 5 metrics (F1, Average Precision Rate, Accuracy, Area under Curve, AvgScore) were produced three times for each run, and then averaged out to have a more robust view on the models true performance. **To summarize, 3 different models will be compared across 3 datasets, 3 partitions, and 5 metrics.**

### Datasets
3 Different datasets varying in size and feature type in order to compare the performances of the models across different cases.

**Heart**: This describes diagnosing of cardiac Single Proton Emission Computed Tomography images. The SPECT images [size = 265] are processed into 22 binary features, with 79% of the Y value being positive, this data is heavily imbalanced. Original dataset was in training and test sets, I combined the two and continue with partitioning and then predicting.

**Coverage Type**: Coverage Type dataset represents forest cover type as the dependent variable with 10 quantitative variables, and 44 binary variables. The dataset is originally a multi-class one, but reduced to a binary classification task by taking the top two cover types. Furthermore the original dataset consists of 500k+ instances, the data was shuffled and the first 50,000 instances were used, leading to a balanced dataset with 42.4% of dependent variable being positive.

**BCI Challenge @ NER 2015**: Dataset collected by ’P300-Speller’ paradigm which measures Electroencephalography (EEG) signals at certain points. The goal is to detect errors during the spelling task, given the subject’s EEG values from 56 electrodes every 5 milliseconds. 


## Results
Visit link provided above for full explanation on methods and more visualizations. The final tables used to conclude all my results can be seen below:

![Results](https://i.imgur.com/gi8jEIF.png)
![Results2](https://i.imgur.com/kEAcFjM.png)
