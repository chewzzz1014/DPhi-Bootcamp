# -*- coding: utf-8 -*-
"""dphi-bootcamp-final-assessment.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FBqRRrUSLzmaEGicA_6oevht0HW4tTKi
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

test = pd.read_csv("https://raw.githubusercontent.com/dphi-official/Datasets/master/pharma_data/Testing_set_begs.csv")

train = pd.read_csv("https://raw.githubusercontent.com/dphi-official/Datasets/master/pharma_data/Training_set_begs.csv")

test.info()

train.info()

train.describe()

test.describe()

train.head()

test.head()

categorical_feature = train.select_dtypes(include=object)
numerical_feature = train.select_dtypes(include=np.number)

"""**Data Pre-Processing**"""

def unique_val(df):
    for col in categorical_feature.columns:
        print("Unique Values of {}:{}".format(col, df[col].unique()))
unique_val(train)

# empty values in train set
for col in train.columns:
  print("{} has {} empty values.".format(col, str(train[col].isna().sum()) ))

# drop rows which have empty value in Number_of_prev_cond column
train = train.drop(train[train["Number_of_prev_cond"].isna()].index, axis=0)
train.info()

# encoding categorical values into numerical
from sklearn.preprocessing import LabelEncoder

LE = LabelEncoder()
train["Patient_Smoker"] = LE.fit_transform(train["Patient_Smoker"])  # 0 for NO, 1 for YES and 2 for "Cannot Say"
train["Patient_Rural_Urban"] = LE.fit_transform(train["Patient_Rural_Urban"])  # 0 for RURAL and 1 for URBAN
train["Patient_mental_condition"] = LE.fit_transform(train["Patient_mental_condition"])  # 0 for stable (the only unique value)

test["Patient_Smoker"] = LE.fit_transform(test["Patient_Smoker"])  # 0 for NO, 1 for YES ( does not contain "Cannot Say")
test["Patient_Rural_Urban"] = LE.fit_transform(test["Patient_Rural_Urban"])  # 0 for RURAL and 1 for URBAN
test["Patient_mental_condition"] = LE.fit_transform(test["Patient_mental_condition"])  # 0 for stable (the only unique value)
# train[train["Patient_mental_condition"]!=0] to verify it's true that there's only one unique value

# ID_Patient_Care_Situation doesn't influence the outcome of the target variable 
print("\"ID_Patient_Care_Situation\" has the same number of unique values as number of rows? : {}".format(train["ID_Patient_Care_Situation"].unique().size == train.shape[0]))
# drop column ID_Patient_Care_Situation
train = train.drop("ID_Patient_Care_Situation", axis=1)
test = test.drop("ID_Patient_Care_Situation", axis=1)

# since the unique value of "Patient_mental_condition" in test and train is always stable, drop this column in train
print("Unique value(s) of \"Patient_mental_condition\" in test: {}", format(test["Patient_mental_condition"].unique()) )
train = train.drop("Patient_mental_condition", axis=1)
test = test.drop("Patient_mental_condition", axis=1)

test.head()

train["Patient_Smoker"].value_counts()

# check the survival of "Cannot Say" in "Patient_Smoker" 
print("Did not survived:",train[ (train["Patient_Smoker"]==2) & (train["Survived_1_year"]==0)].size )
print("Survived:",train[ (train["Patient_Smoker"]==2) & (train["Survived_1_year"]==1)].size )

# replace "Cannot Say" with mode (either 0 or 1)
train["Patient_Smoker"].value_counts()  #it's 1
train.loc[train["Patient_Smoker"]==2] = 1

train.head()

sns.countplot(train["Survived_1_year"])

train.head()

test.head()

train = train.drop("Treated_with_drugs", axis=1)
test = test.drop("Treated_with_drugs", axis=1)

X = train.drop(columns = "Survived_1_year")
y = train["Survived_1_year"]

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.33, random_state = 42)

!pip install -U imbalanced-learn

# SMOTE
from imblearn.over_sampling import SMOTE

sm = SMOTE(random_state = 25, sampling_strategy = 1.0) 
X_train, y_train = sm.fit_resample(X_train, y_train)

np.unique(y_train, return_counts=True)

from sklearn.ensemble import RandomForestClassifier
rfc = RandomForestClassifier(criterion='entropy')
rfc.fit(X_train, y_train)

rfc.score(X_test, y_test)

from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier()
model.fit(X_train, y_train)
model.predict(X_test)

from sklearn.metrics import accuracy_score
accuracy_score(model.predict(X_test), y_test)

from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
rfc = RandomForestClassifier()

criterion = ['gini', 'entropy'] 
n_estimators = [100, 200, 300] 
max_features = ['auto', 'sqrt'] 
max_depth = [10, 20] 
max_depth.append(None) 

params = {'criterion': criterion,
'n_estimators': n_estimators,
'max_features': max_features,
'max_depth': max_depth}

gs = GridSearchCV(rfc, param_grid=params, n_jobs=2)
gs.fit(X_train.values, y_train.values)

gs.score(X_test, y_test)

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(test)
x_test = scaler.transform(test)

# using RandomForestClassifier
pred = gs.predict(x_test)

df = pd.DataFrame(pred, columns=["prediction"])
from google.colab import drive
# drive.mount('drive')
df.to_csv("prediction.csv", index=False)
!cp prediction.csv "drive/My Drive/"

df