class TVLDataset(object):
    """An abstract base class to hold TVL values and material densities for
    the IAEA SRS47 protocol and NCRP151 protocol for a given material (concrete,
    steel and lead).
    """

    def __init__(self, density: float, primary: dict, leakage: dict):

        # Ensure that appropriate values are provided.
        if density is None or primary is None or leakage is None:
            raise TypeError('Object can not be initialized with' +
                    '\"None\" value.')

        self._density = density
        self._primary = primary
        self._leakage = leakage

    @property
    def density(self):
        """Give information on material density in g/cm^3.
        """

        return self._density


class IAEA_TVLDataset(TVLDataset):
    """Container class to hold IAEA SRS47 protocl TVL datasets.

    On initialization density must be specified in g/cm^3 while energiey-TVL
    values must be specified in MV and cm respectively. Also energy-TVL values
    must be given as dictionary where energy is given as key and
    TVL as value, e.g.:

        {1.25: 21.8, 4: 29.0, 6: 34.3, 10: 38.9, 15: 43.2, 18: 44.5, 20: 45.7}
    """

    def show_primary(self):
        """Display dictionary containg energy-TVL pairs for primary beam.
        Energies are given in MV and TVLs in cm.
        """

        print(self._primary)

    def primary(self, energy):
        """Answer TVL value in cm for primary beam and given megavoltage energy.
        """

        if energy not in self._primary.keys():
            raise ValueError(
                    'Energy {0} MV not in or out of range.'.format(energy)
                )

        return self._primary[energy]

    def show_leakage(self):
        """Display dictionary containg energy-TVL pairs for leakage radiation.
        Energies are given in MV and TVLs in cm.
        """

        print(self._leakage)

    def leakage(self, energy):
        """Answer TVL value in cm for leakage radiation and given
        megavoltage energy.
        """

        if energy not in self._leakage.keys():
            raise ValueError(
                    'Energy {0} MV not in or out of range.'.format(energy)
                )

        return self._leakage[energy]


class NCRC_TVLDataset(object):
    """Container class to hold NCRC151 protocl TVL datasets.

    On initialization density must be specified in g/cm^3 while energiey-TVL
    values must be specified in MV and cm respectively. Also energy-TVL values
    must be given as dictionary where energy is given as key and
    TVL tuple as value, where first value of a tuple represent TVL1 and second
    one represents TVLe. E.g.:

        {1.25: (21.8, 29.0), 4: (34.3, 38.9), 6: (43.2, 44.5)}
    """

    def show_primary_one(self):
        """Display dictionary containg energy-TVL pairs for primary beam.
        Energies are given in MV and TVL1s in cm.
        """

        primary_one = {}

        for k in self._primary.keys():
            primary_one[k] = self.primary[k][0]

        print(primary_one)

    def primary_one(self, energy):
        """Answer TVL1 value in cm for primary beam and given
        megavoltage energy.
        """

        if energy not in self._primary.keys():
            raise ValueError(
                    'Energy {0} MV not in or out of range.'.format(energy)
                )

        return self._leakage[energy][0]

    def show_primary_e(self):
        """Display dictionary containg energy-TVL pairs for primary beam.
        Energies are given in MV and TVLes in cm.
        """

        primary_e = {}

        for k in self._primary.keys():
            primary_e[k] = self.primary[k][1]

        print(primary_e)

    def primary_e(self, energy):
        """Answer TVLe value in cm for primary beam and given
        megavoltage energy.
        """

        if energy not in self._primary.keys():
            raise ValueError(
                    'Energy {0} MV not in or out of range.'.format(energy)
                )

        return self._leakage[energy][1]

    def show_leakage_one(self):
        """Display dictionary containg energy-TVL pairs for primary beam.
        Energies are given in MV and TVL1s in cm.
        """

        leakage_one = {}

        for k in self._leakage.keys():
            leakage_one[k] = self.leakage[k][0]

        print(leakage_one)

    def leakage_one(self, energy):
        """Answer TVL1 value in cm for leakage radiation and given
        megavoltage energy.
        """

        if energy not in self._leakage.keys():
            raise ValueError(
                    'Energy {0} MV not in or out of range.'.format(energy)
                )

        return self._leakage[energy][0]

    def show_leakage_e(self):
        """Display dictionary containg energy-TVL pairs for primary beam.
        Energies are given in MV and TVL1s in cm.
        """

        leakage_e = {}

        for k in self._leakage.keys():
            leakage_e[k] = self.leakage[k][1]

        print(leakage_e)

    def leakage_e(self, energy):
        """Answer TVLe value in cm for leakage radiation and given
        megavoltage energy.
        """

        if energy not in self._leakage.keys():
            raise ValueError(
                    'Energy {0} MV not in or out of range.'.format(energy)
                )

        return self._leakage[energy][1]


