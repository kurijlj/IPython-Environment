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
img1 = Image.open('/home/ljubak/Downloads/KCS GK E2E Patient QA [fractionated FrstFr XZ irr20180116 scn20180116 RQ600dpi].jpg')
img2 = Image.open('/home/ljubak/Downloads/KCS GK E2E Patient QA [fractionated FrstFr XZ irr20180116 scn20180123 RQ600dpi].jpg')
img3 = Image.open('/home/ljubak/Downloads/KCS GK E2E Patient QA [fractionated LstFr XZ irr20180123 scn20180123 RQ600dpi].jpg')
fd.show_channels(img1)
fd.show_channels(img2)
fd.show_channels(img3)
fd.plot_channel_histogram(img1, 'R')
fd.plot_channel_histogram(img2, 'R')
fd.plot_channel_histogram(img3, 'R')
fd.plot_chnl_row_profile(img1, 'R', 778)
fd.plot_chnl_row_profile(img3, 'R', 778)
fd.show_channel_threshold(img1, 'R', 110)
fd.show_channel_threshold(img1, 'R', 96)
fd.show_channel_threshold(img1, 'R', 86)
fd.show_channel_threshold(img3, 'R', 92)
fd.show_channel_threshold(img3, 'R', 72)
fd.show_channel_threshold(img3, 'R', 58)
fd.show_channel_threshold(img3, 'R', 100)
fd.show_channel_threshold(img3, 'R', 80)
fd.show_channel_threshold(img3, 'R', 66)
quit()
get_ipython().run_line_magic('logstart', './ipython_session.py append')
get_ipython().run_line_magic('matplotlib', '')
get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')
get_ipython().run_line_magic('cls', '')
from PIL import Image
from matplotlib import pyplot as plt
import numpy as np
import filmdosimetry as fd
img1 = Image.open('C:/Users/Physicist/Documents/TagSpaces/Work In Progress/KCS GK E2E Patient QA [fractionated FrstFr XZ irr20180116 scn20180116 RQ600dpi].jpg')
img2 = Image.open('C:/Users/Physicist/Documents/TagSpaces/Work In Progress/KCS GK E2E Patient QA [fractionated FrstFr XZ irr20180116 scn20180123 RQ600dpi].jpg')
img3 = Image.open('C:/Users/Physicist/Documents/TagSpaces/Work In Progress/KCS GK E2E Patient QA [fractionated LstFr XZ irr20180123 scn20180123 RQ600dpi].jpg')
img1iso = []
img3iso = []
diff = []
img1iso.append(fd.channel_threshold(img1, 'R', 110))
img1iso.append(fd.channel_threshold(img1, 'R', 96))
img1iso.append(fd.channel_threshold(img1, 'R', 86))
img3iso.append(fd.channel_threshold(img3, 'R', 100))
img3iso.append(fd.channel_threshold(img3, 'R', 80))
img3iso.append(fd.channel_threshold(img3, 'R', 66))
diff.append(img1iso[0] ^ img3iso[0])
diff.append(img1iso[0] ^ img3iso[0][1:,])
diff.append(img1iso[1] ^ img3iso[1][1:,])
diff.append(img1iso[2] ^ img3iso[2][1:,])
fig, ax = plt.subplots(1, 3)
ax[0].imshow(diff[0], plt.cm.gray)
ax[1].imshow(diff[1], plt.cm.gray)
ax[2].imshow(diff[2], plt.cm.gray)
quit()
get_ipython().run_line_magic('logstart', './ipython_session.py append')
get_ipython().run_line_magic('matplotlib', '')
get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')
get_ipython().run_line_magic('cls', '')
from PIL import Image
from matplotlib import pyplot as plt
import numpy as np
import filmdosimetry as fd
m1 = np.array([[True, False, False], [False, False, False], [False, False, False]])
m2 = np.array([[True, True, ], [True, True]])
mu = np.array(m1)
np.copyto(mu, m1)
fig, axs = plt.subplots(1, 3)
axs[0].imshow(m1, cmap=plt.cm.gray)
axs[1].imshow(m2, cmap=plt.cm.gray)
axs[2].imshow(mu, cmap=plt.cm.gray)
quit()
get_ipython().run_line_magic('logstart', './ipython_session.py append')
get_ipython().run_line_magic('matplotlib', '')
get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')
<<<<<<< Updated upstream
get_ipython().run_line_magic('cls', '')
from PIL import Image
from matplotlib import pyplot as plt
import numpy as np
import filmdosimetry as fd
=======
get_ipython().run_line_magic('clear', '')
from sys import float_info
print(float_info)
int.bit_length(255)
(255).to_bytes(2,byteorder='big')
(255).to_bytes(2,byteorder='little')
(0.5).as_integer_ratio()
quit()
get_ipython().run_line_magic('logstart', './ipython_session.py append')
get_ipython().run_line_magic('matplotlib', '')
get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')
get_ipython().run_line_magic('clear', '')
form environment import *
from environment import *
ls('/user/ljubak/Dropbox/TagSpaces')
ls('/home/ljubak/Dropbox/TagSpaces')
ListDirectory.list('/home/ljubak/Dropbox/TagSpaces')
ts = ListDirectory()
ts.list('/home/ljubak/Dropbox/TagSpaces')
ts = ListDirectory('/home/ljubak/Dropbox/TagSpaces')
ts = ListDirectory('/home/ljubak/Dropbox/TagSpaces')
get_ipython().run_line_magic('cls', '')
get_ipython().run_line_magic('clear', '')
ts = ListDirectory()
ts = ListDirectory('/home/ljubak/Dropbox/TagSpaces')
ts = IsTrue('')
ts = IsTrue()
dir(ts)
quit()
get_ipython().run_line_magic('logstart', './ipython_session.py append')
get_ipython().run_line_magic('matplotlib', '')
get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')
get_ipython().run_line_magic('clear', '')
form environment import *
from environment import *
ts = ListDirectory('/home/ljubak/Dropbox/TagSpaces')
'
ts = ListDirectory('/home/ljubak/Dropbox/TagSpaces')
ts.test()
ts.list()
test = IsTrue('')
test.test()
test = IsTrue([])
test.test()
test = IsTrue('hello')
test.test()
import secrets
dir(secrets)
from os import stat
si = os.stat('.')
si
cwd = OsDirectory()
quit()
get_ipython().run_line_magic('logstart', './ipython_session.py append')
get_ipython().run_line_magic('matplotlib', '')
get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')
get_ipython().run_line_magic('clear', '')
cwd = OsDirectory()
from environment import *
cwd = OsDirectory()
cwd.exists()
cwd.isdir()
cwd.list()
dir(cwd)
cwd
dir(cwd.__repr__)
get_ipython().run_line_magic('pinfo', 'cwd.__repr__')
get_ipython().run_line_magic('pinfo', 'cwd.__str__')
cwd
get_ipython().run_line_magic('pinfo', 'cwd.__str__')
quit()
get_ipython().run_line_magic('logstart', './ipython_session.py append')
get_ipython().run_line_magic('matplotlib', '')
get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')
get_ipython().run_line_magic('clear', '')
cwd = OsDirectory()
from environment import *
cwd = OsDirectory()
cwd
get_ipython().run_line_magic('pinfo', 'cwd.__str__')
get_ipython().run_line_magic('pinfo', 'cwd.__init__')
quit()
get_ipython().run_line_magic('logstart', './ipython_session.py append')
get_ipython().run_line_magic('matplotlib', '')
get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')
get_ipython().run_line_magic('clear', '')
from environment import *
cwd = OsDirectory()
get_ipython().run_line_magic('pinfo', 'cwd.__init__')
get_ipython().run_line_magic('pinfo', 'cwd.__repr__')
cwd
str(cwd)
cwd.list()
dir1 = OsDirectory(1)
dir1
str(dir1)
dir1.exists()
dir1.isdir()
dir1.list()
type(1)
dir(OSDirectory)
dir(OsDirectory)
get_ipython().run_line_magic('pinfo', 'OsDirectory.__init__')
type('')
dir1 = OsDirectory(1)
dir1 = OsDirectory('123')
str(type(''))
type('').__class__
a = type('')
a.__class__
dir(a)
'' is str
type('') is str
dir1 = OsDirectory('123')
dir1.exists()
dir1
dir1.list()
dir1.list()
dir1 = OsDirectory(345)
test = IsTrue('hello')
test
get_ipython().run_line_magic('pinfo', 'test.__repr__')
quit()
get_ipython().run_line_magic('logstart', './ipython_session.py append')
get_ipython().run_line_magic('matplotlib', '')
get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')
get_ipython().run_line_magic('clear', '')
from environment import *
test = IsTrue('hello')
test
str(test)
str(test)
test.type()
test.evaluate()
test = IsTrue('')
test.evaluate()
test.type()
str(test)
test
test = IsTrue((1))
test
str(test)
test.evaluate()
test.evaluate(())
test.evaluate([])
test = IsTrue(())
test.evaluate([])
test.evaluate()
test
str(test)
str.type()
test.type()
test = IsTrue(None)
test
str(test)
test.type()
test.evaluate()
test
test = IsTrue(False)
test
test.type()
test.evaluate()
str(test)
test = IsTrue(True)
test
test = IsTrue(range(0))
test
str(test)
test.type()
test.evaluate()
quit()
get_ipython().run_line_magic('logstart', './ipython_session.py append')
get_ipython().run_line_magic('matplotlib', '')
get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')
get_ipython().run_line_magic('clear', '')
from matplotlib import pyplot as plt
import matlpotlib.cm as cm
import numpy as np
import py3ddose as dose3d
df1 = dose3d.DoseFile("./H2O_phantom_with_test_cavity_IAEA_Co60_10x10.3ddose")
pdd1 = df1.dose[:, 30, 30]/df1.max()
plt.plot(pdd1)
quit()
get_ipython().run_line_magic('logstart', './ipython_session.py append')
get_ipython().run_line_magic('matplotlib', '')
get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')
get_ipython().run_line_magic('clear', '')
import egsdosetools as edt
from matplotlib import pyplot as plt
vdose = edt.xyzcls.DoseFile("H2O_phantom_with_test_cavity_IAEA_Co60_10x10.3ddose")
vphnt = edt.xyzcls.PhantomFile("H2O_phantom_with_test_cavity_IAEA_Co60_10x10.egsphant")
fig, ax = plt.subplots(1, 1)
tracker = edt.xyzhlp.IsoSlicesTracker(ax, vphnt.voxelsdensity, vdose.dose / vdose.max())
fig.canvas.mpl_connect('scroll_event', tracker.onscroll)
quit()
get_ipython().run_line_magic('logstart', './ipython_session.py append')
get_ipython().run_line_magic('matplotlib', '')
get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')
get_ipython().run_line_magic('clear', '')
import egsdosetools as edt
from matplotlib import pyplot as plt
vdose = edt.xyzcls.DoseFile("H2O_phantom_with_test_cavity_IAEA_Co60_10x10.3ddose")
vphnt = edt.xyzcls.PhantomFile("H2O_phantom_with_test_cavity_IAEA_Co60_10x10.egsphant")
fig, ax = plt.subplots(1, 1)
tracker = edt.xyzhlp.IsoSlicesTracker(ax, vphnt.voxelsdensity, vdose.dose / vdose.max())
fig.canvas.mpl_connect('scroll_event', tracker.onscroll)
quit()
get_ipython().run_line_magic('logstart', './ipython_session.py append')
get_ipython().run_line_magic('matplotlib', '')
get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')
get_ipython().run_line_magic('cls', '')
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
import csv
infile = open('MPR and SPACE distortion map.csv', 'r')
reader = csv.reader(infile)
mprdx = np.zeros((252))
mprdy = np.zeros((252))
mprdz = np.zeros((252))
spcdx = np.zeros((252))
spcdy = np.zeros((252))
spcdz = np.zeros((252))
i = 0
for row in reader:
    mprdx[i] = row[0]
    mprdy[i] = row[1]
    mprdz[i] = row[2]
    spcdx[i] = row[3]
    spcdy[i] = row[4]
    spcdz[i] = row[5]
    i = i + 1
    
