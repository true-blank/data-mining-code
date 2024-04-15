import pandas as pd
import numpy as np
from scipy import (stats)
dataset = pd.read_csv('Breast Cancer Wisconsin (Diagnostic) Data Set.csv')
print(dataset.head())
print(dataset.describe())
print((dataset[[1, 2, 3, 4, 5]] == 0).sum())
dataset[[1, 2, 3, 4, 5]] = dataset[[1, 2, 3, 4, 5]].replace(0, np.NaN)
print(dataset.isnull().sum())
dataset.fillna(dataset.mean(), inplace=True)
print(dataset.isnull().sum())
dataset[[1, 2, 3, 4, 5]] = dataset[[1, 2, 3, 4, 5]].replace(0, np.NaN)
dataset.fillna(dataset.median(), inplace=True)
print(dataset.isnull().sum())
lst_nums = [2, 5, 7, 11, 13, 17, 23, 31, 37, 41, 43, 47]
ary_nums = np.array(lst_nums)
mean_nums = ary_nums.mean()
print(mean_nums)
arr = np.array([1, 4, 2, 8, 5, 7])
median = np.me
