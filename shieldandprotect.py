from math import log10

class TVLDataset(object):
    """An base class to hold TVL values and material densities for the IAEA
    SRS47 protocol and NCRP151 protocol for a given material (concrete, steel
    and lead).
    """

    def __init__(self,
            label: str,
            density: float,
            primary: dict,
            leakage: dict):

        # Ensure that appropriate values are provided.
        if label is None \
                or density is None \
                or primary is None \
                or leakage is None:
            raise TypeError('Object can not be initialized with' +
                    '\"None\" value.')

        self._label = label
        self._density = density
        self._primary = primary
        self._leakage = leakage

    @property
    def density(self):
        """Give information on material density in g/cm^3.
        """

        return self._density


class IAEA_TVLDatasetReport(object):
    """Class to format and print report from given TVL dataset.
    """

    def __init__(self, dataset: IAEA_TVLDataset):
        self._dataset = dataset
        self._report = None

    def _format_report(self):
        self._report = 'material label: {0}\n\
                material density: {1}\n'.format()

    def print_report(self):
        self._format_report()
        print(self._report)


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


class NCRC_TVLDataset(TVLDataset):
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
            primary_one[k] = self._primary[k][0]

        print(primary_one)

    def primary_one(self, energy):
        """Answer TVL1 value in cm for primary beam and given
        megavoltage energy.
        """

        if energy not in self._primary.keys():
            raise ValueError(
                    'Energy {0} MV not in or out of range.'.format(energy)
                )

        return self._primary[energy][0]

    def show_primary_e(self):
        """Display dictionary containg energy-TVL pairs for primary beam.
        Energies are given in MV and TVLes in cm.
        """

        primary_e = {}

        for k in self._primary.keys():
            primary_e[k] = self._primary[k][1]

        print(primary_e)

    def primary_e(self, energy):
        """Answer TVLe value in cm for primary beam and given
        megavoltage energy.
        """

        if energy not in self._primary.keys():
            raise ValueError(
                    'Energy {0} MV not in or out of range.'.format(energy)
                )

        return self._primary[energy][1]

    def show_leakage_one(self):
        """Display dictionary containg energy-TVL pairs for primary beam.
        Energies are given in MV and TVL1s in cm.
        """

        leakage_one = {}

        for k in self._leakage.keys():
            leakage_one[k] = self._leakage[k][0]

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
            leakage_e[k] = self._leakage[k][1]

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
        label='IAEA Concrete',
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
        label='IAEA Steel',
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
        label='IAEA Lead',
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
        label='NCRC concrete',
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
        leakage={1.25: (21.0, 21.0),
            4: (33.0, 28.0),
            6: (34.0, 29.0),
            10: (35.0, 31.0),
            15: (36.0, 33.0),
            18: (36.0, 34.0),
            20: (36.0, 34.0), 
            25: (37.0, 35.0),
            30: (37.0, 36.0)}
        )

ncrc_steel = NCRC_TVLDataset(
        label='NCRC steel',
        density=7.87,
        primary={1.25: (7.0, 7.0),
            4: (9.9, 9.9),
            6: (10.0, 10.0),
            10: (11.0, 11.0),
            15: (11.0, 11.0),
            18: (11.0, 11.0),
            20: (11.0, 11.0),
            25: (11.0, 11.0),
            30: (11.0, 11.0)},
        leakage={0.0: (0.0, 0.0)}
        )

ncrc_lead = NCRC_TVLDataset(
        label='NCRC lead',
        density=11.35,
        primary={1.25: (4.0, 4.0),
            4: (5.7, 5.7),
            6: (5.7, 5.7),
            10: (5.7, 5.7),
            15: (5.7, 5.7),
            18: (5.7, 5.7),
            20: (5.7, 5.7),
            25: (5.7, 5.7),
            30: (5.7, 5.7)},
        leakage={0.0: (0.0, 0.0)}
        )


class PrimaryBarrierGoal(object):
    """An base class for calculation of transmission factor, number of TVLs and
    primary barrier thickness for the IAEA SRS47 protocol and NCRP151 protocol
    for a given shielding design goal, beam energy and material.

    goal      - shielding design goal (P) beyond the barrier given in Sv/week;
    distance  - distance (dpri) from the x-ray target to the point protected
                given in meters;
    sad       - source to axes distance (SAD) given in meters. Usually 1.0 m;
    workload  - workload (W) or photon absorbed dose delivered at 1.0 m from the
                x-ray target given in Gy/week;
    usage     - usage factor (U) or fraction of the workload that primary beam is
                directed at the barrier in question;
    occupancy - occupancy factor (T) for the protected location or fraction of
                the workweek that a person is present beyond the barrier.
    material  - material used for barrier. Usually ordinary concrete. For
                laminated barriers calculation differs. Use given predefined
                material objects;
    energy    - energy of the primary beam field given in megavolts (MV).

    """

    def __init__(
            self,
            goal: float,
            distance: float,
            sad: float,
            workload: float,
            usage: float,
            occupancy: float,
            material: IAEA_TVLDataset,
            energy: float
        ):

        self._goal = goal
        self._distance = distance
        self._sad = sad
        self._workload = workload
        self._usage = usage
        self._occupancy = occupancy
        self._material = material
        self._energy = energy

    @property
    def transmission(self):
        """ Calculates transmission factor (Bpri) for given shielding design
        goal, material and beam energy.
        """

        numerator = self._goal * pow((self._distance + self._sad), 2)
        denominator = self._workload * self._usage * self._occupancy
        return numerator / denominator

    @property
    def tvl_number(self):
        """ Calculates required number of TVLs (n) needed to achieve given
        shielding design goal.
        """

        return log10(1.0 / self.transmission)

    @property
    def barrier_thickness(self):
        """ An abstract property. Must be defiend in the proper subclass.
        """

        pass


class IAEA_PrimaryBarrierGoal(PrimaryBarrierGoal):
    """An class for calculation of transmission factor, number of TVLs and
    primary barrier thickness for the IAEA SRS47 protocol for a given shielding
    design goal, beam energy and material.
    """

    @property
    def barrier_thickness(self):
        """ Calculates required primary barrier thickness (tpri) needed to
        achieve given shielding design goal.
        """

        return self.tvl_number() * self._material.primary(self._energy)


class NCRC_PrimaryBarrierGoal(PrimaryBarrierGoal):
    """An class for calculation of transmission factor, number of TVLs and
    primary barrier thickness for the IAEA SRS47 protocol for a given shielding
    design goal, beam energy and material.
    """

    @property
    def barrier_thickness(self):
        """ Calculates required primary barrier thickness (tpri) needed to
        achieve given shielding design goal.
        """

        tpri = self._material.primary_one(self._energy) + \
                ((self.tvl_number - 1.0) * \
                self._material.primary_e(self._energy))

        return tpri

    @property
    def barrier_thickness_cnsrv(self):
        """ Calculates required primary barrier thickness (tpri) needed to
        achieve given shielding design goal without taking into consideration
        the spectral changes in the radiation as it penetrates the barrier.

        Note that this approach is more conservative than when you take into
        account spectral changes in the radiation.
        """

        return self._material.primary_one(self._energy) * self.tvl_number