mprdxmt = mprdx.reshape((6, 7, 6))
mprdymt = mprdy.reshape((6, 7, 6))
mprdzmt = mprdz.reshape((6, 7, 6))
spcdxmt = spcdx.reshape((6, 7, 6))
spcdymt = spcdy.reshape((6, 7, 6))
spcdzmt = spcdz.reshape((6, 7, 6))
x, y, z, = np.meshgrid(np.arange(1, 8, 1), np.arange(1, 7, 1), np.arange(1, 7, 1))
fig1 = plt.figure()
ax1 = fig1.gca(projection='3d')
ax1.quiver(x, y, z, mprdxmt, mprdymt, mprdzmt, length=0.5, normalize=True)
fig2 = plt.figure()
ax2 = fig2.gca(projection='3d')
ax2.quiver(x, y, z, spcdxmt, spcdymt, spcdzmt, length=0.5, normalize=True)
ax1.set_ylabel('X')
ax1.set_xlabel('Y')
ax1.set_zlabel('Z')
ax1.set_title('MPR distortion map')
ax2.set_xlabel('Y')
ax2.set_ylabel('X')
ax2.set_zlabel('Z')
ax1.set_title('SPACE distortion map')
quit()
get_ipython().run_line_magic('logstart', './ipython_session.py append')
get_ipython().run_line_magic('matplotlib', '')
get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')
get_ipython().run_line_magic('cls', '')
from mpl_toolkits.mplot3d import axes3d
import matplotlib pyplot as plt
import matplotlib.pyplot as plt
import numpy as np
import csv
infile = open('MPR and SPACE distortion map.csv', 'r')
reader = csv.reader(infile)
mprdx = np.zeros((252))
mprdy = np.zeros((252))
mprdz = np.zeros((252))
spcdx = np.zeros((252))
spcdy = np.zeros((252))
spcdz = np.zeros((252))
i = 0
for row in reader:
    mprdx[i] = row[0]
    mprdy[i] = row[1]
    mprdz[i] = row[2]
    spcdx[i] = row[3]
    spcdy[i] = row[4]
    spcdz[i] = row[5]
    i = i + 1
    
mprdxmt = mprdx.reshape((6, 7, 6))
mprdymt = mprdy.reshape((6, 7, 6))
mprdzmt = mprdz.reshape((6, 7, 6))
spcdxmt = spcdx.reshape((6, 7, 6))
spcdymt = spcdy.reshape((6, 7, 6))
spcdzmt = spcdz.reshape((6, 7, 6))
x, y, z, = np.meshgrid(np.arange(1, 8, 1), np.arange(1, 7, 1), np.arange(1, 7, 1))
fig1 = plt.figure()
ax1 = fig1.gca(projection='3d')
ax1.quiver(x, y, z, mprdxmt, mprdymt, mprdzmt, scale=2.0, 'color')
ax1.quiver(x, y, z, mprdxmt, mprdymt, mprdzmt, scale=2.0, color='magenta')
ax1.quiver(x, y, z, mprdxmt, mprdymt, mprdzmt, scale=0.5)
help(ax1.quiver)
ax1.quiver(x, y, z, mprdxmt, mprdymt, mprdzmt)
ax1.quiver(x, y, z, spcdxmt, spcdymt, spcdzmt)
ax1.quiver(x, y, z, spcdxmt, spcdymt, spcdzmt, length=0.5)
ax1.quiver(x, y, z, spcdxmt, spcdymt, spcdzmt, normalize=True)
fig2 = plt.figure()
ax2 = fig2.gca(projection='3d')
ax1.quiver(x, y, z, mprdxmt, mprdymt, mprdzmt, color='magenta')
ax1.quiver(x, y, z, mprdxmt, mprdymt, mprdzmt)
ax2.quiver(x, y, z, mprdxmt, mprdymt, mprdzmt, color='magenta')
ax2.quiver(x, y, z, mprdxmt, mprdymt, mprdzmt, length=0.2, color='magenta')
ax2.quiver(x, y, z, mprdxmt, mprdymt, mprdzmt, length=0.2, color='blue')
fig3 = plt.figure()
ax3 = fig3.gca(projection='3d')
ax2.quiver(x, y, z, mprdxmt, mprdymt, mprdzmt, length=0.5, color='blue')
ax3.quiver(x, y, z, mprdxmt, mprdymt, mprdzmt, length=0.5, color='green')
quit()
get_ipython().run_line_magic('logstart', './ipython_session.py append')
get_ipython().run_line_magic('matplotlib', '')
get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')
get_ipython().run_line_magic('cls', '')
from mpl_toolkits.mplot3d import axes3d
import matplotlib pyplot as plt
import matplotlib.pyplot as plt
import numpy as np
import csv
infile = open('MPR and SPACE distortion map.csv', 'r')
reader = csv.reader(infile)
mprdx = np.zeros((252))
mprdy = np.zeros((252))
mprdz = np.zeros((252))
spcdx = np.zeros((252))
spcdy = np.zeros((252))
spcdz = np.zeros((252))
i = 0
for row in reader:
    mprdx[i] = row[0]
    mprdy[i] = row[1]
    mprdz[i] = row[2]
    spcdx[i] = row[3]
    spcdy[i] = row[4]
    spcdz[i] = row[5]
    i = i + 1
    
mprdxmt = mprdx.reshape((6, 7, 6))
mprdxmt = mprdx.reshape((6, 7, 6))
mprdymt = mprdy.reshape((6, 7, 6))
mprdzmt = mprdz.reshape((6, 7, 6))
spcdxmt = spcdx.reshape((6, 7, 6))
spcdymt = spcdy.reshape((6, 7, 6))
spcdzmt = spcdz.reshape((6, 7, 6))
x, y, z, = np.meshgrid(np.arange(1, 8, 1), np.arange(1, 7, 1), np.arange(1, 7, 1))
fig1 = plt.figure()
ax1 = fig1.gca(projection='3d')
ax1.quiver(x, y, z, mprdxmt, mprdymt, mprdzmt, length=0.5, color='green')
fig2 = plt.figure()
ax2 = fig2.gca(projection='3d')
ax2.quiver(x, y, z, spcdxmt, spcdymt, spcdzmt, length=0.5, color='green')
get_ipython().run_line_magic('logstart', './ipython_session.py append')
get_ipython().run_line_magic('matplotlib', '')
get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')
get_ipython().run_line_magic('cls', '')
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
import csv
infile = open('MPR and SPACE distortion map.csv', 'r')
reader = csv.reader(infile)
mprdx = np.zeros((252))
mprdy = np.zeros((252))
mprdz = np.zeros((252))
spcdx = np.zeros((252))
spcdy = np.zeros((252))
spcdz = np.zeros((252))
i = 0
for row in reader:
    mprdx[i] = row[0]
    mprdy[i] = row[1]
    mprdz[i] = row[2]
    spcdx[i] = row[3]
    spcdy[i] = row[4]
    spcdz[i] = row[5]
    i = i + 1
    
mprdxmt = mprdx.reshape((6, 7, 6))
mprdymt = mprdy.reshape((6, 7, 6))
mprdzmt = mprdz.reshape((6, 7, 6))
spcdxmt = spcdx.reshape((6, 7, 6))
spcdymt = spcdy.reshape((6, 7, 6))
spcdzmt = spcdz.reshape((6, 7, 6))
x, y, z, = np.meshgrid(np.arange(10.0, 80.0, 10.0), np.arange(10.0, 70.0, 10.0), np.arange(10.0, 70.0, 10.0))
fig1 = plt.figure()
ax1 = fig1.gca(projection='3d')
ax1.quiver(x, y, z, mprdxmt, mprdymt, mprdzmt, length=0.5, color='green')
fig2 = plt.figure()
ax2 = fig2.gca(projection='3d')
ax2.quiver(x, y, z, mprdxmt, mprdymt, mprdzmt, length=2.0, color='green')
fig3 = plt.figure()
ax3 = fig3.gca(projection='3d')
ax3.quiver(x, y, z, spcdxmt, spcdymt, spcdzmt, length=2.0, color='green')
ax2.set_ylabel('X')
ax2.set_xlabel('Y')
ax2.set_zlabel('Z')
ax2.set_title('MPR distortion map')
ax2.set_ylabel('X [mm]')
ax2.set_xlabel('Y [mm]')
ax2.set_zlabel('Z [mm]')
ax2.set_title('MPR distortion map')
ax3.set_ylabel('X [mm]')
ax3.set_xlabel('Y [mm]')
ax3.set_zlabel('Z [mm]')
ax3.set_title('SPACE distortion map')

quit()
get_ipython().run_line_magic('logstart', './ipython_session.py append')
get_ipython().run_line_magic('matplotlib', '')
get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')
get_ipython().run_line_magic('cls', '')
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
import csv
inf1 = open('mpr_distortion_field.csv', 'r')
rdr1 = csv.reader(inf1)
inf2 = open('space_distortion_field.csv', 'r')
rdr2 = csv.reader(inf2)
mprdx = np.zeros((252))
mprdy = np.zeros((252))
mprdz = np.zeros((252))
spcdx = np.zeros((252))
spcdy = np.zeros((252))
spcdz = np.zeros((252))
i = 0
mprdx = np.zeros((252))
mprdy = np.zeros((252))
mprdz = np.zeros((252))
spcdx = np.zeros((252))
spcdy = np.zeros((252))
spcdz = np.zeros((252))
i = 0
spcdx = np.zeros((210))
spcdy = np.zeros((210))
spcdz = np.zeros((210))
i = 0
for row in rdr1:
    mprdx[i] = row[0]
    mprdy[i] = row[1]
    mprdz[i] = row[2]
    i = i + 1
    
i=0
for row in rdr2:
    spcdx[i] = row[3]
    spcdy[i] = row[4]
    spcdz[i] = row[5]
    i = i + 1
    
for row in rdr2:
    spcdx[i] = row[1]
    spcdy[i] = row[2]
    spcdz[i] = row[3]
    i = i + 1
    
quit()
get_ipython().run_line_magic('logstart', './ipython_session.py append')
get_ipython().run_line_magic('matplotlib', '')
get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')
get_ipython().run_line_magic('cls', '')
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
import csv
inf1 = open('mpr_distortion_field.csv', 'r')
rdr1 = csv.reader(inf1)
inf2 = open('space_distortion_field.csv', 'r')
rdr2 = csv.reader(inf2)
mprdx = np.zeros((252))
mprdy = np.zeros((252))
mprdz = np.zeros((252))
spcdx = np.zeros((210))
spcdy = np.zeros((210))
spcdz = np.zeros((210))
i = 0
for row in rdr1:
    mprdx[i] = row[0]
    mprdy[i] = row[1]
    mprdz[i] = row[2]
    i = i + 1
