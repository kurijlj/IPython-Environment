# -*- coding: utf-8 -*-
from collections import namedtuple
import matplotlib.patches as ptchs
import numpy as np
import math as m


# Define user datatypes
ArrowLine = namedtuple('ArrowLine',
                       ['x1', 'y1', 'x2', 'y2', 'lbl_x', 'lbl_y', 'style'])


def t1_relax(t, amp, to):
    """Calculates value of the longitudinal magnetization decay.
      @t: Float representing point in time for which to calculate value of
          longitudinal magnetization decay.
    @amp: Float representing T1 longitudinal magnetization amplitude.
     @to: Float representing tissue's T1 relaxation time.
    Returns: Default
    """

    return amp*(1 - (2 * m.exp(-(t/to))))


def t2_relax(t, tt):
    """Calculates value of the transversal magnetization decay.
      @t: Float representing point in time for which to calculate value of
          transverzal magnetization decay.
     @tt: Float representing tissue's T2 relaxation time.
    Returns: Default
    """

    return m.exp(-(t/tt))


def linear_rise(x, m, b):
    """Calculates linear rise for given value run, slope/gradient and
    y-intercept.
    @x: Run value for which to calculate raise.
    @m: Slope/gradient of line.
    @b: y-intercept of a line.
    """

    return (m * x) + b


def t1_relax_plot(ax, rng, amp, toa, tob, tro, trt):
    """Plots figure elements for T1 relaxation graph.
     @ax: An Axes object to put figure elements on.
    @rng: Float representing upper data bound.
    @amp: Float representing T1 longitudinal magnetization amplitude.
    @toa: Float representing first's tissue T1 relaxation time.
    @tob: Float representing second's tissue T1 relaxation time.
    @tro: Float representing first TR constant (good contrast).
    @tro: Float representing second TR constant (bad contrast).
    Returns: Default
    """

    # Generate plot data
    x = np.arange(0, rng, 0.05)
    y1 = np.array([t1_relax(t, amp, toa) for t in x])
    y2 = np.array([t1_relax(t, amp, tob) for t in x])

    # Set axis labels
    ax.set_xlabel(r'Vreme [$t/T_1$]')
    ax.set_ylabel(u'Relaksacija longitudinalne magnetizacije $M_z$')

    # Set TR constants distinctable
    ax.axvline(tro, 0, 1, ls='dashed')
    ax.axvline(trt, 0, 1, ls='dashed')

    # Set time axis line more distinct
    ax.axhline(0, 0, 1, color='black')

    # Set longitudinal magnetization limits distinctable
    ax.axhline(-amp, 0, 1, ls='dashed')
    ax.axhline(amp, 0, 1, ls='dashed')

    # Set grid and minor ticks on for better presentation
    ax.grid('on')
    ax.minorticks_on()

    # Plot data curves
    ax.plot(x, y1, label='$T_{1a}$', color='#d358ae', linewidth=3)
    ax.plot(x, y2, label='$T_{1b}$', color='#aed358', linewidth=3)

    # Plot additional info to legend
    ax.plot([], [], ' ', label=r'$T_{1a}<T_{1b}$')

    # Set axis major ticks
    xt = [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0]
    yt = [-1.00, -0.75, -0.50, -0.25, 0.00, 0.25, 0.50, 0.75, 1.0]
    ax.set_xticks(xt)
    ax.set_yticks(yt)

    # Set ticks labels. Remove all labels and leave just most relevan ones
    # (positions of TR1, TR2, -Mz, +Mz)
    xtl = [r'', r'', r'$TR_1$', r'', r'', r'', r'$TR_2$', r'', r'']
    ytl = [r'$-M_0$', r'', r'', r'', r'$0.0$', r'', r'', r'', r'$M_0$']
    ax.set_xticklabels(xtl)
    ax.set_yticklabels(ytl)

    # Set graph limits so it looks like curves are expanding beyond graph and
    # into infinity
    xlims = ax.get_xlim()
    ax.set_xlim(xlims[0], rng)

    # Set arrow lines and labels illustrating what is achieved with proper TR
    # times. Position of the first arrow line and label is alongside t=tro,
    # while position of the second arrow line and label is alongside t=trt.
    arrlno = ArrowLine(tro,
                       round(t1_relax(tro, amp, tob), 2) - 0.02,
                       tro,
                       round(t1_relax(tro, amp, toa), 2) + 0.02,
                       tro + 0.1,
                       round(t1_relax(tro, amp, tob) +
                             (t1_relax(tro, amp, toa) -
                             t1_relax(tro, amp, tob)) / 2, 2),
                       style='<->')
    arrlnt = ArrowLine(trt,
                       round(t1_relax(trt, amp, tob), 2) - 0.02,
                       trt,
                       round(t1_relax(trt, amp, toa), 2) + 0.02,
                       trt + 0.1,
                       round(t1_relax(trt, amp, tob) +
                             (t1_relax(trt, amp, toa) -
                             t1_relax(trt, amp, tob)) / 2, 2),
                       style='<->')

    # Draw first arrow line and set label (t=tro)
    ax.annotate('',
                xy=(arrlno.x2, arrlno.y2),
                xytext=(arrlno.x1, arrlno.y1),
                arrowprops=dict(arrowstyle=arrlno.style))
    ax.text(arrlno.lbl_x,
            arrlno.lbl_y,
            u'Dobar\nkontrast',
            weight='bold',
            size='large',
            verticalalignment='center')

    # Draw second arrow line and set label (t=trt)
    ax.annotate('',
                xy=(arrlnt.x2, arrlnt.y2),
                xytext=(arrlnt.x1, arrlnt.y1),
                arrowprops=dict(arrowstyle=arrlnt.style))
    ax.text(arrlnt.lbl_x,
            arrlnt.lbl_y,
            u'Loš\nkontrast',
            weight='bold',
            size='large',
            verticalalignment='center')
    ax.legend()


