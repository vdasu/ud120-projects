#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import _pickle as pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "rb"))

print(len(enron_data))

print(len(enron_data["SKILLING JEFFREY K"]))

count_poi=0
for i in enron_data:
    if enron_data[i]["poi"]==1:
        count_poi+=1

print (count_poi)

print (enron_data["PRENTICE JAMES"]["total_stock_value"])

print (enron_data["COLWELL WESLEY"]["from_this_person_to_poi"])

print (enron_data["SKILLING JEFFREY K"]["exercised_stock_options"])

print ("KENNETH LAY: ",enron_data["LAY KENNETH L"]["total_payments"],"JEFFREY SKILLING: ",enron_data["SKILLING JEFFREY K"]["total_payments"],"ANDREW FASTOW: ",enron_data["FASTOW ANDREW S"]["total_payments"])

count_quant_salary=0
count_email_address=0

for i in enron_data:
    if enron_data[i]["email_address"]!="NaN":
        count_email_address+=1
    if enron_data[i]["salary"]!="NaN":
        count_quant_salary+=1

print (count_quant_salary)

print (count_email_address)

count_nan_payments=0

for i in enron_data:
    if enron_data[i]["total_payments"]=="NaN":
        count_nan_payments+=1

print (count_nan_payments/len(enron_data))

count_poi_nan_payments=0

for i in enron_data:
    if enron_data[i]["poi"]==True:
        if enron_data[i]["total_payments"]=="NaN":
            count_poi_nan_payments+=1

print (count_poi_nan_payments/count_poi)