i=0
for row in rdr2:
    spcdx[i] = row[0]
    spcdy[i] = row[1]
    spcdz[i] = row[2]
    i = i + 1
    
mprdxmt = mprdx.reshape((6, 7, 6))
mprdymt = mprdy.reshape((6, 7, 6))
mprdzmt = mprdz.reshape((6, 7, 6))
spcdxmt = spcdx.reshape((6, 7, 5))
spcdymt = spcdy.reshape((6, 7, 5))
spcdzmt = spcdz.reshape((6, 7, 5))
x1, y1, z1, = np.meshgrid(np.arange(10.0, 80.0, 10.0), np.arange(10.0, 70.0, 10.0), np.arange(10.0, 60.0, 10.0))
x1
x1, y1, z1, = np.meshgrid(np.arange(10.0, 80.0, 10.0), np.arange(10.0, 70.0, 10.0), np.arange(10.0, 70.0, 10.0))
x2, y2, z2, = np.meshgrid(np.arange(10.0, 80.0, 10.0), np.arange(10.0, 60.0, 10.0), np.arange(10.0, 70.0, 10.0))
x2
y2
z2
fig1 = plt.figure()
ax1 = fig1.gca(projection='3d')
ax1.quiver(x1, y1, z1, mprdxmt, mprdymt, mprdzmt, length=0.5, color='green')
fig2 = plt.figure()
ax2 = fig2.gca(projection='3d')
ax2.quiver(x1, y1, z1, mprdxmt, mprdymt, mprdzmt, length=0.5, color='green')
fig3 = plt.figure()
ax3 = fig2.gca(projection='3d')
ax3.quiver(x1, y1, z1, mprdxmt, mprdymt, mprdzmt, length=2.0, color='green')
fig4 = plt.figure()
ax4 = fig4.gca(projection='3d')
ax4.quiver(x1, y1, z1, mprdxmt, mprdymt, mprdzmt, length=2.0, color='green')
fig5 = plt.figure()
ax5 = fig5.gca(projection='3d')
ax5.quiver(x, y, z, spcdxmt, spcdymt, spcdzmt, length=2.0, color='green')
ax5.quiver(x2, y2, z2, spcdxmt, spcdymt, spcdzmt, length=2.0, color='green')
x2, y2, z2, = np.meshgrid(np.arange(10.0, 80.0, 10.0), np.arange(10.0, 70.0, 10.0), np.arange(10.0, 60.0, 10.0))
ax5.quiver(x2, y2, z2, spcdxmt, spcdymt, spcdzmt, length=2.0, color='green')
ax4.set_ylabel('X [mm]')
ax4.set_xlabel('Y [mm]')
ax4.set_zlabel('Z [mm]')
ax4.set_title('MPR distortion map')
ax5.set_ylabel('X [mm]')
ax5.set_xlabel('Y [mm]')
ax5.set_zlabel('Z [mm]')
ax5.set_title('SPACE distortion map')
quit()
get_ipython().run_line_magic('logstart', './ipython_session.py append')
get_ipython().run_line_magic('matplotlib', '')
get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')
get_ipython().run_line_magic('cls', '')
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
import csv
inf1 = open('mpr_distortions_avanto.csv', 'r')
rdr1 = csv.reader(inf1)
inf2 = open('space_distortions_avanto.csv', 'r')
rdr2 = csv.reader(inf2)
mprdx = np.zeros((252))
mprdy = np.zeros((252))
mprdz = np.zeros((252))
spcdx = np.zeros((210))
spcdy = np.zeros((210))
spcdz = np.zeros((210))
i = 0
spcdx = np.zeros((252))
spcdy = np.zeros((252))
spcdz = np.zeros((252))
i = 0
for row in rdr1:
    mprdx[i] = row[0]
    mprdy[i] = row[1]
    mprdz[i] = row[2]
    i = i + 1
i=0
for row in rdr2:
    spcdx[i] = row[0]
    spcdy[i] = row[1]
    spcdz[i] = row[2]
    i = i + 1
    
mprdxmt = mprdx.reshape((6, 7, 6))
mprdymt = mprdy.reshape((6, 7, 6))
mprdzmt = mprdz.reshape((6, 7, 6))
spcdxmt = spcdx.reshape((6, 7, 6))
spcdymt = spcdy.reshape((6, 7, 6))
spcdzmt = spcdz.reshape((6, 7, 6))
x, y, z, = np.meshgrid(np.arange(10.0, 80.0, 10.0), np.arange(10.0, 70.0, 10.0), np.arange(10.0, 60.0, 10.0))
fig1 = plt.figure()
ax1 = fig1.gca(projection='3d')
ax1.quiver(x, y, z, mprdxmt, mprdymt, mprdzmt, length=0.5, color='green')
mprdxmt
mprdymt
fig2 = plt.figure()
ax2 = fig2.gca(projection='3d')
ax2.quiver(x, y, z, mprdxmt, mprdymt, mprdzmt, length=2.0, color='green')
x, y, z, = np.meshgrid(np.arange(10.0, 80.0, 10.0), np.arange(10.0, 70.0, 10.0), np.arange(10.0, 70.0, 10.0))
fig3 = plt.figure()
ax3 = fig3.gca(projection='3d')
ax3.quiver(x, y, z, mprdxmt, mprdymt, mprdzmt, length=2.0, color='green')
fig4 = plt.figure()
ax4 = fig4.gca(projection='3d')
ax4.quiver(x, y, z, spcdxmt, spcdymt, spcdzmt, length=2.0, color='green')
quit()
get_ipython().run_line_magic('logstart', './ipython_session.py append')
get_ipython().run_line_magic('matplotlib', '')
get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')
get_ipython().run_line_magic('cls', '')
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
import csv
inf1 = open('mpr_distortions_avanto.csv', 'r')
rdr1 = csv.reader(inf1)
inf2 = open('space_distortions_avanto.csv', 'r')
rdr2 = csv.reader(inf2)
mprdx = np.zeros((252))
mprdy = np.zeros((252))
mprdz = np.zeros((252))
spcdx = np.zeros((210))
spcdy = np.zeros((210))
spcdz = np.zeros((210))
i = 0
for row in rdr1:
    mprdx[i] = row[0]
    mprdy[i] = row[1]
    mprdz[i] = row[2]
    i = i + 1
i=0
for row in rdr2:
    spcdx[i] = row[0]
    spcdy[i] = row[1]
    spcdz[i] = row[2]
    i = i + 1
    
quit()
get_ipython().run_line_magic('logstart', './ipython_session.py append')
get_ipython().run_line_magic('matplotlib', '')
get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')
get_ipython().run_line_magic('cls', '')
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
import csv
inf1 = open('mpr_distortions_avanto.csv', 'r')
rdr1 = csv.reader(inf1)
inf2 = open('space_distortions_avanto.csv', 'r')
rdr2 = csv.reader(inf2)
mprdx = np.zeros((252))
mprdy = np.zeros((252))
mprdz = np.zeros((252))
spcdx = np.zeros((252))
spcdy = np.zeros((252))
spcdz = np.zeros((252))
i = 0
for row in rdr1:
    mprdx[i] = row[0]
    mprdy[i] = row[1]
    mprdz[i] = row[2]
    i = i + 1
i=0
for row in rdr2:
    spcdx[i] = row[0]
    spcdy[i] = row[1]
    spcdz[i] = row[2]
    i = i + 1
    
mprdxmt = mprdx.reshape((6, 7, 6))
mprdymt = mprdy.reshape((6, 7, 6))
mprdzmt = mprdz.reshape((6, 7, 6))
spcdxmt = spcdx.reshape((6, 7, 6))
spcdymt = spcdy.reshape((6, 7, 6))
spcdzmt = spcdz.reshape((6, 7, 6))
x, y, z, = np.meshgrid(np.arange(10.0, 80.0, 10.0), np.arange(10.0, 70.0, 10.0), np.arange(10.0, 70.0, 10.0))
fig1 = plt.figure()
ax1 = fig1.gca(projection='3d')
ax1.quiver(x, y, z, mprdxmt, mprdymt, mprdzmt, length=2.0, color='green')
fig2 = plt.figure()
ax2 = fig2.gca(projection='3d')
ax2.quiver(x, y, z, spcdxmt, spcdymt, spcdzmt, length=2.0, color='green')
ax1.set_ylabel('X [mm]')
ax1.set_xlabel('Y [mm]')
ax1.set_zlabel('Z [mm]')
ax1.set_title('AVANTO MPRAGE distortion map')
ax2.set_ylabel('X [mm]')
ax2.set_xlabel('Y [mm]')
ax2.set_zlabel('Z [mm]')
ax2.set_title('AVANTO SPACE distortion map')

quit()
get_ipython().run_line_magic('logstart', './ipython_session.py append')
get_ipython().run_line_magic('matplotlib', '')
get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')
get_ipython().run_line_magic('cls', '')
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
import csv
inf1 = open('2019-05-24 -- MPR distortions SKYRA.csv', 'r')
rdr1 = csv.reader(inf1)
inf2 = open('2019-05-24 -- SPACE distortions SKYRA.csv', 'r')
rdr2 = csv.reader(inf2)
mprdx = np.zeros((252))
mprdy = np.zeros((252))
mprdz = np.zeros((252))
spcdx = np.zeros((252))
spcdy = np.zeros((252))
spcdz = np.zeros((252))
i = 0
for row in rdr1:
    mprdx[i] = row[0]
    mprdy[i] = row[1]
    mprdz[i] = row[2]
    i = i + 1
i=0
for row in rdr2:
    spcdx[i] = row[0]
    spcdy[i] = row[1]
    spcdz[i] = row[2]
    i = i + 1
    
mprdxmt = mprdx.reshape((6, 7, 6))
mprdymt = mprdy.reshape((6, 7, 6))
mprdzmt = mprdz.reshape((6, 7, 6))
spcdxmt = spcdx.reshape((6, 7, 6))
spcdymt = spcdy.reshape((6, 7, 6))
spcdzmt = spcdz.reshape((6, 7, 6))
x, y, z, = np.meshgrid(np.arange(10.0, 80.0, 10.0), np.arange(10.0, 70.0, 10.0), np.arange(10.0, 70.0, 10.0))
fig1 = plt.figure()
ax1 = fig1.gca(projection='3d')
ax1.quiver(x, y, z, mprdxmt, mprdymt, mprdzmt, length=2.0, color='green')
fig2 = plt.figure()
ax2 = fig2.gca(projection='3d')
ax2.quiver(x, y, z, spcdxmt, spcdymt, spcdzmt, length=2.0, color='green')
ax1.set_ylabel('X [mm]')
ax1.set_xlabel('Y [mm]')
ax1.set_zlabel('Z [mm]')
ax1.set_title('SKYRA MPRAGE distortion map')
ax2.set_ylabel('X [mm]')
ax2.set_xlabel('Y [mm]')
ax2.set_zlabel('Z [mm]')
ax2.set_title('SKYRA SPACE distortion map')
quit()
get_ipython().run_line_magic('logstart', './ipython_session.py append')
get_ipython().run_line_magic('matplotlib', '')
get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')
get_ipython().run_line_magic('cls', '')
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
import csv
inf = open('2019-05-24 -- MPR Deviations SKYRA', 'r')
rdr = csv.reader(inf)
inf = open('2019-05-24 -- MPR Deviations SKYRA.csv', 'r')
rdr = csv.reader(inf)
mprdx = np.zeros((252))
mprdy = np.zeros((252))
mprdz = np.zeros((252))
mprdr = np.zeros((252))
i=0
for row in rdr1:
    mprdx[i] = row[0]
    mprdy[i] = row[1]
    mprdz[i] = row[2]
    mprdr[i] = row[3]
    i = i + 1
