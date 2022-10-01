#!/usr/bin/env python
# coding: utf-8

import sys
import json
import numpy as np
import os
import tensorflow as tf
#import keras.datasets as keras_data

#from sklearn.datasets import load_breast_cancer
#from sklearn.model_selection import train_test_split

sober_set = []
drunk_set = []

sober_path = sys.argv[1] if len(sys.argv) > 1 else ".\\training-json\\sober"
drunk_path = sys.argv[2] if len(sys.argv) > 2 else ".\\training-json\\drunk"

sober_files = os.listdir(sober_path)
drunk_files = os.listdir(drunk_path)

print("\nSOBER FILES\n")
for file in sober_files:
    print("File: " + file)
    x = json.load(open(sober_path + "\\" + file))
    print(x)
    sober_set.append(x)

print("\nDRUNK FILES\n")
for file in drunk_files:
    print("File: " + file)
    x = json.load(open(drunk_path + "\\" + file))
    print(x)
    drunk_set.append(x)


#x, y = load_breast_cancer(return_X_y=True)
#x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=0)

# check otu a sample
#print(x_train.shape)
#print(x_test.shape)
#print(y_train.shape)
#print(y_test.shape)

#print(x_train[5])

#print(x)


