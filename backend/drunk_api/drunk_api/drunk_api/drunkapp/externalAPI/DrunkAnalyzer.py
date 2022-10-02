#!/usr/bin/env python
# coding: utf-8

import numpy as np
import tensorflow as tf
#import keras.datasets as keras_data

def are_you_drunk(input_json):

    types = ['landmark', 'attributes']
    mask = ['headpose']

    sober_table = []
    drunk_table = []

    affirmative_action = 1

    string_to_int = {'Male' : 0, 'Female' : 1, 'None' : 2}
    # Generates a single row [number1, number2...]
    def format_row_new(set):
        result = []
        for type in types:
            #print("MODULE: " + set)
            for metric in set['faces'][0][type]:
                if isinstance(set['faces'][0][type][metric], dict):
                    for v in set['faces'][0][type][metric]:
                        if isinstance(set['faces'][0][type][metric][v], dict):
                            for w in set['faces'][0][type][metric][v]:
                                # print(type + '_' + metric + '_' + v + '_' + w + " = " + str(set['faces'][0][type][metric][v][w]))
                                adders = set['faces'][0][type][metric][v][w]
                                if (w == "stain"):
                                    afirmative_action *= 0.85 + (set['faces'][0][type][metric][v][w]/100)*0.30
                                if (isinstance(adders, str)):
                                    if (adders in string_to_int):
                                        adders = string_to_int[adders]
                                    else:
                                        adders = -1
                                result.append(adders)
                        else:
                            # print(type + '_' + metric + '_' + v + " = " + str(set['faces'][0][type][metric][v]))
                            adders = set['faces'][0][type][metric][v]
                            if (isinstance(adders, str)):
                                if (adders in string_to_int):
                                    adders = string_to_int[adders]
                                else:
                                    adders = -1
                            result.append(adders)
        return result

    # load the model:
    fancy_model = tf.keras.models.load_model('models/baseline_0.h5')

    # make a prediction:
    #print(np.array(format_row_new(input_json)))
    yhat = fancy_model.predict(np.array([format_row_new(input_json)]))

    return min(yhat[0][0] * affirmative_action, 1)


# print("Is Sober Drunk? --> " + str(are_you_drunk(json.load(open('./test/example_sober_face.json')))))
# print("Is Drunk Drunk? --> " + str(are_you_drunk(json.load(open('./test/example_drunk_face.json')))))
# print("Is Osman Drunk? --> " + str(are_you_drunk(json.load(open('./test/sober_test_osman.json')))))