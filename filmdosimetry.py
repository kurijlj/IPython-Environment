#!/usr/bin/env python
# -*- coding: utf-8 -*-


import numpy as np
# from PIL import Image
from PIL import ImageFilter
from matplotlib import pyplot as plt
from matplotlib.colors import LightSource
from mpl_toolkits.mplot3d import Axes3D
from scipy import ndimage
# from skimage import filters


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
    # fig.tight_layout()
    fig.canvas.set_window_title('RGB Color Channels - ' + img.filename)
    objects = zip(axes, titles, images, cmaps)
    display_objects(objects)


def show_topography(img, chnl, br=0, ve=0.5, cm=0):
    cmaps = [plt.cm.nipy_spectral, plt.cm.terrain, plt.cm.gist_earth]
    filtered = None
    if 0 != br:
        blured = img.filter(ImageFilter.GaussianBlur(br))
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
    # fig.tight_layout()
    fig.canvas.set_window_title(title + ' Channel Topography - ' +
                                img.filename)
    axes[0].axis('off')
    axes[0].set_title(title + ' Channel')
    axes[0].imshow(imgc, cmap='gray')
    axes[1].axis('off')
    axes[1].set_title(title +
                      ' Channel Topography [BR:' +
                      (str(br) if filtered is not None else 'None') +
                      ', VE:' + str(ve) + ']')
    elevated = ls.shade((filtered if filtered is not None else imgc),
                        cmap=cmaps[cm],
                        blend_mode='overlay',
                        vert_exag=ve)
    axes[1].imshow(elevated)


def plot_channel_histogram(img, chnl):
    imgc = img.getchannel(chnl)
    hst = np.array(imgc.histogram())
    maxvalindex = np.argmax(hst)
    title = 'Unknown'
    if chnl is 'R':
        title = 'Red '
    elif chnl is 'G':
        title = 'Green '
    elif chnl is 'B':
        title = 'Blue '
    else:
        pass

    # Normalize histogram
    hst = hst / hst[maxvalindex]

    fig, axes = plt.subplots(1, 2, figsize=(9.0, 4.0))
    # fig.tight_layout()
    fig.canvas.set_window_title(title + 'Channel Histogram - ' + img.filename)
    # axes[0].axis('off')
    axes[0].set_title(title + 'Channel')
    axes[0].imshow(np.asarray(imgc), cmap='gray')
    axes[1].set_title('Channel Histogram')
    axes[1].axis(xmin=0, xmax=255, ymax=1)
    axes[1].grid('on', linestyle='--')
    axes[1].set_facecolor('#e6e6e6')
    axes[1].bar([x for x in range(hst.size)], hst, width=1.0, color='#297ae5')


def plot_3d_histogram(img):
    hst = dict()
    c = img.getchannel('R')
    hst['R'] = np.array(c.histogram())
    maxi = np.argmax(hst['R'])
    hst['R'] = hst['R'] / hst['R'][maxi]
    c = img.getchannel('G')
    hst['G'] = np.array(c.histogram())
    maxi = np.argmax(hst['G'])
    hst['G'] = hst['G'] / hst['G'][maxi]
    c = img.getchannel('B')
    hst['B'] = np.array(c.histogram())
    maxi = np.argmax(hst['B'])
    hst['B'] = hst['B'] / hst['B'][maxi]

    fig = plt.figure(figsize=(9.0, 4.0))
    # fig.tight_layout()
    fig.canvas.set_window_title('3D Color Histogram - ' + img.filename)
    axes = []
    axes.append(fig.add_subplot(1, 2, 1))
    axes.append(fig.add_subplot(1, 2, 2, projection='3d'))
    axes[0].axis('off')
    axes[0].set_title('Source Image')
    axes[0].imshow(img)
    axes[1].axis(xmin=0, xmax=255, ymin=0, ymax=4)
    axes[1].bar([x for x in range(hst['R'].size)], hst['R'], zs=1, color='red',
                zdir='y', alpha=0.8, width=1.0)
    axes[1].bar([x for x in range(hst['G'].size)], hst['G'], zs=2,
                color='green', zdir='y', alpha=0.8, width=1.0)
    axes[1].bar([x for x in range(hst['B'].size)], hst['B'], zs=3,
                color='blue', zdir='y', alpha=0.8, width=1.0)
    axes[1].set_yticks([1, 2, 3])
    axes[1].set_title('3D Color Histogram')


def edge_detect(img):
    filt = ndimage.sobel(np.asarray(img))
    fig, axes = plt.subplots(1, 2)
    fig.canvas.set_window_title('Sobel Edge Detect - ' + img.filename)
    # axes[0].axis('off')
    axes[0].set_title('Source Image')
    axes[0].imshow(img)
    # axes[1].axis('off')
    axes[1].set_title('Sobel Edge Detect')
    axes[1].imshow(filt)


def channel_threshold(img, chnl, val):
    return np.asarray(img.getchannel(chnl)) > val


