import tkinter as tk
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import NavigationToolbar2TkAgg
from matplotlib.figure import Figure


class DosXYZShowApp(tk.Tk):
    """ A simple GUI application to show EGS phantom and 3ddose data.
    """

    def __init__(self, *args, **kwargs):

        x = kwargs.pop('dmslicesw', None)
        y = kwargs.pop('dmslicesh', None)
        p = kwargs.pop('dm3dw', None)
        q = kwargs.pop('dm3dh', None)
        bgsl = kwargs.pop('slviewbg', None)
        bg3d = kwargs.pop('view3dbg', None)

        if x is None:
            x = 200
        if y is None:
            y = 300
        if p is None:
            p = 500
        if q is None:
            q = 500
        if bgsl is None:
            bgsl = 'black'
        if bg3d is None:
            bg3d = 'black'

        self.sliceshape = (x, y)
        self.v3dshape = (p, q)
        self.bgcolors = {}
        self.bgcolors['slview'] = bgsl
        self.bgcolors['view3d'] = bg3d

        tk.Tk.__init__(self, *args, **kwargs)

        # Set app icon and window title.
        # tk.Tk.iconbitmap(self, default='dosxyz_show.ico')
        tk.Tk.wm_title(self, 'dosxyz_show.py')

        # Set viewframe and frame with all commands.
        self.viewframe = tk.Frame(self)
        self.viewframe.pack(side=tk.TOP)
        self.commandframe = tk.Frame(self)
        self.commandframe.pack(side=tk.BOTTOM)

        # Set slices view frame and 3D view frame.
        self.sliceframe = tk.Frame(self.viewframe)
        self.sliceframe.pack(side=tk.LEFT)
        self.frame3d = tk.Frame(self.viewframe)
        self.frame3d.pack(side=tk.RIGHT)

        # Set each of slices frames.
        self.frameXZ = tk.Frame(self.sliceframe)
        self.frameXZ.pack()
        self.frameYZ = tk.Frame(self.sliceframe)
        self.frameYZ.pack(side=tk.BOTTOM)
        self.frameXY = tk.Frame(self.sliceframe)
        self.frameXY.pack(side=tk.BOTTOM)

        # Set canvases.
        # canvasXZ = tk.Canvas(
        #         frameXZ,
        #         width=self.sliceshape[0],
        #         height=self.sliceshape[1]
        #     )
        # canvasXZ.pack()
        # canvasYZ = tk.Canvas(
        #         frameYZ,
        #         width=self.sliceshape[0],
        #         height=self.sliceshape[1]
        #     )
        # canvasYZ.pack()
        # canvasXY = tk.Canvas(
        #         frameXY,
        #         width=self.sliceshape[0],
        #         height=self.sliceshape[1]
        #     )
        # canvasXY.pack()
        # canvas3d = tk.Canvas(
        #         frame3d,
        #         width=self.v3dshape[0],
        #         height=self.v3dshape[1]
        #     )
        # canvas3d.pack()

        # Configure canvases
        # canvasXZ.config(background=self.bgcolors['slview'])
        # canvasYZ.config(background=self.bgcolors['slview'])
        # canvasXY.config(background=self.bgcolors['slview'])
        # canvas3d.config(background=self.bgcolors['view3d'])

        # Set commands
        button = tk.Button(self.commandframe, text='Command')
        button.pack()

        fig = plt.figure()
        canvas = FigureCanvasTkAgg(fig, master=self.frameXZ)
        toolbar = NavigationToolbar2TkAgg(canvas, self.frameXZ)
        # canvas.get_tk_widget().grid(row=2, column=1)
        # toolbar.grid(row=6, column=1)


# Instance app and run the mainloop.
app = DosXYZShowApp()
app.mainloop()
