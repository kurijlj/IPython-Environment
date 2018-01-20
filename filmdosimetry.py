#!/usr/bin/env python
# -*- coding: utf-8 -*-


import numpy as np
# from PIL import Image
from PIL import ImageFilter
from matplotlib import pyplot as plt
from matplotlib.colors import LightSource


def display_objects(objs):
    for ax, title, img, cm in objs:
        ax.cla()
        ax.axis('off')
        ax.imshow(img, cmap=cm)
        ax.set_title(title)


def show_channels(img):
    imgr = np.asarray(img.getchannel('R'))
    imgg = np.asarray(img.getchannel('G'))
    imgb = np.asarray(img.getchannel('B'))
    images = [img, imgr, imgg, imgb]
    titles = ['Source', 'Red', 'Green', 'Blue']
    cmaps = [None, 'gray', 'gray', 'gray']
    fig, axes = plt.subplots(1, 4, figsize=(12.0, 4.0))
    fig.canvas.set_window_title('RGB Color Channels - ' + img.filename)
    objects = zip(axes, titles, images, cmaps)
    display_objects(objects)


def show_topography(img, chnl, blur_radius=0, vert_exag=0.5):
    filtered = None
    if 0 != blur_radius:
        blured = img.filter(ImageFilter.GaussianBlur(blur_radius))
        filtered = np.asarray(blured.getchannel(chnl))
    imgc = np.asarray(img.getchannel(chnl))
    title = 'Unknown'
    if chnl is 'R':
        title = 'Red '
    elif chnl is 'G':
        title = 'Green '
    elif chnl is 'B':
        title = 'Blue '
    else:
        pass
    ls = LightSource(azdeg=45, altdeg=45)
    fig, axes = plt.subplots(1, 2, figsize=(9.0, 4.0))
    fig.canvas.set_window_title(title + ' Channel Topography - ' +
                                img.filename)
    axes[0].axis('off')
    axes[0].set_title(title + ' Channel')
    axes[0].imshow(imgc, cmap='gray')
    axes[1].axis('off')
    axes[1].set_title(title +
                      ' Channel Topography [BR:' +
                      (str(blur_radius) if filtered is not None else 'None') +
                      ', VE:' + str(vert_exag) + ']')
    elevated = ls.shade((filtered if filtered is not None else imgc),
                        cmap=plt.cm.gist_earth,
                        blend_mode='overlay',
                        vert_exag=vert_exag)
    axes[1].imshow(elevated)


def plot_histogram(img, chnl):
    imgc = img.getchannel(chnl)
    hst = np.array(imgc.histogram())
    maxvalindex = np.argmax(hst)
    title = 'Channel Histogram'
    if chnl is 'R':
        title = 'Red ' + title
    elif chnl is 'G':
        title = 'Green ' + title
    elif chnl is 'B':
        title = 'Blue ' + title
    else:
        pass

    # Normalize histogram
    hst = hst / hst[maxvalindex]

    fig, axes = plt.subplots(1, 2, figsize=(9.0, 4.0))
    fig.canvas.set_window_title(title + ' - ' + img.filename)
    axes[0].axis('off')
    axes[0].imshow(np.asarray(imgc), cmap='gray')
    axes[1].axis(xmin=0, xmax=255, ymax=1)
    axes[1].grid('on', linestyle='--')
    axes[1].set_facecolor('#e6e6e6')
    axes[1].bar([x for x in range(hst.size)], hst, width=1.0, color='#297ae5')