def t2_relax_plot(ax, rng, tta, ttb, teo, tet):
    """Plots figure elements for T2 relaxation graph.
     @ax: An Axes object to put figure elements on.
    @rng: Float representing upper data bound.
    @tta: Float representing first's tissue T2 relaxation time.
    @ttb: Float representing second's tissue T2 relaxation time.
    @teo: Float representing first TE constant (bad contrast).
    @teo: Float representing second TE constant (good contrast).
    Returns: Default
    """

    # Generate plot data
    x = np.arange(0, rng, 0.05)
    y1 = np.array([t2_relax(t, tta) for t in x])
    y2 = np.array([t2_relax(t, ttb) for t in x])

    # Set axis labels
    ax.set_xlabel(r'Vreme')
    ax.set_ylabel(u'Relaksacija transferzalne magnetizacije $M_{xy}$')

    # Set TE constants distinctable
    ax.axvline(teo, 0, 1, ls='dashed')
    ax.axvline(tet, 0, 1, ls='dashed')

    # Set transversal magnetization amplitude more distinct
    ax.axhline(1.0, 0, 1, ls='dashed')

    # Set axis lines more distinct
    ax.axhline(0, 0, 1, color='black')
    ax.axvline(0, 0, 1, color='black')

    # Set grid and minor ticks on for better presentation
    ax.grid('on')
    ax.minorticks_on()

    # Plot data curves
    ax.plot(x, y1, label='$T_{2a}$', color='#d358ae', linewidth=3)
    ax.plot(x, y2, label='$T_{2b}$', color='#aed358', linewidth=3)

    # Plot additional info to legend
    ax.plot([], [], ' ', label=r'$T_{2a}<T_{2b}$')

    # Set axis major ticks
    xt = [0.0, 0.4, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0]
    yt = [0.00, 0.20, 0.40, 0.60, 0.80, 1.00]
    ax.set_xticks(xt)
    ax.set_yticks(yt)

    # Set ticks labels. Remove all labels and leave just most relevan ones
    # (positions of TE1, TE2)
    xtl = [r'', r'$TE_1$', r'', r'', r'$TE_2$', r'', r'', r'', r'', r'']
    ytl = [r'', r'', r'', r'', r'', r'$M_0$']
    ax.set_xticklabels(xtl)
    ax.set_yticklabels(ytl)

    # Set graph limits so it looks like curves are expanding beyond graph and
    # into infinity
    xlims = ax.get_xlim()
    ax.set_xlim(xlims[0], rng)

    # Set arrow lines and labels illustrating what is achieved with proper TR
    # times. Position of the first arrow line and label is alongside t=tro,
    # while position of the second arrow line and label is alongside t=trt.
    arrlno = ArrowLine(teo,
                       round(t2_relax(teo, tta), 2) - 0.02,
                       teo,
                       round(t2_relax(teo, ttb), 2) + 0.02,
                       teo + 0.1,
                       round(t2_relax(teo, tta) +
                             (t2_relax(teo, ttb) -
                             t2_relax(teo, tta)) / 2, 2),
                       style='<->')
    arrlnt = ArrowLine(tet,
                       round(t2_relax(tet, tta), 2) - 0.02,
                       tet,
                       round(t2_relax(tet, ttb), 2) + 0.02,
                       tet + 0.1,
                       round(t2_relax(tet, tta) +
                             (t2_relax(tet, ttb) -
                             t2_relax(tet, tta)) / 2, 2),
                       style='<->')

    # Draw first arrow line and set label (t=tro)
    ax.annotate('',
                xy=(arrlno.x2, arrlno.y2),
                xytext=(arrlno.x1, arrlno.y1),
                arrowprops=dict(arrowstyle=arrlno.style))
    ax.text(arrlno.lbl_x,
            arrlno.lbl_y,
            u'Loš\nkontrast',
            weight='bold',
            size='large',
            verticalalignment='center')

    # Draw second arrow line and set label (t=trt)
    ax.annotate('',
                xy=(arrlnt.x2, arrlnt.y2),
                xytext=(arrlnt.x1, arrlnt.y1),
                arrowprops=dict(arrowstyle=arrlnt.style))
    ax.text(arrlnt.lbl_x,
            arrlnt.lbl_y,
            u'Dobar\nkontrast',
            weight='bold',
            size='large',
            verticalalignment='center')
    ax.legend()