iaea_concrete = IAEA_TVLDataset(
        density=2.35,
        primary={1.25: 21.8,
            4: 29.0,
            6: 34.3,
            10: 38.9,
            15: 43.2,
            18: 44.5,
            20: 45.7,
            24: 47.0},
        leakage={1.25: 21.8,
            4: 25.4,
            6: 27.9,
            10: 30.5,
            15: 33.0,
            18: 33.0,
            20: 34.3,
            24: 35.6}
        )

iaea_steel = IAEA_TVLDataset(
        density=7.8,
        primary={1.25: 71.0,
            4: 91.0,
            6: 98.0,
            10: 10.5,
            15: 10.8,
            18: 11.1,
            20: 11.1,
            24: 10.7},
        leakage={1.25: 69.0,
            4: 79.0,
            6: 80.0,
            10: 85.5,
            15: 87.0,
            18: 87.0,
            20: 88.0,
            24: 89.0}
        )

iaea_lead = IAEA_TVLDataset(
        density=11.36,
        primary={1.25: 41.0,
            4: 53.0,
            6: 55.0,
            10: 56.0,
            15: 57.0,
            18: 56.0,
            20: 55.0,
            24: 52.0},
        leakage={1.25: 40.0,
            4: 47.0,
            6: 45.0,
            10: 46.0,
            15: 47.0,
            18: 47.0,
            20: 49.0,
            24: 51.0}
        )

ncrc_concrete = NCRC_TVLDataset(
        density=2.35,
        primary={1.25: (21.0, 21.0),
            4: (35.0, 30.0),
            6: (37.0, 33.0),
            10: (41.0, 37.0),
            15: (44.0, 41.0),
            18: (45.0, 43.0),
            20: (46.0, 44.0),
            25: (49.0, 46.0),
            30: (51.0, 49.0)},
        leakage={}
#        leakage={1.25: (21.0, 21.0), 4: (33.0, 28.0), 6: (34.0, 29.0), 10: (35.0, 31.0), 15: (36.0, 33.0), 18: (36.0, 34.0), 20: (36.0, 34.0), 25: (37.0, 35.0), 30: (37.0, 36.0)}
        )

#ncrc_steel = NCRC_TVLDataset(
#        density=7.87,
#        primary={1.25: (7.0, 7.0),
#            4: (9.9, 9.9),
#            6: (10.0, 10.0),
#            10: (11.0, 11.0),
#            15: (11.0, 11.0),
#            18: (11.0, 11.0),
#            20: (11.0, 11.0),
#            25: (11.0, 11.0),
#            30: (11.0, 11.0)},
#        leakage={0.0: (0.0, 0.0)}
#        )

#ncrc_lead = NCRC_TVLDataset(
#        density=11.35,
#        primary={1.25: (4.0, 4.0),
#            4: (5.7, 5.7),
#            6: (5.7, 5.7),
#            10: (5.7, 5.7),
#            15: (5.7, 5.7),
#            18: (5.7, 5.7),
#            20: (5.7, 5.7),
#            25: (5.7, 5.7),
#            30: (5.7, 5.7)},
#        leakage={0.0: (0.0, 0.0)}
#        )