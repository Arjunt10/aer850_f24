# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 11:22:27 2024

@author: arjun
"""

import pandas as pd
df = pd.read_csv("data/housing.csv")

print(df.columns)

x_columns = ['longitude',
             'latitude',
             'housing_median_age', 
             'total_rooms',
             'total_bedrooms',
             'population',
             'households',
             'median_income',
             'median_house_value',
             'ocean_proximity']

y_column = ['median_house_value']

x = df[x_columns] #input, indpendant variables, predictors
y = df[y_column] #outcome measure, dependant variable