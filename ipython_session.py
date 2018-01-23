# IPython log file

get_ipython().run_line_magic('logstart', './ipython_session.py')
get_ipython().run_line_magic('matplotlib', '')
get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')
from matplotlib import pyplot as plt
from nmrgraphs import *
fig1, ax1 = plt.subplots()
t1_relax_graph(ax1, 8, 1, 1, 2)
ax1.cla()
ytl = list()
for item in ax1.get_yticklabels():
    text = item.get_text()
    if '\u22121.00' == text:
        text = r'$-M_0$'
    elif '1.00' == text:
        text = r'$M_0$'
    else:
        text = r''
    ytl.append(text)
ax1.set_yticklabels(ytl)
quit()
get_ipython().run_line_magic('logstart', './ipython_session.py append')
get_ipython().run_line_magic('matplotlib', '')
get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')
from matplotlib import pyplot as plt
from nmrgraphs import *
fig1, ax1 = plt.subplots()
t1_relax_graph(ax1, 8, 1, 1, 2)
quit()
get_ipython().run_line_magic('logstart', './ipython_session.py append')
get_ipython().run_line_magic('matplotlib', '')
get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')
from matplotlib import pyplot as plt
from nmrgraphs import *
fig1, ax1 = plt.subplots()
t1_relax_graph(ax1, 8, 1, 1, 2)
get_ipython().run_line_magic('clear', '')
t1_relax_graph(ax1, 8, 1, 1, 2)
for item in ax1.get_xticklabels():
    print(item.get_text())
    print(item.get_position())
    
for item in ax1.get_yticklabels():
    print(item.get_text())
    print(item.get_position())
    
ax1.cla()
t2_relax_plot(ax1, 8.0, 1.5, 5.0, 0.4, 3.0)
ax1.cla()
quit()
get_ipython().run_line_magic('logstart', './ipython_session.py append')
get_ipython().run_line_magic('matplotlib', '')
get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')
from matplotlib import pyplot as plt
from nmrgraphs import *
fig1, ax1 = plt.subplots()
gradient_field_plot(ax1, 4.0, 0.25, 2)
ax1.cla()
quit()
get_ipython().run_line_magic('logstart', './ipython_session.py append')
get_ipython().run_line_magic('matplotlib', '')
get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')
get_ipython().run_line_magic('logstart', './ipython_session.py append')
get_ipython().run_line_magic('matplotlib', '')
get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')
from matplotlib import pyplot as plt
import dicomparser
import dicomparser
import dicomparser
import dicomparser
img = dicomparser.DicomParser('./IMG-0001-00001.dcm')
img = dicomparser.DicomParser('./IMG-0001-00001.dcm')
fig, ax = plt.subplots(num="MRI_demo")
ax.imshow(img.GetImage(), cmap=cm.gray)
ax.imshow(img.GetImage(), cmap=cm.gray)
import matplotlib.cm as cm
ax.imshow(img.GetImage(), cmap=cm.gray)
ax.cla()
img = dicomparser.DicomParser('./IMG-0002-00001.dcm')
ax.imshow(img.GetImage(), cmap=cm.gray)
quit()
get_ipython().run_line_magic('logstart', './ipython_session.py append')
get_ipython().run_line_magic('matplotlib', '')
get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')
from matplotlib import pyplot as plt
import matplotlib.cm as cm
import dicomparser
prsr = dicomparser.DicomParser('IMG-0001-00001.dcm')
prsr.GetStudyInfo()
prsr.GetSeriesInfo()
prsr.GetDemographics()
prsr.GetImageData()
prsr.GetImageLocation()
prsr.GetNumberOfFrames()
prsr.GetSOPClassUID()
prsr2 = dicomparser.DicomParser('OT-MONO2-8-a7.gz')
prsr2 = dicomparser.DicomParser('OT-MONO2-8-a7')
prsr.GetSOPClassUID()
prsr2.GetSOPClassUID()
prsr.GetSOPClassUID()
prsr2.GetNumberOfFrames()
prsr2.GetImageData()
fig1, ax1 = plt.subplot()
fig1, ax1 = plt.subplots()
ax.imshow(prsr2.GetImage(), cmap=cm.gray)
ax1.imshow(prsr2.GetImage(), cmap=cm.gray)
quit()
get_ipython().run_line_magic('logstart', './ipython_session.py append')
get_ipython().run_line_magic('matplotlib', '')
get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')
get_ipython().run_line_magic('clear', '')
from matplotlib import pyplot as plt
import matplotlib.patches as ptchs
import matplotlib.cm as cm
from enum import Enum
class PatientSex(Enum):
    other = 'o'
    male = 'm'
    female = 'f'