i=0
for row in rdr:
    mprdx[i] = row[0]
    mprdy[i] = row[1]
    mprdz[i] = row[2]
    mprdr[i] = row[3]
    i = i + 1
i=0
np.mean(mprdx)
np.mean(mprdy)
np.mean(mprdz)
np.mean(mprdr)
np.histogram(mprdr)
np.amin(mprdr)
np.amax(mprdr)
np.std(mprdr)
np.histogram(mprdx)
np.histogram(mprdy)
plt.hist(mprdx)
plt.hist(mprdy)
plt.hist(mprdz)
plt.hist(mprdr)
plt.hist(mprdx, bins=252)
plt.hist(mprdy, bins=252)
plt.hist(mprdz, bins=252)
plt.hist(mprdx, bins=25)
plt.hist(mprdy, bins=25)
plt.hist(mprdz, bins=25)
plt.hist(mprdr, bins=25)
devs = np.zeros((252))
sqrt(4)
import math as m
for i in xrange(252):
    devs[i] = m.sqrt(m.pow(mprdx[i], 2) + m.pow(mprdy[i], 2) + m.pow(mprdz[i], 2))
    
range(252)
for i in range(252):
    devs[i] = m.sqrt(m.pow(mprdx[i], 2) + m.pow(mprdy[i], 2) + m.pow(mprdz[i], 2))
    
devs
plt.hist(mprdr, bins=25)
plt.hist(devs, bins=25)
np.amin(devs)
np.amax(devs)
np.mean(devs)
np.std(devs)
quit()
get_ipython().run_line_magic('logstart', './ipython_session.py append')
get_ipython().run_line_magic('matplotlib', '')
get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')
get_ipython().run_line_magic('cls', '')
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
import csv
input_file = open('2019-05-24 - MPR deviations AVANTO.csv', 'r')
input_file_reader = csv.reader(input_file)
x_devs = np.zeros((252))
y_devs = np.zeros((252))
z_devs = np.zeros((252))
rad_devs = np.zeros((252))
i=0
for row in input_file_reader:
    x_devs[i] = row[4]
    y_devs[i] = row[6]
    z_devs[i] = row[8]
    rad_devs[i] = row[10]
    i = i + 1
quit()
get_ipython().run_line_magic('logstart', './ipython_session.py append')
get_ipython().run_line_magic('matplotlib', '')
get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')
get_ipython().run_line_magic('cls', '')
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
import csv
input_file = open('2019-05-24 - MPR deviations AVANTO.csv', 'r')
input_file_reader = csv.reader(input_file)
x_devs = np.zeros((252))
y_devs = np.zeros((252))
z_devs = np.zeros((252))
rad_devs = np.zeros((252))
i = 0
for row in input_file_reader:
    x_devs[i] = row[4]
    y_devs[i] = row[6]
    z_devs[i] = row[8]
    rad_devs[i] = row[10]
    i = i + 1
    
x_devs_mtrx = x_devs.reshape((6, 7, 6))
x_devs_mtrx
quit()
get_ipython().run_line_magic('logstart', './ipython_session.py append')
get_ipython().run_line_magic('matplotlib', '')
get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')
get_ipython().run_line_magic('cls', '')
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
import csv
input_file = open('2019-05-24 - MPR deviations AVANTO.csv', 'r')
input_file_reader = csv.reader(input_file)
x_devs = np.zeros((252))
y_devs = np.zeros((252))
z_devs = np.zeros((252))
rad_devs = np.zeros((252))
i = 0
for row in input_file_reader:
    x_devs[i] = row[4]
    y_devs[i] = row[6]
    z_devs[i] = row[8]
    rad_devs[i] = row[10]
    i = i + 1
    
x_devs_mtrx = x_devs.reshape((6, 7, 6))
x_devs_mtrx
quit()
get_ipython().run_line_magic('logstart', './ipython_session.py append')
get_ipython().run_line_magic('matplotlib', '')
get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')
get_ipython().run_line_magic('cls', '')
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
import csv
input_file = open('2019-05-24 - MPR deviations AVANTO.csv', 'r')
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
    
x_devs_mtrx = x_devs.reshape((6, 7, 6))
x_devs_mtrx
y_devs_mtrx = y_devs.reshape((6, 7, 6))
z_devs_mtrx = z_devs.reshape((6, 7, 6))
rad_devs_mtrx = rad_devs.reshape((6, 7, 6))
fig, axes = plt.subplots(1, 6)
titles = ['Layer 1', 'Layer 2', 'Layer 3', 'Layer 4', 'Layer 5', 'Layer 6']
x_devs_mtrx[0::]
x_devs_mtrx[::0]
x_devs_mtrx[::1]
x_devs_mtrx[1,:,:]
x_devs_mtrx[0,:,:]
for i in range(5):
    axes[i].set_title(titles[i])
    axes[i].imshow(x_devs_mtrx[i,:,:], cmap=plt.cm.nipy_spectral)
    
range(5)
for i in range(5):
    x_devs_mtrx[i,:,:]
    
for i in range(5):
    print(x_devs_mtrx[i,:,:])
    
fig, axes = plt.subplots(1, 6)
for i in range(6):
    axes[i].set_title(titles[i])
    axes[i].imshow(x_devs_mtrx[i,:,:], cmap=plt.cm.coolwarm)
    
    
fig = plt.figure()
import matplotlib.gridspec as gs
grid = gs.GridSpec(4, 1, figure=fig)
grid = gs.GridSpec(4, 1, fig)
ax1 = fig.add_subplot(grid[0, 0])
fig = plt.figure()
grid = fig.add_gridspec(ncols=1, nrows=4)
quit()
get_ipython().run_line_magic('logstart', './ipython_session.py append')
get_ipython().run_line_magic('matplotlib', '')
get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')
get_ipython().run_line_magic('cls', '')
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
import csv
input_file = open('2019-05-24 - MPR deviations AVANTO.csv', 'r')
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
    
x_devs_mtrx = x_devs.reshape((6, 7, 6))
y_devs_mtrx = y_devs.reshape((6, 7, 6))
z_devs_mtrx = z_devs.reshape((6, 7, 6))
rad_devs_mtrx = rad_devs.reshape((6, 7, 6))
fig = plt.figure()
grid = fig.add_gridspec(ncols=1, nrows=4)
fig, axes = plt.subplots(4, 6)
titles = ['Layer 1', 'Layer 2', 'Layer 3', 'Layer 4', 'Layer 5', 'Layer 6']
for i in range(6):
    axes[i, 0].set_title(titles[i])
    axes[i, 1].set_title(titles[i])
    axes[i, 2].set_title(titles[i])
    axes[i, 3].set_title(titles[i])
    axes[i, 0].imshow(x_devs_mtrx[i,:,:], cmap=plt.cm.coolwarm)
    axes[i, 1].imshow(y_devs_mtrx[i,:,:], cmap=plt.cm.coolwarm)
    axes[i, 2].imshow(z_devs_mtrx[i,:,:], cmap=plt.cm.coolwarm)
    axes[i, 3].imshow(rad_devs_mtrx[i,:,:], cmap=plt.cm.coolwarm)
    
for i in range(6):
    axes[0, i].set_title(titles[i])
    axes[1, i].set_title(titles[i])
    axes[2, i].set_title(titles[i])
    axes[3, i].set_title(titles[i])
    axes[0, i].imshow(x_devs_mtrx[i,:,:], cmap=plt.cm.coolwarm)
    axes[1, i].imshow(y_devs_mtrx[i,:,:], cmap=plt.cm.coolwarm)
    axes[2, i].imshow(z_devs_mtrx[i,:,:], cmap=plt.cm.coolwarm)
    axes[3, i].imshow(rad_devs_mtrx[i,:,:], cmap=plt.cm.coolwarm)
    
row_titles = ['X-Axis Deviations Map', 'Y-Axis Deviations Map', 'Z-Axis Deviations Map', 'Radial Deviations Map']
for i in range(4):
    axes[i, 0].set_ylabel(row_titles[i])
    
fig, axes = plt.subplots(1, 1)
axes[0].set_title(titles[i])
axes.set_title(titles[i])
axes.set_title(titles[1])
axes.set_title(titles[0])
axes.imshow(x_devs_mtrx[1,:,:], cmap=plt.cm.coolwarm)
axes.imshow(x_devs_mtrx[0,:,:], cmap=plt.cm.coolwarm)
axes.set_xticks(np.arange(6))
axes.set_xticks(np.arange(7)[1:-1])
axes.set_xticks(np.arange(7)[1:])
axes.set_xticks(np.arange(6))
axes.set_yticks(np.arange(7))
x_ticks_labels = ['A', 'B', 'C', 'D', 'E', 'F']
y_ticks_labels = ['1', '2', '3', '4', '5', '6', '7']
axes.set_xticklabels(x_ticks_labels)
axes.set_yticklabels(y_ticks_labels)
for i in range(7):
    for j in range(6):
        text = axes.text(j, i, x_devs_mtrx[0,:,:], ha='center', va='center', color='black')
        
for i in range(7):
    for j in range(6):
        text = axes.text(j, i, x_devs_mtrx[0,j,i], ha='center', va='center', color='black')
        
        
for i in range(7):
    for j in range(6):
        text = axes.text(j, i, x_devs_mtrx[0,i,j], ha='center', va='center', color='black')
fig, axes = plt.subplots(1, 1)
axes.set_title(titles[1])
axes.set_title(titles[0])
axes.imshow(x_devs_mtrx[0,:,:], cmap=plt.cm.coolwarm)
axes.set_xticks(np.arange(6))
axes.set_yticks(np.arange(7))
axes.set_xticklabels(x_ticks_labels)
axes.set_yticklabels(y_ticks_labels)
for i in range(7):
    for j in range(6):
        text = axes.text(j, i, x_devs_mtrx[0,i,j], ha='center', va='center', color='black')
