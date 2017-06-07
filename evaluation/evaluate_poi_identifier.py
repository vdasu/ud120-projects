#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "rb") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list, sort_keys = '../tools/python2_lesson14_keys.pkl')
labels, features = targetFeatureSplit(data)

from sklearn.model_selection import train_test_split

features_train,features_test,labels_train,labels_test = train_test_split(features,labels,test_size=0.3,random_state=42)

### your code goes here 

from sklearn.tree import DecisionTreeClassifier as dtc
from sklearn.metrics import accuracy_score,precision_score,recall_score

clf = dtc()
clf.fit(features_train,labels_train)
pred = clf.predict(features_test)
print ("Accuracy score: ",accuracy_score(pred,labels_test))
print ("Number of POI's: ",len([i for i in labels_test if int(i)==1]))
print ("Number of people in test sest: ",len(labels_test))
print ("Actual -> Predicted")
print ("Precision: ",precision_score([int(i) for i in pred],[int(i) for i in labels_test]))
print ("Recall: ",recall_score([int(i) for i in pred],[int(i) for i in labels_test]))

