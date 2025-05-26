# Poland-Bankrupty-Prediction
 recently completed a data analysis and prediction of companies that will go bankrupt in poland.
 
in this project i used libraries from imblearn libraries....for over sampling and under sampling

 sklearn library...for decision trees and random forest classifier models
 
ipywidgets.... for dashboard interactions

pandas.... for data manipulation

 matplotlib and seaborn for visulaizations
 
 numpy for numerical computation.
 
in this project i discovered that i had a very imbalanced dataset about negative class 95% and 5% positive class.
so i leveraged the imblearn libraries of over sampling and under sampling.....the over sampling works in a way it increases the number of the non dominant population till it reaches the number of the dominant data points.

the under sampling method will do just the opposite...it decreases the number of data points in the dominant set until it reaches the same number of data points of the non dominant data points..
Fitting the model...........Decision Trees

the model was fitted into the three sets of data.....the normal dataset.....the over sampled dataset, and the under sampled dataset to see the data set that performs best

after fitting the model, the accuracy score of the datasets shows that the over_sampled dataset has the highest performance with 1.0 accuracy on the training set and 0.95% accuracy on the testing set...

the confusion matrix display was visualized but more needed to be done to get a more accurate prediction...

Randomforestclassifier was used to predict the dataset using the same over_sampled data and the cross_val_score was within the 0.99 range which shows our model with generalize well with unseen data.

GridSearchCV was used for hyper parameter tuning and after that the model prediction power increased significantly after visualizing the confusion matrix

an interactive dashboard was created for tuning of recall and precision depending on the need of the business.
link to the dataset 
