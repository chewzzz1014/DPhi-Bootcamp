# -*- coding: utf-8 -*-
"""Explainable_AI_Solution.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FcQ-m2yrilQWAsypjlWl-l4VbgvENxRo

#Task 1
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv("https://raw.githubusercontent.com/dphi-official/Datasets/master/breast_cancer/Training_set_breastcancer.csv")
df.head()

#EDA
print(df.info())
print("\n\nEmpty values:\n",df.isnull().sum())

#Split the data into Train and Test Sets
le = LabelEncoder()
df["diagnosis"] = le.fit_transform(df["diagnosis"])

train_set = df["diagnosis"].sample(frac = 0.8, random_state=0)
test_set = df["diagnosis"].drop(train_set.index)

train_label = df.drop("id",axis=1)
test_label = df.drop("id",axis=1)

train_label = df.drop("diagnosis",axis=1).sample(frac = 0.8, random_state=0)
test_label = df.drop("diagnosis",axis=1).drop(train_label.index)

#for display purpose later
train_set_disp = df["diagnosis"].sample(frac = 0.8, random_state=0)
test_set_disp = df["diagnosis"].drop(train_set.index)

train_label_disp = df.drop("id",axis=1)
test_label_disp = df.drop("id",axis=1)

train_label_disp = df.drop("diagnosis",axis=1).sample(frac = 0.8, random_state=0)
test_label_disp= df.drop("diagnosis",axis=1).drop(train_label.index)

"""#Task 2"""

#Use Random Forest Machine Learning Model for prediction
train_label = np.array(train_label)
test_label = np.array(test_label)
train = np.array(train_set)
test = np.array(test_set)

#train and predict
rf = RandomForestClassifier(n_estimators=100)
rf.fit(train_label,train)
pred_test = rf.predict(test_label)

#Evaluate the model using Accuracy Score
print("Accuracy Score:", accuracy_score(pred_test, test) )

"""#Task 3"""

!pip install shap

from pandas.compat.numpy import np_datetime64_compat
#Use a SHAP Explainer to derive SHAP Values for the random forest ml model
import shap

explainer = shap.TreeExplainer(rf)

shap_values = explainer.shap_values(test_label)

print('Expected Value:', explainer.expected_value)


shap_values = np.array(shap_values)
shap_values = shap_values.reshape(2*80,31) 
shap_values = shap_values.reshape(-1,31)

pd.DataFrame(shap_values).head()

"""Expected values are 0.62034591 and 0.37965409.

#Task 4
"""

#Plot a SHAP force plot for the first row of test data.
shap.initjs()
shap.force_plot(explainer.expected_value[0], shap_values[0,:], test_label_disp.iloc[0,:])

"""There're 2 expected values and in this force plot the first expected valus is taken account. The number of features that push the prediction higher is almost same as the number of features that push the prediction lower. Features that push the prediction higher include radius_mean, area_mean, perimeter_mean etc., while the features that push the prediction lower include concave_points_mean, concave_points_worst, symmetry_worst etc.

#Task 5
"""

#Plot a SHAP force plot for all the rows of the data
shap.initjs()
shap.force_plot(explainer.expected_value[0], shap_values[:80,:], test_label.iloc[:,:].values,feature_names=test_label.columns)

"""Most of the first 50 test samples probably have higher risk in getting breast cancer and they have lower area_worst and perimeter_worst.

The remaining 50+ test samples probably have lower risk in getting breast cancer and they have higher area_worst and perimeter_worst.

#Task 6
"""

#Plot a SHAP summary plot using all the features in the data
shap.initjs()
shap.summary_plot(shap_values, test_label, plot_type="bar")

"""area_worst impacts the most in determining the diagnosis of breast cancer. Features that follow include perimeter_worst, radius_worst etc.

#Task 7
"""

#Plot a SHAP dependecne plot using all features in the data
shap.initjs()

shap.dependence_plot(ind=test_label.columns.all(), shap_values=shap_values[:len(test_label),:], features = test_label.values, feature_names=test_label.columns)

"""People with lower fractal_dimension_worst and higher symmetry_se have lower risk of breast cancer.

"""