axes.set_xlabel('Layer 1')
get_ipython().run_line_magic('logstart', './ipython_session.py append')
get_ipython().run_line_magic('matplotlib', '')
get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')
get_ipython().run_line_magic('cls', '')
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
import csv
fig, axes = plt.subplots(1, 1)
fig.suptitle('Hello!')
quit()
get_ipython().run_line_magic('logstart', './ipython_session.py append')
get_ipython().run_line_magic('matplotlib', '')
get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')
get_ipython().run_line_magic('cls', '')
import distortions as dt
deviations = dt.import_data('2019-05-24 - MPR deviations AVANTO.csv')
dt.plot_deviation_map(deviations['x'], dt.row_titles[0])
dt.plot_deviation_map(deviations['x'], dt.row_titles[0])
dt.plot_deviation_map(deviations['x'], dt.row_titles[0])
dt.plot_deviation_map(deviations['x'], dt.row_titles[0])
dt.plot_deviation_map(deviations['x'], dt.row_titles[0])
dt.plot_deviation_map(deviations['x'], dt.row_titles[0])
dt.plot_deviation_map(deviations['y'], dt.row_titles[1])
dt.plot_deviation_map(deviations['z'], dt.row_titles[2])
dt.plot_deviation_map(deviations['r'], dt.row_titles[3])
dt.plot_deviation_map(deviations['x'], dt.row_titles[0])
dt.plot_deviation_map(deviations['y'], dt.row_titles[1])
dt.plot_deviation_map(deviations['z'], dt.row_titles[2])
dt.plot_deviation_map(deviations['r'], dt.row_titles[3])
quit()
get_ipython().run_line_magic('logstart', './ipython_session.py append')
get_ipython().run_line_magic('matplotlib', '')
get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')
get_ipython().run_line_magic('cls', '')
import distortions as dt
deviations = dt.import_data('2019-05-24 - MPR deviations AVANTO.csv')
dt.plot_deviation_map(deviations['x'], 'MPR Deviations AVANTO', dt.row_titles[0])
dt.plot_deviation_map(deviations['r'], 'MPR Deviations AVANTO', dt.row_titles[3])
dt.plot_deviation_map(deviations['r'], 'Deviations Map for 3D MPrage Sequence on SIEMENS Avanto 1.5 T MRI Unit', dt.row_titles[3])
dt.plot_deviation_map(deviations['r'], 'Deviations Map for 3D MPrage Sequence on SIEMENS Avanto 1.5 T MRI Unit', dt.row_titles[3])
dt.plot_deviation_map(deviations['r'], 'Deviations Map for 3D MPrage Sequence on SIEMENS Avanto 1.5 T MRI Unit', dt.row_titles['r'])
sd = dt.import_data('2019-05-24 - SPACE deviations AVANTO.csv')
dt.plot_deviation_map(sd['r'], 'Deviations Map for T2 SPACE Sequence on SIEMENS Avanto 1.5 T MRI Unit', dt.row_titles['r'])
sd = dt.import_data('2019-05-24 - MPR deviations SKYRA.csv')
dt.plot_deviation_map(sd['r'], 'Deviations Map for T1 3D MPrage Sequence on SIEMENS Skyra 3 T MRI Unit', dt.row_titles['r'])
dt.plot_deviation_map(sd['r'], 'Deviations Map for T1 3D MPrage Sequence on SIEMENS Skyra 3 T MRI Unit', dt.row_titles['r'])
sd = dt.import_data('2019-05-24 - SPACE deviations SKYRA.csv')
dt.plot_deviation_map(sd['r'], 'Deviations Map for T2 SPACE Sequence on SIEMENS Skyra 3 T MRI Unit', dt.row_titles['r'])
quit()
get_ipython().run_line_magic('logstart', './ipython_session.py append')
get_ipython().run_line_magic('matplotlib', '')
get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')
get_ipython().run_line_magic('cls', '')
import distortions as dt
dt.plot_measurement_map()
dt.plot_measurement_map()
dt.plot_measurement_map()
quit()
get_ipython().run_line_magic('logstart', './ipython_session.py append')
get_ipython().run_line_magic('matplotlib', '')
get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')
get_ipython().run_line_magic('cls', '')
words = ['look','into','my','eyes','look','into','my','eyes','the','eyes','the','eyes','the','eyes','not','around','the','eyes',"don't",'look','around','the','eyes','look','into','my','eyes',"you're",'under']
from collections import CO
from collections import Counter
word_counts = Counter(words)
word_counts
exit()
get_ipython().run_line_magic('logstart', './ipython_session.py append')
get_ipython().run_line_magic('matplotlib', '')
get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')
get_ipython().run_line_magic('cls', '')
from dosimetry import map_measurements
snlog = open('(2016-08-09) -- Output.txt', 'rt', encoding='utf-8')
map_measurements(snlog)
map_measurements(snlog)
map_measurements(snlog)
map_measurements(snlog)
map_measurements(snlog)
map_measurements(snlog)
exit()
get_ipython().run_line_magic('logstart', './ipython_session.py append')
get_ipython().run_line_magic('matplotlib', '')
get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')
get_ipython().run_line_magic('cls', '')
get_ipython().run_line_magic('clear', '')
from dosimetry import map_measurements
snlog = open('./\(2016-08-09) -- Output.txt', 'rt', encoding='utf-8')
snlog = open('./(2016-08-09) -- Output.txt', 'rt', encoding='utf-8')
map_measurements(snlog)
snlog.tell()
snlog.seek(0)
map_measurements(snlog)
map_measurements(snlog)
snlog.tell()
map_measurements(snlog)
map_measurements(snlog)
map_measurements(snlog)
map_measurements(snlog)
exit()
get_ipython().run_line_magic('logstart', './ipython_session.py append')
get_ipython().run_line_magic('matplotlib', '')
get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')
get_ipython().run_line_magic('cls', '')
snlog = open('./(2016-08-09) -- Output.txt', 'rt', encoding='utf-8')
from dosimetry import map_measurements
map_measurements(snlog)
snlog.tell()
snlog.seek(99)
46710 - 99
snlog.read(46611)
snlog.seek(0)
map_measurements(snlog)
46664 - 53
snlog.seek(53)
snlog.read(46611)
snlog.seek(0)
snlog.seek(55)
46664 - 55
snlog.read(46609)
snlog.seek(0)
snlog.seek(53)
measurement = snlog.read(46611)
for line in measurement:
    print(line)
    
for line in measurement.split():
    print(line)
    
for line in measurement.splitlines():
    print(line)
    
snlog.close()
exit()
seq = (1, 2, 3, 4, 5, 6)
for index, item in enumerate(seq):
    print(index, item)
    
get_ipython().run_line_magic('logstart', './ipython_session.py append')
get_ipython().run_line_magic('matplotlib', '')
get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')
get_ipython().run_line_magic('cls', '')
from dosimetry import measurements
snlog = open('./(2016-08-09) -- Output.txt', 'rt', encoding='utf-8')
res = measurements(snlog)
res
len(res)
get_ipython().run_line_magic('man', 'egrep')
exit()
get_ipython().run_line_magic('logstart', './ipython_session.py append')
get_ipython().run_line_magic('matplotlib', '')
get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')
get_ipython().run_line_magic('cls', '')
somelist = (1, 2, 3, 4, 5, 6, 7)
print(len(somelist))
for index, item in enumerate(somelist):
    print(index, item)
    
somelist = (1, 2, 4, 8, 16, 32, 64)
difflist = (1, 2, 4, 8, 16, 32)
print(len(somelist))
for index, item in enumerate(somelist):
    if index < len(somelist) - 1:
        print(somelist[index + 1] - item)
    else:
        print(item - 1)
        
from dosimetry import measurements
snlog = open('(2016-08-09) -- Output.txt', 'rt', encoding='utf-8')
measurements(snlog)
res = measurements(snlog)
len(res)
print(res[20])
print(res[19])
get_ipython().run_line_magic('logstart', './ipython_session.py append')
get_ipython().run_line_magic('matplotlib', '')
get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')
get_ipython().run_line_magic('cls', '')
get_ipython().run_line_magic('clear', '')
from dosimetry import measurements
snlog = open('./(2016-08-09) -- Output.txt', 'rt', encoding='utf-8')
result = measurements(snlog)
len(result)
result[0].application_version()
result[0].app_version()
result[9].app_version()
result[20].app_version()
result[19].app_version()
result = measurements(snlog)
len(result)
result[19].app_version()
result[19].log_date()
result[19].log_date()
result[19].log_date()
result[19].log_date()
log_datetime = result[19].log_date()
log_datetime.date()
log_datetime.time()
print(log_datetime.time())
print(log_datetime.date())
log_datetime = result[0].log_date()
print(log_datetime.date())
print(log_datetime.time())
result = measurements(snlog)
result[0].app_version
result[0].app_version()
print(result[0].log_datetime())
print(result[0].log_date())
print(result[0].log_time())
print(result[0].pce_serial_number())
exit()
get_ipython().run_line_magic('logstart', './ipython_session.py append')
get_ipython().run_line_magic('matplotlib', '')
get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')
get_ipython().run_line_magic('cls', '')
snlog = open('(2016-08-09) -- Output.txt', 'rt', encoding='utf-8')
from dosimetry import measurements
result = measurements(snlog)
len(result)
result[0].bkg_compensation()
result[1].bkg_compensation()
result[2].bkg_compensation()
result[2].bkg_compensation()
result[1].bkg_compensation()
result[0].bkg_compensation()
result[0].bkg_compensation()
result[1].bkg_compensation()
result[1].app_version()
somelst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 15]
somelst
somelst
somestr = 'line1\nline2\nline3'
somestr.splitlines()
somestr.splitlines()
somestr.splitlines()
somestr.splitlines()
result = measurements(snlog)
result[1].app_version()
result[1].bkg_compensation()
print(result[1])
print(result[1])
get_ipython().run_line_magic('cls', '')
print(result[0])
print(result[2])
from dosimetry import map_measurements()
from dosimetry import map_measurements(snlog)
from dosimetry import map_measurements
map_measurements(snlog)
snlog.seek(53, 0)
snlog.readline()
snlog.seek(54, 0)
snlog.readline()
snlog.seek(55, 0)
snlog.readline()
snlog.seek(56, 0)
snlog.readline()
snlog.read(10)
snlog.seek(56, 0)
snlog.read(50)
snlog.seek(53, 0)
snlog.read(50)
snlog.seek(57, 0)
snlog.read(50)
snlog.close
snlog.close()
snlog = open('(2016-08-09) -- Output.txt', 'rt', encoding='utf-8', newline='\n')
from dosimetry import map_measurements
map_measurements(snlog)
result = measurements(snlog)
result[1].app_version()
result[0].app_version()
result[1].bkg_compensation()
result[0].bkg_compensation()
result[10].bkg_compensation()
result[15].bkg_compensation()
result[15].pce_serial_number()
result[1].pce_serial_number()
result[0].bkg_compensation()
result[0].bkg_current()
result[0].bkg_current()
result[0].bkg_current()
exit()
get_ipython().run_line_magic('logstart', './ipython_session.py append')
get_ipython().run_line_magic('matplotlib', '')
get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')
get_ipython().run_line_magic('cls', '')
snlog = open('(2016-08-09) -- Output.txt', 'rt', encoding='utf-8', newline='\n')
from dosimetry import measurements
result = measurements(snlog)
result[0].bkg_compensation()
result[0].bkg_current()
result[2].bkg_compensation()
result[2].bkg_current()
result[1].bkg_current()
result[19].bkg_current()
result[1].input_correction()
result[1].input_correction()
exit()
get_ipython().run_line_magic('logstart', './ipython_session.py append')
get_ipython().run_line_magic('matplotlib', '')
get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')
get_ipython().run_line_magic('cls', '')
snlog = open('(2016-08-09) -- Output.txt', 'rt', encoding='utf-8', newline='\n')
from dosimetry import measurements
result = measurements(snlog)
result[1].input_correction()
result[1].input_correction()
result[1].input_correction()
result[1].input_calibration()
result[19].bkg_current()
exit()
get_ipython().run_line_magic('logstart', './ipython_session.py append')
get_ipython().run_line_magic('matplotlib', '')
get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')
get_ipython().run_line_magic('cls', '')
from dosimetry import measurements
from dosimetry import PCELogMeasurement
nonemsr = PCELogMeasurement()
print(nonemsr)
exit()
get_ipython().run_line_magic('logstart', './ipython_session.py append')
get_ipython().run_line_magic('matplotlib', '')
get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')
get_ipython().run_line_magic('cls', '')
get_ipython().run_line_magic('clear', '')
from dosimetry import measurements
snlog = open('./(2016-08-09) -- Output.txt', 'rt', encoding='utf-8', newline='\n')
result = measurements(snlog)
len(result)
result[0].application_version()
result[0].app_version()
from dosimetry import PCELogMeasurement
newlog = PCELogMeasurement()
print(newlog)
nelog
newlog
newlog
print(newlog)
newlog.data(3)
newlog.data(None)
newlog.data('')
newlog.data(3)
print(newlog)
sin(3)
from math import sin
sin(3)
sin(None)
type('hello')
newlog = PCELogMeasurement()
newlog = PCELogMeasurement()
type(None)
newlog = PCELogMeasurement()
'a' is str
'ab' is str
type('ab') is str
newlog = PCELogMeasurement()
newlog = PCELogMeasurement(34)
newlog = PCELogMeasurement(34)
newlog = PCELogMeasurement()
newlog = PCELogMeasurement(None)
newlog = PCELogMeasurement('Hello')
newlog = PCELogMeasurement(34)
newlog = PCELogMeasurement(3.4)
type(int)
type(int)._str_
type(int).__str__()
type(int)._str_()
str(type(int))
type(int).__repr__()
type(int).__name__
newlog = PCELogMeasurement(3.4)
newlog = PCELogMeasurement(34)
newlog = PCELogMeasurement()
newlog.data(34)
newlog.data(3.4)
newlog.data('Hello;')
exit()
df = open('data.csv', 'r')
lst_edep = []
lst_d = []
for row in df:
    lst_data = row.split()
    lst_edep.append(float(lst_data[4]))
    lst_d.append(float(lst_data[8]))
    
