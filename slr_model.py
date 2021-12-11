# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 08:51:25 2021

@author: ssridhar
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 09:04:28 2021

@author: ssridhar
"""
import os
os.getcwd()
# modify the following path to your current working directory
os.chdir('C:\\Users\\Venkat K Pillai\\OneDrive\\Documents\\DSML\\MachineLearning\\FacultyNotes\\demo_slr')
os.getcwd()

import pandas as pd
#import numpy as np
from sklearn import linear_model
#import requests
import pickle

lm = linear_model.LinearRegression()

X = pd.DataFrame({'x':[1,2,3,4,5]})

y = pd.Series([2,3,5,8,11])

lm.fit(X,y)

lm.coef_, lm.intercept_

lm.predict(X)

# save the model to disk
filename = 'demo_slr.pkl'
pickle.dump(lm, open(filename, 'wb')) 
