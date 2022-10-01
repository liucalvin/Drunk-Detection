#!/usr/bin/env python
# coding: utf-8

import random
import sys
import json
import numpy as np
import os
import pandas as pd
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from scikeras.wrappers import KerasClassifier
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import StratifiedKFold
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
#import keras.datasets as keras_data

#from sklearn.datasets import load_breast_cancer
#from sklearn.model_selection import train_test_split

sober_set = []
drunk_set = []

sober_path = sys.argv[1] if len(sys.argv) > 1 else "./training-json/sober"
drunk_path = sys.argv[2] if len(sys.argv) > 2 else "./training-json/drunk"

sober_files = os.listdir(sober_path)
drunk_files = os.listdir(drunk_path)

#print("\nSOBER FILES\n")
for file in sober_files:
    #print("File: " + file)
    x = json.load(open(sober_path + "/" + file))
    #print(x)
    sober_set.append(x)

#print("\nDRUNK FILES\n")
for file in drunk_files:
    #print("File: " + file)
    x = json.load(open(drunk_path + "/" + file))
    #print(x)
    drunk_set.append(x)

# x is an array of input data
# y is an array of output integers (ie 0 = sober or 1 = drunk)

types = ['landmark', 'attributes']
mask = ['headpose']

sober_table = []
drunk_table = []

# Generates a single row {metric = number, metric2 = number2...}
def format_row(set):
    result = {}
    for type in types:
        for metric in set['faces'][0][type]:
            if isinstance(set['faces'][0][type][metric], dict):
                for v in set['faces'][0][type][metric]:
                    if isinstance(set['faces'][0][type][metric][v], dict):
                        for w in set['faces'][0][type][metric][v]:
                            #print(type + '_' + metric + '_' + v + '_' + w + " = " + str(set['faces'][0][type][metric][v][w]))
                            result[type + '_' + metric + '_' + v + '_' + w] = set['faces'][0][type][metric][v][w]
                    else:
                        #print(type + '_' + metric + '_' + v + " = " + str(set['faces'][0][type][metric][v]))
                        result[type + '_' + metric + '_' + v] = set['faces'][0][type][metric][v]
    return result

# Generates a single row [number1, number2...]
def format_row_new(set):
    result = []
    for type in types:
        for metric in set['faces'][0][type]:
            if isinstance(set['faces'][0][type][metric], dict):
                for v in set['faces'][0][type][metric]:
                    if isinstance(set['faces'][0][type][metric][v], dict):
                        for w in set['faces'][0][type][metric][v]:
                            #print(type + '_' + metric + '_' + v + '_' + w + " = " + str(set['faces'][0][type][metric][v][w]))
                            result.append(set['faces'][0][type][metric][v][w])
                    else:
                        #print(type + '_' + metric + '_' + v + " = " + str(set['faces'][0][type][metric][v]))
                        result.append(set['faces'][0][type][metric][v])
    return result

# sober_set = [{person 1}, {person 2}, {person 3}]
# set = {person}
# Format the sets properly into tables
for set in drunk_set:
    drunk_table.append(format_row_new(set))
    
for set in sober_set:
    sober_table.append(format_row_new(set))

#print(drunk_table)   
#print(sober_table)

#print(drunk_set[0]['faces'][0]['landmark'])

x = []
y = []
si = 0
di = 0
for i in range(0, len(sober_table) + len(drunk_table)):
    drunk = bool(random.getrandbits(1))
    if (si >= len(sober_table)):
        drunk = True
    if (di >= len(drunk_table)):
        drunk = False
    if (di < len(sober_table) or si < len(drunk_table)):
        if drunk:
            x.append(drunk_table[di])
            y.append(1)
            di+=1
        else:
            x.append(sober_table[si])
            y.append(0)
            si+=1

#x, y = load_breast_cancer(return_X_y=True)

# x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=0)

# Baseline Model
def create_baseline():
    print("Creating Baseline Model")
    model = Sequential()
    model.add(Dense(len(sober_table[0]), input_shape=(len(sober_table[0]),), activation='relu'))
    model.add(Dense(1, activation='sigmoid'))
    # Compile Model
    print("Compiling Baseline Model")
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    print("Compiled Baseline Model")
    return model

# evaluate model with standardized dataset
def evaluate_model():
    print("Evaluating Baseline Model")
    estimator = KerasClassifier(model=create_baseline(), epochs=100, batch_size=5, verbose=0)
    print("Created Estimator")
    kfold = StratifiedKFold(n_splits=2, shuffle=True)
    print("Created kfold")
    results = cross_val_score(estimator, x, y, cv=kfold)
    print("Created results")
    print("Baseline: %.2f%% (%.2f%%)" % (results.mean()*100, results.std()*100))

x = np.array(x).reshape(-1, 1)
y = np.array(y)

evaluate_model()

# check otu a sample
#print(x_train.shape)
#print(x_test.shape)
#print(y_train.shape)
#print(y_test.shape)

#print(x_train[5])

#print(x)