fig1, ax1 = plt.subplots()
plt.axis('off')
ax1.add_patch(ptchs.FancyBboxPatch((0.25, 0.15), 0.5, 0.7, boxstyle=ptchs.BoxStyle("Round", pad=0.02, rounding_size=0.04), fc='#3f8cc6', ec='#3f48c6', zorder=0))
ax1.add_patch(ptchs.FancyBboxPatch((0.3, 0.2), 0.4, 0.6, boxstyle=ptchs.BoxStyle("Round", pad=0.02, rounding_size=0.04), fc='#3fb4c6', ec='#3f71c6', zorder=1))
ax1.add_patch(ptchs.Ellipse((0.5, 0.5), 0.35, 0.5, fc='#c66780', ec='#c67d67', ls='dotted', zorder=2))
ax1.add_patch(ptchs.Ellipse((0.5, 0.5), 0.25, 0.38, fc='#c63f63', ec='#c65f3f', ls='dashed', zorder=3))
ax1.add_patch(ptchs.Ellipse((0.5, 0.5), 0.15, 0.26, fc='#c61746', ec='#c64017', zorder=4))
ax1.text(0.5, 0.15, u'ozračeni volumen', size='large', horizontalalignment='center')
ax1.text(0.5, 0.2, u'tretirani volumen', size='large', horizontalalignment='center')
ax1.text(0.5, 0.27, u'PTV', size='large', horizontalalignment='center')
ax1.text(0.5, 0.34, u'CTV', size='large', horizontalalignment='center')
ax1.text(0.5, 0.5, u'GTV', size='large', horizontalalignment='center')
quit()
get_ipython().run_line_magic('logstart', './ipython_session.py append')
get_ipython().run_line_magic('matplotlib', '')
get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')
get_ipython().run_line_magic('clear', '')
from matplotlib import pyplot as plt
import matplotlib.cm as cm
from nmrgraphs import gtvctvptv_plot
fig1, ax1 = plt.subplots()
plt.axis('off')
gtvctvptv_plot(ax1)
ax1.text(0.5, 0.5, u'GTV', size='large', horizontalalignment='center', zorder=5)
ax1.cla()
quit()
get_ipython().run_line_magic('logstart', './ipython_session.py append')
get_ipython().run_line_magic('matplotlib', '')
get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')
get_ipython().run_line_magic('clear', '')
from matplotlib import pyplot as plt
import matplotlib.cm as cm
import nmrgraphs
fig, (ax1, ax2) = plt.subplots(1, 2, squeeze=True, num="MRI Distortion Demo")
ax1.axis('off')
ax2.axis('off')
gn = plt.imread('./IMG-0001-00001.jpg')
dst = plt.imread('./IMG-0002-00001.jpg')
ax1.imshow(gn)
ax2.imshow(dst)
quit()
get_ipython().run_line_magic('logstart', './ipython_session.py append')
get_ipython().run_line_magic('matplotlib', '')
get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')
get_ipython().run_line_magic('clear', '')
from matplotlib import pyplot as plt
import matplotlib.cm as cm
import nmrgraphs
fig, (ax1, ax2) = plt.subplots(2, 1, squeeze=True, num="MRI Distortion Demo")
im1 = plt.imread('./MRI Distortion 001.png')
im2 = plt.imread('./MRI Distortion 003.png')
ax1.axis('off')
ax2.axis('off')
ax1.imshow(im1)
ax2.imshow(im2)
quit()
get_ipython().run_line_magic('logstart', './ipython_session.py append')
get_ipython().run_line_magic('matplotlib', '')
get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')
get_ipython().run_line_magic('cls', '')
from matplotlib import pyplot as plt
import matplotlib.cm as cm
import nmrgraphs
fig, (ax1, ax2) = plt.subplots(1, 2, squeeze=True, num="GK Units")
im1 = plt.imread('./LGKP-017.jpg.jpg')
im2 = plt.imread('./Leksell-Gamma-Knife-Icon-0.png')
ax1.imshow(im1)
ax2.imshow(im2)
ax1.axis('off')
ax2.axis('off')
quit()
get_ipython().run_line_magic('logstart', './ipython_session.py append')
get_ipython().run_line_magic('matplotlib', '')
get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')
get_ipython().run_line_magic('cls', '')
from matplotlib import pyplot as plt
import matplotlib.cm as cm
import nmrgraphs
fig, (ax1, ax2) = plt.subplots(1, 2, squeeze=True, num="GK Imobilization")
im1 = plt.imread('./Thermoplastic_mask.jpg')
im1 = plt.imread('./125124.jpg')
ax1.imshow(im1)
ax2.imshow(im2)
im1 = plt.imread('./Thermoplastic_mask.jpg')
im2 = plt.imread('./125124.jpg')
ax1.imshow(im1)
ax2.imshow(im2)
ax1.axis('off')
ax2.axis('off')
quit()
get_ipython().run_line_magic('logstart', './ipython_session.py append')
get_ipython().run_line_magic('matplotlib', '')
get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')
get_ipython().run_line_magic('clear', '')
import filmdosimetry as fd
from matplotlib import pyplot as plt
img = fd.open_image('/home/ljubak/Downloads/KCS GK profile [XZ 20160327].jpg')
imgG = fd.image_channel(img, fd.RGB.green)
fig, axes = plt.subplots(1, 2, num='RGB - Extracting Color Channels')
axes[0].axis('off')
axes[1].axis('off')
axes[0].imshow(img)
axes[1].imshow(imgG, cmap='Greys')
quit()
get_ipython().run_line_magic('logstart', './ipython_session.py append')
get_ipython().run_line_magic('matplotlib', '')
get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')
get_ipython().run_line_magic('clear', '')
from matplotlib import pyplot as plt
import matplotlib.image as mpimg
import numpy as np
fig, axes = plt.subplots(1, 2, num='RGB - Extracting Color Channels')
axes[0].axis('off')
axes[1].axis('off')
image = mpimg.imread('/home/ljubak/Downloads/KCS GK profile [XZ 20160327].jpg')
image_G = 255 - image[:,:,0]
axes[0].imshow(image)
axes[1].imshow(image_G, cmap='Greys')
image_G = 255 - image[:,:,1]
axes[1].imshow(image_G, cmap='Greys')
image_G = 255 - image[:,:,2]
axes[1].imshow(image_G, cmap='Greys')
get_ipython().run_line_magic('logstart', './ipython_session.py append')
get_ipython().run_line_magic('matplotlib', '')
get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')
get_ipython().run_line_magic('clear', '')
from PIL import Image
from matplotlib import pyplot as plt
import numpy as np
import filmdosimetry as fd
image = Image.open('/home/ljubak/Downloads/KCS GK profile [XZ 20160327].jpg')
red = image.getchannel('R')
green = image.getchannel('G')
blue = image.getchannel('B')
images = [image, np.asarray(red), np.asarray(green), np.asarray(blue)]
titles = ['Original', 'Red Channel', 'Green Channel', 'Blue Channel']
cmaps = [None, 'gray', 'gray', 'gray']
fig, axes = plt.subplots(1, 4, num='Image Color Bands')
objects = zip(axes, titles, images, cmaps)
fd.display_objects(objects)
quit()
get_ipython().run_line_magic('logstart', './ipython_session.py append')
get_ipython().run_line_magic('matplotlib', '')
get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')
get_ipython().run_line_magic('clear', '')
from PIL import Image
from matplotlib import pyplot as plt
import numpy as np
import filmdosimetry
image = Image.open('/home/ljubak/Downloads/KCS GK profile [XZ 20160327].jpg')
green = image.getchannel('G')
greenhist = np.array(green.histogram())
np.argmax(greenhist)
greenhist / greenhist[149]
len(green.histogram())
[i for i in range(len(green.histogram()))]
fig, axes = plt.subplots(1, 2, num='Green Channel Histogram')
axes[0].axis('off')
axes[1].axis('off')
axes[0].imshow(green, cmap='gray')
axes[1].bar([x for x in range(256)], greenhist / greenhist[149], width=1.0)
quit()
get_ipython().run_line_magic('logstart', './ipython_session.py append')
get_ipython().run_line_magic('matplotlib', '')
get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')
get_ipython().run_line_magic('clear', '')
from PIL import Image
from matplotlib import pyplot as plt
import numpy as np
import filmdosimetry as fd
image = Image.open('/home/ljubak/Downloads/KCS GK profile [XZ 20160327].jpg')
fd.show_channels(image)
fd.plot_histogram(image, 'G')
fd.show_topography(image, 'R', blur_radius=5, vert_exag=0.7)
fd.show_topography(image, 'R', vert_exag=10)
quit()
get_ipython().run_line_magic('logstart', './ipython_session.py append')
get_ipython().run_line_magic('matplotlib', '')
get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')
get_ipython().run_line_magic('clear', '')
from PIL import Image
from matplotlib import pyplot as plt
import numpy as np
import filmdosimetry as fd
from mpl_toolkits.mplot3d import Axes3D
image = Image.open('/home/ljubak/Downloads/KCS GK profile [XZ 20160327].jpg')
red = image.getchannel('R')
redh = np.array(red.histogram())
redmaxi = np.argmax(redh)
green = image.getchannel('G')
greenh = np.array(green.histogram())
greenmaxi = np.argmax(greenh)
blue = image.getchannel('B')
blueh = np.array(blue.histogram())
bluemaxi = np.argmax(blueh)
redh = rehd / redh[redmaxi]
redh = redh / redh[redmaxi]
greenh = greenh / greenh[greenmaxi]
blueh = blueh / blueh[bluemaxi]
fig = plt.figure(figsize=(9.0, 4.0))
axes = []
axes.append(fig.add_subplot(1, 2, 1))
axes.append(fig.add_subplot(1, 2, 2, projection='3d'))
axes[0].axis('off')
fig.canvas.set_window_title('3D Color Histogram - ' + image.filename)
axes[0].imshow(image)
axes[0].set_title('Source Image')
axes[1].axis(xmin=0, xmax=255, ymin=0, ymax=4)
axes[1].bar([x for x in range(redh.size)], redh, zs=1, color='red', zdir='y', alpha=0.8, width=1.0)
axes[1].bar([x for x in range(greenh.size)], greenh, zs=2, color='green', zdir='y', alpha=0.8, width=1.0)
axes[1].bar([x for x in range(blueh.size)], blueh, zs=3, color='blue', zdir='y', alpha=0.8, width=1.0)
axes[1].set_yticks([1, 2, 3])
axes[1].set_title('3D Color Histogram')
quit()
get_ipython().run_line_magic('logstart', './ipython_session.py append')
get_ipython().run_line_magic('matplotlib', '')
get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')
get_ipython().run_line_magic('clear', '')
from PIL import Image
from matplotlib import pyplot as plt
import numpy as np
import filmdosimetry as fd
image = Image.open('/home/ljubak/Downloads/KCS GK profile [XZ 20160327].jpg')
fd.plot_3d_histogram(image)
quit()
get_ipython().run_line_magic('logstart', './ipython_session.py append')
get_ipython().run_line_magic('matplotlib', '')
get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')
get_ipython().run_line_magic('clear', '')
from PIL import Image
from matplotlib import pyplot as plt
import numpy as np
import filmdosimetry as fd
image = Image.open('/home/ljubak/Downloads/KCS GK profile [XZ 20160327].jpg')
fd.plot_3d_histogram(image)
fd.show_channels()
fd.show_channels(image)
fd.show_topography(image, 'R', blur_radius=3, vert_exag=0.7)
fd.plot_channel_histogram(image, 'G')
quit()
get_ipython().run_line_magic('logstart', './ipython_session.py append')
get_ipython().run_line_magic('matplotlib', '')
get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')
get_ipython().run_line_magic('clear', '')
from PIL import Image
from matplotlib import pyplot as plt
import numpy as np
import filmdosimetry as fd
image = Image.open('/home/ljubak/Downloads/KCS GK profile [XZ 20160327].jpg')
fd.edge_detect(image)
quit()
get_ipython().run_line_magic('logstart', './ipython_session.py append')
get_ipython().run_line_magic('matplotlib', '')
get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')
get_ipython().run_line_magic('clear', '')
from PIL import Image
from matplotlib import pyplot as plt
import numpy as np
import filmdosimetry as fd
image = Image.open('/home/ljubak/Downloads/KCS GK profile [XZ 20160327].jpg')
from skimage import measure
rarr = np.asarray(image.getchannel('R'))
cntrs = measure.find_contours(rarr, 0.8)
fig = plt.figure(figsize=(4, 6))
ax = fig.add_subplot(1, 1, 1)
ax.imshow(rarr, cmap=plt.cm.gray)
for n, cnt in enumerate(cntrs):
    ax.plot(contour[:, 1], contour[:, 0], linewidth=1)
    