for row in df:
    lst_data = row.split()
    lst_edep.append(float(lst_data[4]))
    lst_d.append(float(lst_data[8]))
    
lst_edep
lst_d
import numpy as np
edep = np.array(lst_edep)
dose = np.array(lst_d)
edep
dose
get_ipython().run_line_magic('logstart', './ipython_session.py append')
get_ipython().run_line_magic('matplotlib', '')
get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')
get_ipython().run_line_magic('cls', '')
edep
dose
from matplotlib import pyplot as plt
len(edep)
xrange(1, 40)
range(1, 40)
fig, axes = plt.subplots(1, 2, num='PDD')
axes[0].axis('off')
axes[1].axis('off')
axes[0].bar([x for x in range(1, 40)], edep, width=0.1)
fig, axes = plt.subplots(1, 2, num='PDD')
axes[0].bar([x for x in range(40)], edep, width=0.1)
axes[1].bar([x for x in range(40)], dose, width=0.1)
axes[0].plt([x for x in range(40)], edep, width=0.1)
axes[0].plot([x for x in range(40)], edep, width=0.1)
axes[0].plot([x for x in range(40)], edep)
axes[1].plot([x for x in range(40)], dose)
exit()
get_ipython().run_line_magic('logstart', './ipython_session.py append')
get_ipython().run_line_magic('matplotlib', '')
get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')
get_ipython().run_line_magic('cls', '')
get_ipython().run_line_magic('clear', '')
fd = open('data.csv', 'r')
counter = 0
lst_edep = []
lst_dose = []
for row in fd:
    if 1 <= counter:
        splitted = row.split()
        lst_edep.append(float(splitted[4]))
        lst_dose.append(float(splitted[8]))
    counter = counter + 1
    
quit()
get_ipython().run_line_magic('logstart', './ipython_session.py append')
get_ipython().run_line_magic('matplotlib', '')
get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')
get_ipython().run_line_magic('cls', '')
get_ipython().run_line_magic('clear', '')
fd = open('data.csv', 'r')
counter = 0
lst_edep = []
lst_dose = []
for row in fd:
    if 1 <= counter:
        splitted = row.split()
        lst_edep.append(float(splitted[4]))
        lst_dose.append(float(splitted[6]))
    counter = counter + 1
    
row = '0 H2O521ICRU 1.000 0.0008 3.0872e-08 3.900 6.3002e-15 3.900'
row.split()
row.split()[4]
float(row.split()[4])
quot
quit()
get_ipython().run_line_magic('logstart', './ipython_session.py append')
get_ipython().run_line_magic('matplotlib', '')
get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')
get_ipython().run_line_magic('clear', '')
fd = open('data.csv', 'r')
counter = 0
lst_edep = []
lst_dose = []
for row in fd:
    if 1 < counter:
        splitted = row.split()
        lst_edep.append(float(splitted[4]))
        lst_dose.append(float(splitted[6]))
    counter = counter + 1
    
lst_edep
len(lst_edep)
lst_dose
import numpy as np
edep = np.array(lst_edep)
dose = np.array(lst_dose)
from matplotlib import pyplot as plt
fig, axes = plt.subplots(1, 2, num='EDEP and PDD')
axes[0].axis('off')
axes[1].axis('off')
axes[0].plot([x for x in range(len(lst_edep))], edep)
axes[1].plot([x for x in range(len(lst_dose))], dose)
axes[0].axis('on')
axes[1].axis('on')
quit()
get_ipython().run_line_magic('logstart', './ipython_session.py append')
get_ipython().run_line_magic('matplotlib', '')
get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')
get_ipython().run_line_magic('cls', '')
df = open('data.csv', 'r')
counter = 0
lst_edep = []
lst_dose = []
for row in df:
    if 1 < counter:
        sp = row.split()
        lst_edep.append(float(sp[4]))
        lst_dose.append(float(sp[6]))
        
lst_edep
lst_dose
quit()
get_ipython().run_line_magic('logstart', './ipython_session.py append')
get_ipython().run_line_magic('matplotlib', '')
get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')
get_ipython().run_line_magic('cls', '')
counter = 0
lst_edep = []
lst_dose = []
for row in df:
    if 1 < counter:
        sp = row.split()
        lst_edep.append(float(sp[4]))
        lst_dose.append(float(sp[6]))
    counter += 1
    
df = open('data.csv', 'r')
for row in df:
    if 1 < counter:
        sp = row.split()
        lst_edep.append(float(sp[4]))
        lst_dose.append(float(sp[6]))
    counter += 1
    
