# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 10:23:24 2024

@author: arjun
"""
import numpy as np
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split

df = pd.read_csv("Data/housing.csv")



"""ONE HOT ENCODING"""

my_encoder = OneHotEncoder(sparse_output=False)
my_encoder.fit(df[['ocean_proximity']])
encoded_data = my_encoder.transform(df[['ocean_proximity']])
category_names = my_encoder.get_feature_names_out()

encoded_data_df = pd.DataFrame(encoded_data, columns = category_names)

df = pd.concat([df,encoded_data_df], axis = 1)
df = df.drop(columns = 'ocean_proximity')
"""Define X and y"""

x_columns = ['longitude',
             'latitude',
             'housing_median_age', 
             'total_rooms',
             'total_bedrooms',
             'population',
             'households',
             'median_income',
             'median_house_value',
             'ocean_proximity_<1H OCEAN',
             'ocean_proximity_INLAND',
             'ocean_proximity_ISLAND',
             'ocean_proximity_NEAR BAY',
             'ocean_proximity_NEAR OCEAN'
             ]

y_column = ['median_house_value']
X = df[x_columns] #input, indpendant variables, predictors
y = df[y_column] #outcome measure, dependant variable


"""Train/Test Split"""

#This is the basic random train/test split. 

#X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.2, random_state = 134535)

#Stratified sampling base on income

df["income_categories"] = pd.cut(df['median_income'], bins = [0,2,4,6,np.inf], labels = [1,2,3,4])

my_splitter = StratifedShuffleSplit (n_splits = 1, test_size =0.2, random_state= 36345634)

for train_index, test_indec in my_splitter.split(df, df["income"])