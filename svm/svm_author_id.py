#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
import math
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

#features_train=features_train[:math.floor(len(features_train)/100)]
#labels_train=labels_train[:math.floor(len(labels_train)/100)]



#########################################################
### your code goes here ###
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

#clf=SVC(kernel='linear')
clf=SVC(kernel='rbf',C=10000.0)
t0=time()
clf.fit(features_train,labels_train)
print("Training time: ",round(time()-t0,3),"secs")
t1=time()
pred=clf.predict(features_test)
#pred=clf.predict([features_test[10],features_test[26],features_test[50]])
print("Prediction time: ",round(time()-t1,3),"secs")
#count_chris=0
#for i in pred:
#    if i==1:
#        count_chris+=1
#print(count_chris)
print(accuracy_score(pred,labels_test))


#########################################################