lst_edep
import numpy as np
edep = np.array(lst_edep)
dose = np.array(lst_dose)
len(edep)
from matplotlib import pyplot as plt
fig, axes = plt.subplots(1, 2, num='EDEP and PDD')
axes[0].plot([x for x in range(len(edep))], edep)
axes[1].plot([x for x in range(len(dose))], dose)
quit()
get_ipython().run_line_magic('logstart', './ipython_session.py append')
get_ipython().run_line_magic('matplotlib', '')
get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')
get_ipython().run_line_magic('cls', '')
import radiobiology as rb
data = open('Zivanovic Ivana TR1.csv', 'r')
cdvh = cdvh_from_file(data, ',')
cdvh = rb.cdvh_from_file(data, ',')
ddvh = rb.cdvh_to_ddvh(cdvh)
ddvh = rb.cdvh_to_ddvh(cdvh)
from matplotlib import pyplot as plt
fig, axes = plt.subplots(1)
axes.axis('off')
axes.bar(cdvh[:,0], cdvh[:,1])
fig, axes = plt.subplots(1)
axes.line(cdvh[:,0], cdvh[:,1])
axes.plot(cdvh[:,0], cdvh[:,1], '.-')
ddvh = rb.cdvh_to_ddvh(cdvh)
ddvh = rb.cdvh_to_ddvh(cdvh)
ddvh = rb.cdvh_to_ddvh(cdvh)
ddvh = rb.cdvh_to_ddvh(cdvh)
data.close()
data = open('Zivanovic Ivana TR1.csv', 'r')
cdvh = rb.cdvh_from_file(data, ',')
ddvh = rb.cdvh_to_ddvh(cdvh)
fig, axes = plt.subplots(1)
axes.plot(cdvh[:,0], cdvh[:,1], '.-')
axes.plot(ddvh[:,0], ddvh[:,1], '.-')
fig, axes = plt.subplots(1)
axes.plot(ddvh[:,0], ddvh[:,1], '.-')
ddvh
data.close()
data = open('Zivanovic Ivana TR1.csv', 'r')
cdvh = rb.cdvh_from_file(data, ',')
ddvh = rb.cdvh_to_ddvh(cdvh)
fig, axes = plt.subplots(1)
axes.plot(ddvh[:,0], ddvh[:,1], '.-')
ddvh = rb.cdvh_to_ddvh(cdvh)
fig, axes = plt.subplots(1)
axes.plot(ddvh[:,0], ddvh[:,1], '.-')
quit()
get_ipython().run_line_magic('logstart', './ipython_session.py append')
get_ipython().run_line_magic('matplotlib', '')
get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')
get_ipython().run_line_magic('cls', '')
import radiobiology as rb
tr = open('DVH_TR.csv', 'r')
rt = open('DVH_PP.csv', 'r')
dvhtr = rb.dvh_from_file(tr, ',')
dvhrt = rb.dvh_from_file(rt, ',')
from matplotlib import pyplot as plt
fig, axes = plt.subplots(1)
axes.plot(dvhtr[:,0], dvhtr[:,1], '.-')
axes.plot(dvhrt[:,0], dvhrt[:,1], '.-')
rb.total_volume(dvhtr)
rb.total_volume(dvhrt)
ndvhtr = rb.normalized_ddvh(dvhtr, 1, 2.0, 1.03)
quit()
get_ipython().run_line_magic('logstart', './ipython_session.py append')
get_ipython().run_line_magic('matplotlib', '')
get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')
get_ipython().run_line_magic('cls', '')
from matplotlib import pyplot as plt
import radiobiology as rb
tr = open('DVH_TR.csv', 'r')
rt = open('DVH_PP.csv', 'r')
dvhtr = rb.dvh_from_file(tr, ',')
dvhrt = rb.dvh_from_file(rt, ',')
ndvhtr = rb.normalized_ddvh(dvhtr, 1, 2.0, 1.03)
ndvhtr = rb.normalized_ddvh(dvhtr, 1, 2.0, 1.03)
ndvhrt = rb.normalized_ddvh(dvhrt, 1, 2.0, 1.03)
fig1, axes1 = plt.subplots(1)
fig2, axes2 = plt.subplots(1)
axes.plot(dvhtr[:,0], dvhtr[:,1], '.-')
axes1.plot(dvhtr[:,0], dvhtr[:,1], '.-')
axes1.plot(dvhrt[:,0], dvhrt[:,1], '.-')
axes2.plot(ndvhtr[:,0], ndvhtr[:,1], '.-')
axes2.plot(ndvhrt[:,0], ndvhrt[:,1], '.-')
2^2
power(2,2)
pow(2,2)
pow(2,1)
pow(2,0)
rb.EUD(ndvhtr, 25.0)
rb.EUD(ndvhtr, 25.0)
rb.EUD(ndvhrt, 25.0)
rb.NTCP(17.78 + 6.63, 65.0, 3.0)
rb.NTCP(17.78 + 6.63, 65.0, 3.0) * 100
quit()
get_ipython().run_line_magic('logstart', './ipython_session.py append')
get_ipython().run_line_magic('matplotlib', '')
get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')
get_ipython().run_line_magic('cls', '')
get_ipython().run_line_magic('clear', '')
from matplotlib import pyplot as plt
import skimage as ski
from skimage import filters
from PIL import Image
img1 = Image.open('./test_film_1.png')
img2 = Image.open('./test_film_2.tiff')
get_ipython().run_line_magic('logstart', './ipython_session.py append')
get_ipython().run_line_magic('matplotlib', '')
get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')
get_ipython().run_line_magic('clear', '')
from matplotlib import pyplot as plt
import skimage as ski
from skimage import filters
from PIL import Image
img1 = Image.open('./test_film_1.png')
img2 = Image.open('./test_film_2.tiff')
img1_red = img1.getchannel('R')
img2_red = img2.getchannel('R')
fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.imshow(img1_red, cmap='gray')
ax2.imshow(img2_red, cmap='gray')
import numpy as np
img1_denoised = filters.median(img1_red, selem=np.ones((5, 5)))
img2_denoised = filters.median(img2_red, selem=np.ones((5, 5)))
ax2.imshow(img1_denoised, cmap='gray')
ax1.imshow(img2_red, cmap='gray')
ax2.imshow(img2_denoised, cmap='gray')
ax1.imshow(img1_red, cmap='gray')
ax2.imshow(img1_denoised, cmap='gray')
from skimage import feature
img1_edges = feature.canny(img1_red, sigma=1.0, low_threshold=10, high_threshold=50)
img1_edges = feature.canny(np.asarray(img1_red), sigma=1.0, low_threshold=10, high_threshold=50)
img1_edges_denoised = feature.canny(np.asarray(img1_denoised), sigma=1.0, low_threshold=10, high_threshold=50)
ax1.imshow(img1_edges, cmap='gray')
ax1.imshow(img1_edges_denoised, cmap='gray')
ax1.imshow(img1_edges, cmap='gray')
ax2.imshow(img1_edges_denoised, cmap='gray')
img2_edges = feature.canny(np.asarray(img2_red), sigma=1.0, low_threshold=10, high_threshold=50)
img2_edges_denoised = feature.canny(np.asarray(img2_denoised), sigma=1.0, low_threshold=10, high_threshold=50)
ax1.imshow(img2_edges, cmap='gray')
ax2.imshow(img2_edges_denoised, cmap='gray')
fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.imshow(img2_edges, cmap='gray')
ax2.imshow(img2_edges_denoised, cmap='gray')
from scipy.ndimage import distance_transform_edt
img1_dt = distance_transform_edt(-img1_edges)
img1_dt = distance_transform_edt(~img1_edges)
img2_dt = distance_transform_edt(~img2_edges)
ax1.imshow(img1_edges, cmap='gray')
ax2.imshow(img1_dt, cmap='gray')
fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.imshow(img1_edges, cmap='gray')
ax2.imshow(img1_dt, cmap='gray')
ax2.imshow(img1_dt)
ax1.imshow(img2_edges, cmap='gray')
ax2.imshow(img2_dt, cmap='gray')
img1_local_max = feature.peak_local_max(img1_dt, indices=False, min_distance=5)
img2_local_max = feature.peak_local_max(img2_dt, indices=False, min_distance=5)
ax1.imshow(img1_edges, cmap='gray')
ax2.imshow(img1_local_max, cmap='gray')
ax1.imshow(img2_edges, cmap='gray')
ax2.imshow(img2_local_max, cmap='gray')
img1_local_max_idx = feature.peak_local_max(img1_dt, indices=True, min_distance=5)
img2_local_max_idx = feature.peak_local_max(img2_dt, indices=True, min_distance=5)
ax1.imshow(img1_edges, cmap='gray')
ax2.imshow(img1_dt, cmap='gray')
ax2.imshow(img1_dt)
ax2.plot(img1_local_max_idx[1], img1_local_max_idx[0], 'r.')
ax2.plot(img1_local_max_idx, 'r.')
ax2.imshow(img1_dt)
ax2.clear()
ax2.plot(img1_local_max_idx[:,1], img1_local_max_idx[:,0], 'r.')
ax2.imshow(img1_dt)
from skimage import measure
ax1.imshow(img2_edges, cmap='gray')
ax2.clear()
ax2.plot(img2_local_max_idx[:,1], img1_local_max_idx[:,0], 'r.')
ax2.plot(img2_local_max_idx[:,1], img2_local_max_idx[:,0], 'r.')
ax2.clear()
ax2.plot(img2_local_max_idx[:,1], img2_local_max_idx[:,0], 'r.')
ax2.clear()
ax2.plot(img2_local_max_idx[:,0], img2_local_max_idx[:,1], 'r.')
ax2.clear()
ax2.plot(img2_local_max_idx[:,1], img2_local_max_idx[:,0], 'r.')
ax2.imshow(img2_dt, cmap='gray')
img1_markers = measure.label(img1_local_max)
img2_markers = measure.label(img2_local_max)
from skimage import morphology, segmentation
img1_labels = morphology.watershed(-img1_dt, img1_markers)
img2_labels = morphology.watershed(-img2_dt, img2_markers)
ax1.imshow(img1_edges, cmap='gray')
ax2.imshow(segmentation.mark_boundaries(img1_red, img1_labels))
ax2.clear()
ax2.imshow(segmentation.mark_boundaries(img1_red, img1_labels))
ax1.imshow(img2_edges, cmap='gray')
ax2.clear()
ax2.imshow(segmentation.mark_boundaries(img2_red, img2_labels))
from skimage import color
ax2.clear()
ax2.imshow(color.label2rgb(img2_labels, image=image2_red))
ax2.imshow(color.label2rgb(img2_labels, image=img2_red))
ax2.imshow(color.label2rgb(img2_labels, image=np.asarray(img2_red)))
ax1.clear()
ax2.clear()
ax1.imshow(img1_red, cmap='gray')
ax2.imshow(color.label2rgb(img1_labels, image=np.asarray(img1_red)))
from skiimage.transform import hough_circle, hough_circle_peaks
from skimage.transform import hough_circle, hough_circle_peaks
img1_hres = hough_circle(img1_edges, 90)
img1_res
img1_hres
img2_hres = hough_circle(img2_edges, 90)
img1_accums, img1_cx, img1_cy, radii = hough_circle_peaks(img1_hres, radii, total_num_peaks=2)
img1_accums, img1_cx, img1_cy, radii = hough_circle_peaks(img1_hres, 90, total_num_peaks=2)
img1_accums, img1_cx, img1_cy, radii = hough_circle_peaks(img1_hres, 90, total_num_peaks=3)
hough_circle_peaks(img1_hres, 90, total_num_peaks=2)
hough_circle_peaks(img1_hres, np.arange(90), total_num_peaks=2)
hough_circle_peaks(img1_hres, np.arange(90), total_num_peaks=5)
img1_hres = hough_circle(img1_edges, 50)
img2_hres = hough_circle(img2_edges, 50)
hough_circle_peaks(img1_hres, np.arange(50), total_num_peaks=5)
hough_circle_peaks(img2_hres, np.arange(50), total_num_peaks=5)
ax1.clear()
ax2.clear()
ax1.imshow(img2_red, cmap='gray')
ax2.imshow(img2_red)
hough_circle_peaks(img2_hres, np.arange(50), total_num_peaks=10)
img2_hres = hough_circle(img2_edges, 30)
hough_circle_peaks(img2_hres, np.arange(30), total_num_peaks=5)
ax2.clear()
ax2.imshow(img2_edges)
img1_local_max_idx
img1_hough_circle_peaks = hough_circle_peaks(img1_hres, np.arange(50), total_num_peaks=5)
img2_hough_circle_peaks = hough_circle_peaks(img2_hres, np.arange(30), total_num_peaks=5)
img1_hough_circle_centres = zip(img1_hough_circle_peaks[1], img1_hough_circle_peaks[2])
img1_hough_circle_centres
img1_hough_circle_centres = np.column_stack((img1_hough_circle_peaks[1], img1_hough_circle_peaks[2]))
img1_hough_circle_centres
img2_hough_circle_centres = np.column_stack((img2_hough_circle_peaks[1], img2_hough_circle_peaks[2]))
img2_hough_circle_centres
ax2.clear()
ax2.plot(img2_hough_circle_centres[:,1], img2_hough_circle_centres[:,0], 'r.')
ax2.imshow(img2_edges)
ax2.plot(img2_hough_circle_centres[:,0], img2_hough_circle_centres[:,1], 'r.')
ax2.imshow(img2_edges)
ax2.plot(img2_hough_circle_centres, 'r.')
ax2.imshow(img2_edges)
ax2.clear()
ax2.plot(img2_hough_circle_centres[:,1], img2_hough_circle_centres[:,0], 'r.')
ax2.imshow(img2_edges)
ax1.clear()
ax2.clear()
ax1.imshow(img1_red, cmap='gray')
ax2.imshow(img1_edges)
ax2.plot(img1_hough_circle_centres[:,1], img1_hough_circle_centres[:,0], 'r.')
ax2.imshow(img1_edges)
ax2.clear()
ax2.plot(img1_hough_circle_centres[:,0], img1_hough_circle_centres[:,1], 'r.')
ax2.imshow(img1_edges)
ax2.clear()
ax1.clear()
ax1.imshow(img2_red, cmap='gray')
ax2.plot(img2_hough_circle_centres[:,0], img2_hough_circle_centres[:,1], 'r.')
ax2.imshow(img2_edges)
ax2.clear()
img2_hres = hough_circle(img2_edges, 25)
img2_hough_circle_peaks = hough_circle_peaks(img2_hres, np.arange(25), total_num_peaks=5)
img2_hough_circle_centres = np.column_stack((img2_hough_circle_peaks[1], img2_hough_circle_peaks[2]))
ax2.plot(img2_hough_circle_centres[:,0], img2_hough_circle_centres[:,1], 'r.')
ax2.imshow(img2_edges)
img2_hough_circle_centres
quit()
get_ipython().run_line_magic('logstart', './ipython_session.py append')
get_ipython().run_line_magic('matplotlib', '')
get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')
get_ipython().run_line_magic('clear', '')
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image
import filmdosimetry as fd
img1 = Image.open('./test_film_1.png')
img2 = Image.open('./test_film_2.tiff')
img1_cnt = fd.find_fiducials(img1, 0.5, 10, 50)
img1_cnt = fd.find_fiducials(img1, 0.5, 10, 50)
img1.__class__
img2.__class__
type(img1)
dir(img1)
dir(img1.png)
dir(img1.info)
img1.info.keys()
img1_cnt = fd.find_fiducials(img1, 0.5, 10, 50)
img1_cnt = fd.find_fiducials(img1, 0.5, 10, 50)
img1.info['dpi']
img2.info['dpi']
img1_cnt = fd.find_fiducials(img1, 0.5, 10, 50)
img1_cnt1 = fd.find_fiducials(img1, 0.5, 10, 50)
img1_cnt2 = fd.find_fiducials(img1, 0.5, 10, 50)
img1_cnt2 = fd.find_fiducials(img1, 1.0, 10, 50)
img1_cnt2 = fd.find_fiducials(img1, 1.5, 10, 50)
img1_cnt2 = fd.find_fiducials(img1, 1.0, 10, 50)
img1_cnt3 = fd.find_fiducials(img1, 1.5, 10, 50)
img1_cnt1
fig, (ax1, ax2) = plt.subplots(1, 2, 1)
fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.plot(img1_cnt1[:,0], img1_cnt1[:,1], 'r.')
ax1.plot(img1_cnt2[:,0], img1_cnt2[:,1], 'g.')
ax1.plot(img1_cnt3[:,0], img1_cnt3[:,1], 'b.')
ax1.imshow(img1.getchannel('R'))
img1_cnt2
ax1.imshow(img1.getchannel('R'), cmap='grayscale')
ax1.imshow(img1.getchannel('R'), cmap='gray')
img2_cnt1 = fd.find_fiducials(img2, 0.5, 10, 50)
img2_cnt2 = fd.find_fiducials(img2, 1.0, 10, 50)
img2_cnt3 = fd.find_fiducials(img2, 1.5, 10, 50)
ax1.plot(img2_cnt1[:,0], img2_cnt1[:,1], 'r.')
ax1.plot(img2_cnt2[:,0], img2_cnt2[:,1], 'g.')
ax1.plot(img2_cnt3[:,0], img2_cnt3[:,1], 'b.')
ax1.clear()
ax1.plot(img1_cnt1[:,0], img1_cnt1[:,1], 'r.')
ax1.plot(img1_cnt2[:,0], img1_cnt2[:,1], 'g.')
ax1.plot(img1_cnt3[:,0], img1_cnt3[:,1], 'b.')
ax1.imshow(img1.getchannel('R'), cmap='gray')
ax2.plot(img2_cnt1[:,0], img2_cnt1[:,1], 'r.')
ax2.plot(img2_cnt2[:,0], img2_cnt2[:,1], 'g.')
ax2.plot(img2_cnt3[:,0], img2_cnt3[:,1], 'b.')
ax2.imshow(img2.getchannel('R'), cmap='gray')
get_ipython().run_line_magic('clear', '')
img1_cnt1 = fd.find_fiducials(img1, 0.5, 5, 100)
img1_cnt2 = fd.find_fiducials(img1, 1.5, 5, 100)
img1_cnt2 = fd.find_fiducials(img1, 1.0, 5, 100)
img1_cnt3 = fd.find_fiducials(img1, 1.5, 5, 100)
ax1.plot(img1_cnt1[:,0], img1_cnt1[:,1], 'r.')
ax1.plot(img1_cnt2[:,0], img1_cnt2[:,1], 'g.')
ax1.plot(img1_cnt3[:,0], img1_cnt3[:,1], 'b.')
ax1.imshow(img1.getchannel('R'), cmap='gray')
img2_cnt1 = fd.find_fiducials(img2, 0.5, 5, 100)
img2_cnt2 = fd.find_fiducials(img2, 1.0, 5, 100)
img2_cnt3 = fd.find_fiducials(img2, 1.5, 5, 100)
ax2.plot(img2_cnt1[:,0], img2_cnt1[:,1], 'r.')
ax2.plot(img2_cnt2[:,0], img2_cnt2[:,1], 'g.')
ax2.plot(img2_cnt3[:,0], img2_cnt3[:,1], 'b.')
ax2.imshow(img2.getchannel('R'), cmap='gray')
img1_cnt1 = fd.find_fiducials(img1, 0.8, 10, 50)
img1_cnt2 = fd.find_fiducials(img1, 1.0, 10, 50)
img1_cnt3 = fd.find_fiducials(img1, 1.2, 10, 50)
img2_cnt1 = fd.find_fiducials(img2, 0.8, 10, 50)
img2_cnt2 = fd.find_fiducials(img2, 1.0, 10, 50)
img2_cnt3 = fd.find_fiducials(img2, 1.2, 10, 50)
ax1.clear()
ax2.clear()
ax1.plot(img1_cnt1[:,0], img1_cnt1[:,1], 'r.')
ax1.plot(img1_cnt2[:,0], img1_cnt2[:,1], 'g.')
ax1.plot(img1_cnt3[:,0], img1_cnt3[:,1], 'b.')
ax1.imshow(img1.getchannel('R'), cmap='gray')
ax2.plot(img2_cnt1[:,0], img2_cnt1[:,1], 'r.')
ax2.plot(img2_cnt2[:,0], img2_cnt2[:,1], 'g.')
ax2.plot(img2_cnt3[:,0], img2_cnt3[:,1], 'b.')
ax2.imshow(img2.getchannel('R'), cmap='gray')
type(img1_cnt1)
for i, point in enumerate(img1_cnt1):
    print(1, point)
    
