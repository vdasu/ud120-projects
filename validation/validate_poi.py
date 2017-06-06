#!/usr/bin/python


"""
    Starter code for the validation mini-project.
    The first step toward building your POI identifier!

    Start by loading/formatting the data

    After that, it's not our code anymore--it's yours!
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "rb") )

### first element is our labels, any added elements are predictor
### features. Keep this the same for the mini-project, but you'll
### have a different feature list when you do the final project.
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list,sort_keys = '../tools/python2_lesson13_keys.pkl')
labels, features = targetFeatureSplit(data)

from sklearn.model_selection import train_test_split

features_train,features_test,labels_train,labels_test = train_test_split(features,labels,test_size=0.3,random_state=42)


### it's all yours from here forward!  

from sklearn.tree import DecisionTreeClassifier as dtc
from sklearn.metrics import accuracy_score

clf = dtc()
clf.fit(features,labels)
pred = clf.predict(features)
print ("Accuracy score before split: ",accuracy_score(pred,labels))
clf_split = dtc()
clf_split.fit(features_train,labels_train)
pred_split = clf_split.predict(features_test)
print ("Accuracy score after split: ",accuracy_score(pred_split,labels_test))