def gradient_field_plot(ax, rng, gz, bz):
    """Plots figure elements for linear magnetic field gradient graph.
     @ax: An Axes object to put figure elements on.
    @rng: Positive float value representing data range [-rng, +rng].
     @gz: Float representing slope/gradient of magnetic field.
     @bz: Float representing value B0 of constant magnetic field.
    Returns: Default
    """

    # Generate plot data
    x = np.arange(-rng, rng, 0.05)
    y = np.array([linear_rise(r, gz, bz) for r in x])

    # Set axis lines more distinct
    ax.axhline(0, 0, 1, color='black')
    ax.axvline(0, 0, 1, color='black')

    # Set grid and minor ticks on for better presentation
    ax.grid('on')
    ax.minorticks_on()

    # Fill area beneath line
    ax.fill_between(x, 0, y, color='#96caff')

    # Plot data curves
    ax.plot(x, y, linewidth=3)

    # Set axis major ticks
    xt = np.arange(-rng + 1.0, rng, 1.0).tolist()
    yt = np.arange(0.0, linear_rise(rng, gz, bz) + 0.5, 0.5).tolist()
    ax.set_xticks(xt)
    ax.set_yticks(yt)

    # Set ticks labels. Remove all labels and leave just most relevan ones
    # (positions of TE1, TE2)
    xtl = [r'$-z$', r'', r'', r'$0.0$', r'', r'', r'$+z$']
    ytl = [r'', r'', r'', r'', r'', r'', r'$B_z$']
    ax.set_xticklabels(xtl)
    ax.set_yticklabels(ytl)

    # Set graph limits so it looks like curves are expanding beyond graph and
    # into infinity
    ax.set_xlim(-rng + 0.5, rng - 0.5)
    ax.set_ylim(0, linear_rise(rng, gz, bz))

    # Draw additional graph info
    ax.text(-1.5,
            bz + 0.5,
            r'$z=0, B_z=B_0$',
            size='large',
            horizontalalignment='center')
    ax.text(round((rng - 0.5) / 2, 1),
            bz,
            r'$nagib = G_z$',
            size='large',
            horizontalalignment='center')
    ax.annotate('',
                xy=(0.0, bz),
                xytext=(-1.5, bz + 0.5),
                arrowprops=dict(arrowstyle='->',
                                connectionstyle='angle,\
                                                 angleA=-90,\
                                                 angleB=0,\
                                                 rad=0'
                                )
                )


def gtvctvptv_plot(ax):
    """Plots GTV, CTV, PTV, Treated Volume and Irradiated Volume relations
    diagram.

     @ax: An Axes object to put figure elements on.

    Returns: Default
    """

    ax.add_patch(
            ptchs.FancyBboxPatch(
                            (0.25, 0.15),
                            0.5,
                            0.7,
                            boxstyle=ptchs.BoxStyle(
                                                "Round",
                                                pad=0.02,
                                                rounding_size=0.04
                                                ),
                            fc='#3f8cc6',
                            ec='#3f48c6',
                            zorder=0
                            )
            )
    ax.add_patch(
            ptchs.FancyBboxPatch(
                            (0.3, 0.2),
                            0.4,
                            0.6,
                            boxstyle=ptchs.BoxStyle(
                                                "Round",
                                                pad=0.02,
                                                rounding_size=0.04
                                                ),
                            fc='#3fb4c6',
                            ec='#3f71c6',
                            zorder=1)
            )
    ax.add_patch(
            ptchs.Ellipse(
                        (0.5, 0.5),
                        0.35,
                        0.5,
                        fc='#c66780',
                        ec='#c67d67',
                        ls='dotted',
                        zorder=2
                        )
            )
    ax.add_patch(
            ptchs.Ellipse(
                        (0.5, 0.5),
                        0.25,
                        0.38,
                        fc='#c63f63',
                        ec='#c65f3f',
                        ls='dashed',
                        zorder=3
                        )
            )
    ax.add_patch(
            ptchs.Ellipse(
                        (0.5, 0.5),
                        0.15,
                        0.26,
                        fc='#c61746',
                        ec='#c64017',
                        zorder=4
                        )
            )
    ax.text(0.5,
            0.15,
            u'ozračeni volumen',
            size='large',
            horizontalalignment='center')
    ax.text(0.5,
            0.2,
            u'tretirani volumen',
            size='large',
            horizontalalignment='center')
    ax.text(0.5,
            0.27,
            u'PTV',
            size='large',
            horizontalalignment='center')
    ax.text(0.5,
            0.34,
            u'CTV',
            size='large',
            horizontalalignment='center')
    ax.text(0.5,
            0.5,
            u'GTV',
            size='large',
            horizontalalignment='center')
