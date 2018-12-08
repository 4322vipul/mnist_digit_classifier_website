#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 22:03:27 2018

@author: vipul
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as img
from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras.preprocessing.image import ImageDataGenerator
from sklearn.tree import DecisionTreeClassifier
import pickle

def decision_tree_model():
    data=pd.read_csv('mnist_train.csv').as_matrix()
    classifier=DecisionTreeClassifier()

    x_train=data[0:50000,1:]
    train_label=data[0:50000,0]

    classifier.fit(x_train,train_label)
    x_test=data[50000:,1:]
    actual_label=data[50000:,0]

    d=x_test[100]
    d.shape=(28,28)
    plt.imshow(d,cmap='gray')
    plt.show
    return classifier
    

#labels=data[[0]]
#a=data.head(1)
#del a['label']
#c=np.array(a)
#b=c.reshape(28,28)
#plt.imshow(b)

data=pd.read_csv('mnist_train.csv').as_matrix()
classifier_new=decision_tree_model()
x_test=data[50000:,1:]

pickle.dump(classifier_new,open('decision_tree_model.sav','wb'))

print(classifier_new.predict([x_test[100]]))
print(x_test[100].shape)