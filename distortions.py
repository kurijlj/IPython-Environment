#!/usr/bin/env python
# -*- coding: utf-8 -*-


import csv
import numpy as np
from matplotlib import pyplot as plt


row_titles = {'x': 'X-Axis Deviations', 'y': 'Y-Axis Deviations', 'z': 'Z-Axis Deviations', 'r': 'Radial Deviations'}
col_titles = ['Layer 1', 'Layer 2', 'Layer 3', 'Layer 4', 'Layer 5', 'Layer 6']
x_ticks_labels = ['A', 'B', 'C', 'D', 'E', 'F']
y_ticks_labels = ['1', '2', '3', '4', '5', '6', '7']


def import_data(filename=None):
    if filename:
        data = {}
        input_file = open(filename, 'r')
        input_file_reader = csv.reader(input_file)

        x_devs = np.zeros((252))
        y_devs = np.zeros((252))
        z_devs = np.zeros((252))
        rad_devs = np.zeros((252))

        i = 0
        for row in input_file_reader:
            x_devs[i] = row[6]
            y_devs[i] = row[8]
            z_devs[i] = row[10]
            rad_devs[i] = row[12]
            i = i + 1

        data['x'] = x_devs.reshape((6, 7, 6))
        data['y'] = y_devs.reshape((6, 7, 6))
        data['z'] = z_devs.reshape((6, 7, 6))
        data['r'] = rad_devs.reshape((6, 7, 6))

        input_file.close()

        return data


def plot_deviation_map(data=None, title='Deviations Map for \"SEQUENCE\" on \"UNIT\" MRI unit', subtitle='Deviations Map'):
    fig, axes = plt.subplots(1, 6, figsize=(20, 5))
    fig.suptitle(title)
    axes[0].set_ylabel(subtitle)
    for c in range(6):
        axes[c].set_title(col_titles[c])
        axes[c].imshow(data[c,:,:], cmap=plt.cm.coolwarm)
        axes[c].set_xticks(np.arange(6))
        axes[c].set_yticks(np.arange(7))
        axes[c].set_xticklabels(x_ticks_labels)
        axes[c].set_yticklabels(y_ticks_labels)
        for y in range(7):
            for x in range(6):
                text = axes[c].text(x, y, data[c,y,x], ha='center', va='center', color='black')