def show_channel_threshold(img, chnl, val):
    data = np.asarray(img.getchannel(chnl))
    mask = data > val
    fig, axes = plt.subplots(1, 2)
    fig.canvas.set_window_title('Threshold - ' + img.filename)
    # axes[0].axis('off')
    axes[0].set_title(chnl + ' Channel')
    axes[0].imshow(data, cmap=plt.cm.gray)
    # axes[1].axis('off')
    axes[1].set_title('Mask')
    axes[1].imshow(mask, cmap=plt.cm.gray)


def smooth1d(x, window_len=11, window='hanning'):
    """Smooth the data using a window with requested size.

    This method is based on the convolution of a scaled window with the signal.
    The signal is prepared by introducing reflected copies of the signal
    (with the window size) in both ends so that transient parts are minimized
    in the begining and end part of the output signal.

    input:
        x:          the input signal
        window_len: the dimension of the smoothing window. Should be an
                    odd integer
        window: the type of window from 'flat', 'hanning', 'hamming',
                'bartlett', 'blackman'. Flat window will produce a moving
                average smoothing

    output:
        the smoothed signal

    example:

    t = linspace(-2, 2, 0.1)
    x = sin(t) + randn(len(t)) * 0.1
    y = smooth(x)

    see also: numpy.hanning, numpy.hamming, numpy.bartlett, numpy.blackman,
              numpy.convolve, scipy.signal.lfilter

    TODO: the window parameter could be the window itself if an array instead
          of a string
    NOTE: length(output) != length(input), to correct this:
          return y[(window_len/2-1):-(window_len/2)] instead of just y.
    """

    if x.ndim != 1:
        raise ValueError('Smooth only accepts 1 dimension arrays.')

    if x.size < window_len:
        raise ValueError('Input vector needs to be bigger than window size.')

    if window_len < 3:
        return x

    if window not in ['flat', 'hanning', 'hamming', 'bartlett', 'blackman']:
        raise ValueError('Window is one of "flat", "hanning", "hamming", ' +
                         '"bartlett", "blackman"')

    s = np.r_[x[window_len-1:0:-1], x, x[-2:-window_len-1:-1]]

    if window == 'flat':  # moving average
        w = np.ones(window_len, 'd')
    else:
        w = eval('np.'+window+'(window_len)')

    y = np.convolve(w / w.sum(), s, mode='valid')
    return y


def plot_chnl_row_profile(img, chnl, row, wl=11, wnd='hanning', pad=0):
    c = np.asarray(img.getchannel(chnl))
    prof = 255 - c[row][pad:c.shape[1] - pad]
    smtd = smooth1d(prof, wl, wnd)
    title = 'Unknown'
    if chnl is 'R':
        title = 'Red '
    elif chnl is 'G':
        title = 'Green '
    elif chnl is 'B':
        title = 'Blue '
    else:
        pass

    fig, axes = plt.subplots(1, 2, figsize=(12, 4))
    fig.canvas.set_window_title(title + ' Channel Row Profile - '
                                + img.filename)
    axes[0].set_title(title + ' Channel')
    # axes[0].imshow(c, cmap=plt.cm.gray,
    #                extent=[0, img.size[0], 0, img.size[1]])
    axes[0].imshow(c, cmap=plt.cm.gray)

    # Draw row position indicator
    axes[0].plot([0, img.size[0] - 2], [row, row], '-', linewidth=0.8,
                 color='green')

    axes[1].set_title('Row Profile [' + str(row) + ']')
    axes[1].plot(prof)
    axes[1].plot(smtd, ':')


def chnl_3d_heat_plot(img, chnl):
    Z = 255 - np.asarray(img.getchannel(chnl))[::1, ::1]
    X, Y = np.mgrid[:Z.shape[0], :Z.shape[1]]
    title = 'Unknown'
    if chnl is 'R':
        title = 'Red '
    elif chnl is 'G':
        title = 'Green '
    elif chnl is 'B':
        title = 'Blue '
    else:
        pass

    fig = plt.figure()
    fig.canvas.set_window_title(title + ' Channel 3D Heat Plot')
    ax = Axes3D(fig)
    ax.view_init(75, 0)
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.cm.nipy_spectral)
    ax.set_title(title + ' Channel 3D Heat Plot')


def plot_channel_heatmap(img, chnl):
    imgc = np.asarray(img.getchannel(chnl))
    heatmap = 255 - np.asarray(img.getchannel(chnl))
    title = 'Unknown'
    if chnl is 'R':
        title = 'Red '
    elif chnl is 'G':
        title = 'Green '
    elif chnl is 'B':
        title = 'Blue '
    else:
        pass

    fig, axes = plt.subplots(1, 2, figsize=(9.0, 4.0))
    fig.canvas.set_window_title(title + 'Channel Heatmap - ' + img.filename)
    axes[0].set_title(title + 'Channel')
    axes[0].imshow(imgc, cmap=plt.cm.gray)
    axes[1].set_title(title + 'Channel Heatmap')
    axes[1].imshow(heatmap, cmap=plt.cm.nipy_spectral)
