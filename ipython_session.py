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
