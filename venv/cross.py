import numpy as np

import pandas as pd

import matplotlib.pyplot as plt

import sklearn
from sklearn.preprocessing import StandardScaler

from sklearn.model_selection import train_test_split

from sklearn.metrics import mean_squared_error

from sklearn import model_selection

from sklearn.linear_model import LogisticRegression

from sklearn.model_selection import KFold

from sklearn.model_selection import LeaveOneOut

from sklearn.metrics import accuracy_score
df= pd.read_csv("C:\Users\Ritwik\Downloads\diabetes.csv")