img1_cnt1.size
for i, point in enumerate(img1_cnt1):
    print(i, point)
    
np.sqrt(4)
quit()
get_ipython().run_line_magic('logstart', './ipython_session.py append')
get_ipython().run_line_magic('matplotlib', '')
get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')
get_ipython().run_line_magic('clear', '')
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image
import filmdosimetry as fd
img1 = Image.open('./test_film_1.png')
img2 = Image.open('./test_film_2.tiff')
img1_cnt1 = fd.find_fiducials(img1, 0.8, 10, 50)
img1_cnt1
enumerate_neighbors(img1_cnt, 50)
enumerate_neighbors(img1_cnt, 50)
quit()
get_ipython().run_line_magic('logstart', './ipython_session.py append')
get_ipython().run_line_magic('matplotlib', '')
get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')
get_ipython().run_line_magic('clear', '')
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image
import filmdosimetry as fd
img1 = Image.open('./test_film_1.png')
img2 = Image.open('./test_film_2.tiff')
img1_cnt1 = fd.find_fiducials(img1, 0.8, 10, 50)
enumerate_neighbors(img1_cnt, 50)
fd.enumerate_neighbors(img1_cnt, 50)
fd.enumerate_neighbors(img1_cnt1, 50)
fd.enumerate_neighbors(img1_cnt1, 50)
img1_cnt1
img1_cnt1.shape
img1_cnt1.shape
fd.enumerate_neighbors(img1_cnt1, 50)
pow(2, 2)
pow(3, 2)
fd.enumerate_neighbors(img1_cnt1, 50)
img1_cnt1
fd.enumerate_neighbors(img1_cnt1, 50)
fd.enumerate_neighbors(img1_cnt1, 100)
fd.enumerate_neighbors(img1_cnt1, 1000)
img1_cnt1
fd.enumerate_neighbors(img1_cnt1, 50)
fd.enumerate_neighbors(img1_cnt1, 100)
fd.enumerate_neighbors(img1_cnt1, 50)
img1_cnt1
fd.enumerate_neighbors(img1_cnt1, 50)
fd.enumerate_neighbors(img1_cnt1, 50)
img1_cnt1 = fd.find_fiducials(img1, 0.8, 10, 50)
fd.enumerate_neighbors(img1_cnt1, 50)
img1_cnt2 = fd.find_fiducials(img1, 1.0, 10, 50)
fd.enumerate_neighbors(img1_cnt2, 50)
img1_cnt3 = fd.find_fiducials(img1, 1.2, 10, 50)
fd.enumerate_neighbors(img1_cnt3, 50)
img1_cnt2
img1_cnt3
img1_cnt1 = fd.find_fiducials(img1, 1.0, 10, 50)
img1_cnt2 = fd.find_fiducials(img1, 1.1, 10, 50)
fd.enumerate_neighbors(img1_cnt1, 50)
fd.enumerate_neighbors(img1_cnt2, 50)
img1_cnt1
img1_cnt2
img2_cnt1 = fd.find_fiducials(img2, 1.0, 10, 50)
img2_cnt2 = fd.find_fiducials(img2, 1.1, 10, 50)
img2_cnt1
img2_cnt2
fd.enumerate_neighbors(img2_cnt1, 30)
fd.enumerate_neighbors(img2_cnt2, 30)
sort(fd.enumerate_neighbors(img2_cnt2, 30))
fd.enumerate_neighbors(img2_cnt2, 30).sort()
img2_cnt2.sort()
img2_cnt2
img2_cnt1.sort()
img2_cnt1
vals, counts = np.unique(fd.enumerate_neighbors(img1_cnt1, 50), return_counts=True)
vals
counts
vals, counts = np.unique(fd.enumerate_neighbors(img1_cnt1, 50)[:,1], return_counts=True)
vals
counts
vals, counts = np.unique(fd.enumerate_neighbors(img1_cnt2, 50)[:,1], return_counts=True)
vals
counts
vals, counts = np.unique(fd.enumerate_neighbors(img2_cnt1, 30)[:,1], return_counts=True)
vals
vals, counts = np.unique(fd.enumerate_neighbors(img2_cnt2, 30)[:,1], return_counts=True)
vals
img1_cnt1
fd.enumerate_neighbors(img1_cnt1, 50)
fd.enumerate_neighbors(img1_cnt1, 50)
fd.enumerate_neighbors(img1_cnt1, 50)
fd.enumerate_neighbors(img1_cnt2, 50)
vals, counts = np.unique(fd.enumerate_neighbors(img1_cnt1, 50), return_counts=True)
vals
vals, counts = np.unique(fd.enumerate_neighbors(img2_cnt1, 30), return_counts=True)
fd.enumerate_neighbors(img2_cnt1, 30)
fd.enumerate_neighbors(img2_cnt2, 30)
vals, counts = np.unique(fd.enumerate_neighbors(img1_cnt1, 50)[:,0], return_counts=True)
vals
set(fd.enumerate_neighbors(img2_cnt2, 30))
set(fd.enumerate_neighbors(img2_cnt2, 30))
fd.enumerate_neighbors(img2_cnt2, 30)
fd.enumerate_neighbors(img2_cnt1, 30)
result = fd.enumerate_neighbors(img2_cnt1, 30)
result.sort()
result
result = set()
for point in fd.enumerate_neighbors(img2_cnt1, 30):
    result.append(point)
    
for point in fd.enumerate_neighbors(img2_cnt1, 30):
    result.add(point)
    
for point in fd.enumerate_neighbors(img2_cnt1, 30):
    result.add((point))
    
a = set()
a.add(1.0)
a.add(2.0)
a.add(3.0)
a.add(2.0)
a
fd.enumerate_neighbors(img2_cnt1, 30)
a = set()
for point in fd.enumerate_neighbors(img2_cnt1, 30):
    if point[0] not in a:
        a.add(point[0])
        print(point)
        
find_fiducials(img1, 1.0, 10, 50)
fd.find_fiducials(img1, 1.0, 10, 50)
fd.find_fiducials(img2, 1.0, 10, 50)
img1_fids = fd.find_fiducials(img1, 1.0, 10, 50)
img2_fids = fd.find_fiducials(img2, 1.0, 10, 50)
fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.plot(img1_fids[:,0], img1_fids[:,1], 'g.')
ax2.plot(img2_fids[:,0], img2_fids[:,1], 'g.')
ax1.imshow(img1)
ax2.imshow(img2)
ax1.imshow(img1, cmap='gray')
ax2.imshow(img2, cmap='gray')
fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.plot(img1_fids[:,0], img1_fids[:,1], 'g.')
ax2.plot(img2_fids[:,0], img2_fids[:,1], 'g.')
ax1.imshow(img1, cmap='gray')
ax2.imshow(img2, cmap='gray')
ax1.imshow(img1.getchannel('R'), cmap='gray')
ax2.imshow(img2.getchannel('R'), cmap='gray')
quit()
get_ipython().run_line_magic('logstart', './ipython_session.py append')
get_ipython().run_line_magic('matplotlib', '')
get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')
get_ipython().run_line_magic('clear', '')
from matplotlib import pyplot as plt
import cv2
img = cv2.imread('./test_film_1.png', 0)
plt.imshow(img)
img2 = cv2.imread('./test_film_2.tiff', 0)
plt.imshow(img2)
plt.imshow(img, cmap='gray')
plt.imshow(img2, cmap='gray')
quit()
