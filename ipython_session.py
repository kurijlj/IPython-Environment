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