for n, cnt in enumerate(cntrs):
    ax.plot(cnt[:, 1], cnt[:, 0], linewidth=1)
    
    
cntrs = measure.find_contours(rarr, 0.1)
for n, cnt in enumerate(cntrs):
    ax.plot(cnt[:, 1], cnt[:, 0], linewidth=1)
    
cntrs = measure.find_contours(rarr, 5.0)
for n, cnt in enumerate(cntrs):
    ax.plot(cnt[:, 1], cnt[:, 0], linewidth=1)
    
fd.plot_channel_histogram('R')
fd.plot_channel_histogram(image, 'R')
cntrs = measure.find_contours(rarr, 150.0)
for n, cnt in enumerate(cntrs):
    ax.plot(cnt[:, 1], cnt[:, 0], linewidth=1)
    
fd.channel_threshold(image, 'R', 150)
fd.channel_threshold(image, 'R', 150)
fd.channel_threshold(image, 'R', 15)
fd.channel_threshold(image, 'R', 100)
fd.plot_channel_histogram(image, 'R')
fd.show_channel_threshold(image, 'R', 35)
fd.show_channel_threshold(image, 'R', 40)
green = np.asarray(image.getchannel('G'))
green
fd.plot_channel_histogram(image, 'G')
len(green)
green[586]
fig = plt.figure()
ax = fig.add_subplot()
ax.plot(255 - green[586])
ax = fig.add_subplot(1, 1, 1)
ax.plot(255 - green[586])
ax.plot(255 - green[586][50:103])
ax.plot(255 - green[586][50:890])
from scipy import interpolate as intpol
spline = intpol.interp1d([x for x in range(890-50)], 255 - green[586][50:890], kind='cubic')
ax.plot(spline, '--'))
ax.plot(spline, '--')
x = [x for x in range(890-50)]
spline = intpol.interp1d(x, 255 - green[586][50:890], kind='cubic')
ax.plot(spline(x), '--')
ax.cla()
ax.plot(255 - green[586][50:890])
spline = intpol.BarycentricInterpolator(x, 255 - green[586][50:890])
spline = intpol.KroghInterpolator(x, 255 - green[586][50:890])
ax.plot(spline(x))
ax.plot(spline)
ax.cla()
ax.plot(255 - green[586][50:890])
spline = intpol.CubicSpline(x, 255 - green[586][50:890])
ax.plot(spline(x))
ax.cla()
ax.plot(255 - green[586][50:890])
ax.plot(spline(x), '--')
ax.plot(fd.smooth(255 - green[586][50:890]), ':')
ax.cla()
ax.plot(255 - green[586][50:890])
ax.plot(fd.smooth(255 - green[586][50:890]), ':')
ax.plot(fd.smooth(255 - green[586][50:890], window_len=20), '--')
ax.plot(fd.smooth(255 - green[586][50:890], window_len=30), '-.')
230-106
230-62
255-168
fd.show_channel_threshold(image, 'R', 62)
green.dim()
green.dim
np.dim(green)
dir(green)
green.size()
green.size
green.ndim()
green.ndim
green.shape()
green.shape
fd.plot_chnl_row_profile(image, 'R', 585, pad=60)
fd.plot_chnl_row_profile(image, 'R', 585, pad=60)
fd.plot_chnl_row_profile(image, 'R', 585, pad=60)
fd.plot_chnl_row_profile(image, 'R', 585, pad=60)
fd.plot_chnl_row_profile(image, 'R', 585, pad=60)
fd.plot_chnl_row_profile(image, 'R', 585, pad=60, wnd='hamming')
fd.plot_chnl_row_profile(image, 'R', 585, pad=60, wnd='bartlett')
fd.plot_chnl_row_profile(image, 'R', 585, pad=60, wnd='bartlett', wl=20)
fd.plot_chnl_row_profile(image, 'R', 585, pad=60, wnd='blackman', wl=20)
fd.plot_chnl_row_profile(image, 'R', 585, pad=60, wnd='blackman', wl=20)
quit()
get_ipython().run_line_magic('logstart', './ipython_session.py append')
get_ipython().run_line_magic('matplotlib', '')
get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')
get_ipython().run_line_magic('clear', '')
from PIL import Image
from matplotlib import pyplot as plt
import numpy as np
import filmdosimetry as fd
image = Image.open('/home/ljubak/Downloads/KCS GK E2E Patient QA 002 [fractionated XZ 20180116].tif')
fd.show_channels(image)
fd.plot_3d_histogram(image)
fd.plot_channel_histogram(image, 'R')
fd.show_topography(image, 'R', blur_radius=10, vert_exag=0.7)
fd.edge_detect(image)
quit()
get_ipython().run_line_magic('logstart', './ipython_session.py append')
get_ipython().run_line_magic('matplotlib', '')
get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')
get_ipython().run_line_magic('clear', '')
from PIL import Image
from matplotlib import pyplot as plt
import numpy as np
import filmdosimetry as fd
image = Image.open('/home/ljubak/Downloads/KCS GK E2E Patient QA 002 RQ [fractionated XZ 20180116].jpg')
fd.show_channels(image)
fd.plot_3d_histogram(image)
fd.plot_channel_histogram(image, 'R')
fd.show_topography(image, 'R', blur_radius=10, vert_exag=0.7)
fd.show_topography(image, 'R', blur_radius=10, vert_exag=5)
fd.show_topography(image, 'R', blur_radius=10, vert_exag=2)
fd.show_topography(image, 'R', blur_radius=10, vert_exag=1)
fd.edge_detect(image)
fd.plot_channel_histogram(image, 'R')
fd.plot_chnl_row_profile(image, 'R', 652, pad=70)
fd.show_channel_threshold(image, 'R', 100)
fd.show_channel_threshold(image, 'R', 40)
fd.show_channel_threshold(image, 'R', 150)
fd.show_topography(image, 'R', blur_radius=10, vert_exag=1)
fd.show_topography(image, 'R', blur_radius=5, vert_exag=0.7)
fd.plot_channel_histogram(image, 'R')
fd.edge_detect(image)
fd.plot_channel_histogram(image, 'R')
fd.show_channel_threshold(image, 'R', 142)
fd.show_channel_threshold(image, 'R', 120)
fd.show_channel_threshold(image, 'R', 110)
fd.show_channel_threshold(image, 'R', 40)
255 - 80
(255 - 80)/2
255 - (255 - 80)/2
fd.show_channel_threshold(image, 'R', 167)
fd.plot_chnl_row_profile(image, 'R', 652, pad=70)
176-120
(176-120)/2
fd.plot_channel_histogram(image, 'R')
fd.plot_chnl_row_profile(image, 'R', 698, pad=70)
(176-110)/2
255 - 176 + 33
fd.show_channel_threshold(image, 'R', 112)
from mpl_toolkits.mplot3d import Axes3D
r_chnl = np.asarray(image.getchannel('R'))
r_chnl.size
r_chnl.ndim
dir(r_chnl)
r_chnl.shape
X = [x for x in range(r_chnl.shape[0])]
Y = [y for y in range(r_chnl.shape[1])]
fig = plt.figure()
ax = Axes3D(fig)
ax.plot_surface(X, Y, r_chnl, rstride=1, cstride=1, cmap=cm.viridis)
ax.plot_surface(X, Y, r_chnl, rstride=1, cstride=1, cmap=plt.cm.viridis)
X, Y = np.mgrid[:r_chnl.shape[0],:r_chnl.shape[1]]
Z = r_chnl[::1,::1]
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.cm.viridis)
r_chnl = image.getchannel('R')
r_chnl.size
r_chnl.size * 0.5
nsz = (r_chnl.size[0] * 0.5, r_chnl.size[1] * 0.5)
nsz
r_rsz = r_chnl.resize(nsz)
nsz = (int(r_chnl.size[0] * 0.5), int(r_chnl.size[1] * 0.5))
nsz
r_rsz = r_chnl.resize(nsz)
r_rsz = np.asarray(r_chnl.resize(nsz))
Z = r_rsz[::1,::1]
X, Y = np.mgrid[:Z.shape[0],:Z.shape[1]]
fig = plt.figure()
ax = Axes3D(fig)
Z = 255 - Z
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.cm.viridis)
fig = plt.figure()
ax = Axes3D(fig)
ax.view_init(60, 90)
ax.view_init(30, 90)
ax.view_init(60, 90)
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.cm.nipy_spectral)
ax.view_init(60, 0)
ax.cla()
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.cm.nipy_spectral)
quit()
get_ipython().run_line_magic('logstart', './ipython_session.py append')
get_ipython().run_line_magic('matplotlib', '')
get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')
get_ipython().run_line_magic('clear', '')
from PIL import Image
from matplotlib import pyplot as plt
import numpy as np
import filmdosimetry as fd
from mpl_toolkits.mplot3d import Axes3D
image = Image.open('/home/ljubak/Downloads/KCS GK E2E Patient QA 002 RQ [fractionated XZ 20180116].jpg')
cropbox = (70, 70, image.size[0] - 70, image.size[1] - 70)
newsize = (int((image.size[0] - 140) * 0.5), int((image.size[1] - 140) * 0.5))
imagersz = image.crop(cropbox).resize(newsize, resample=Image.BICUBIC)
Z = 255 - np.asarray(imagersz.getchannel('R'))[::1, ::1]
X, Y = np.mgrid[:Z.shape[0],:Z.shape[1]]
fig = plt.figure()
ax = Axes3D(fig)
ax.view_init(75, 0)
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.cm.nipy_spectral)
quit()
get_ipython().run_line_magic('logstart', './ipython_session.py append')
get_ipython().run_line_magic('matplotlib', '')
get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')
get_ipython().run_line_magic('clear', '')
from PIL import Image
from matplotlib import pyplot as plt
import numpy as np
import filmdosimetry as fd
from mpl_toolkits.mplot3d import Axes3D
image = Image.open('/home/ljubak/Downloads/KCS GK E2E Patient QA 002 RQ [fractionated XZ 20180116].jpg')
cropbox = (70, 70, image.size[0] - 70, image.size[1] - 70)
newsize = (int((image.size[0] - 140) * 0.5), int((image.size[1] - 140) * 0.5))
imagersz = image.crop(cropbox).resize(newsize, resample=Image.BICUBIC)
fd.chnl_3d_heat_plot(imagersz, 'G')
fd.chnl_3d_heat_plot(imagersz, 'R')
