# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 11:15:16 2024

@author: arjun
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


data = {
        'A': [1, 2, 3, 4, 5],
        'B': [10, 20, 30, 40, 50],
        'C': [100, 200, 300, 400, 500]
        
        }

df = pd.DataFrame(data)

array = df.to_numpy()

result = np.square(array)

df['D'] =  np.sqrt(df['C'])

print("here are sqrt results for df['C']\n")
print (df['D'])

plt.plot(df['A'], df['D'])

