#!/usr/bin/env python
# -*- coding: utf-8 -*-


class EnvConds(object):
    """
    """

    def __init__(self,
                 t: float = 20.0,
                 p: float = 101.3,
                 RH: float = 50.0,
                 ref: bool = True,
                 ):
        self._t = t
        self._p = p
        self._RH = RH
        self._ref = ref

    def __repr__(self):
        objstr = str()
        if self._ref:
            objstr = (self.__class__.__name__ +
                      ('(t0={0} 0C, p0={1} kPa, RH={2} %)'
                          .format(self._t, self._p, self._RH)))
        else:
            objstr = (self.__class__.__name__ +
                      ('(t0={0} 0C, p0={1} kPa, RH={2} %)'
                          .format(self._t, self._p, self._RH)))

        return objstr

    @property
    def t(self):
        """
        """

        return self._t

    @property
    def p(self):
        """
        """

        return self._p

    @property
    def RH(self):
        """
        """

        return self._RH

    def asdict(self):
        """
        """
        if self._ref:
            return {'t0': self._t, 'p0': self._p, 'RH': self._RH}
        else:
            return {'t': self._t, 'p': self._p, 'RH': self._RH}


class Instrument(object):
    """
    """

    def __init__(self,
                 mnfc: str = 'Unknown',
                 model: str = 'Uknown',
                 SNo: str = 'Unknown'
                 ):
        self._mnfc = mnfc
        self._model = model
        self._SNo = SNo

    @property
    def mnfc(self):
        """
        """

        return self._mnfc

    @property
    def model(self):
        """
        """

        return self._model

    @property
    def SNo(self):
        """
        """

        return self._SNo

    def asdict(self):
        """
        """

        return {'Manufacturer': self._mnfc,
                'Model': self._model,
                'Serial Number': self._SNo}
