import numpy as np
import math as m


def t1_relax_graph(ax, rng, amp, toa, tob):
    x = np.arange(0, rng, 0.05)
    y1 = np.array([amp*(1 - (2 * m.exp(-(t/toa)))) for t in x])
    y2 = np.array([amp*(1 - (2 * m.exp(-(t/tob)))) for t in x])

    ax.plot(x, y1, label='$T_{1a}$', color='#a4c122')
    ax.plot(x, y2, label='$T_{1b}$', color='#c122a4')

    ax.set_xlabel(r'Vreme [$t/T_1$]')
    ax.set_ylabel(r'Longitudinalna magnetizacija $M_z$')

    ax.axhline(-1, 0, 1, ls='dashed', label=r'$-M_0$')
    ax.axhline(1, 0, 1, ls='dashed', label=r'$+M_0$')

    ax.grid('on')
    ax.minorticks_on()
    ax.legend()
