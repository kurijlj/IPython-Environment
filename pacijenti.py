from pprint import pprint
from collections import defaultdict
import re

meseci = {'januar', 'februar', 'mart', 'april', 'maj', 'jun', 'jul', 'avgust',
          'septembar', 'oktobar', 'novembar', 'decembar'}

diagnoses = {'adenoma', 'apc', 'astrocitoma', 'cavernom', 'fcp', 'glomus',
             'hipofiza', 'hypop', 'menin', 'menineg', 'menineoma', 'mening',
             'neuralg', 'neurinom', 'neurofibr', 'pcu', 'swanom', 'swanoma',
             'tunstatooct', 'turegoct'}

lastnames = {'aleksic', 'andonov', 'arsic', 'arsov', 'bakocevic', 'bakrac',
            'belancic', 'biculjevic', 'biljana', 'biserka', 'blagojevic',
            'bogdanovic', 'bogicevic', 'bogosavljevic', 'bogucanin', 'bojcuk',
            'bojinov', 'bojovic', 'bosic', 'bozic', 'bratkova', 'brkljac',
            'cakic', 'cavic', 'cekeljic', 'celekelic', 'ceman', 'ciganovic',
            'cirkovic', 'corovic', 'curovic', 'cvertkov', 'cveticanin',
            'cvetkovic', 'cvijanovic', 'cvijetic', 'cvjetic', 'dacic',
            'damnjanovic', 'danicic', 'dargan', 'dedic', 'dejanovic', 'delic',
            'dimitric', 'dimitrijevic', 'dimkovic', 'dinic', 'divic', 'djeric',
            'djevori', 'djindjic', 'djokic', 'djokovic', 'djordjevic',
            'djukanovic', 'djuran', 'djurdjevic', 'djuric', 'dobrijevic',
            'dodos', 'dostanic', 'drakulic', 'draskovic', 'drobmjakovic',
            'dubajic', 'dulovic', 'dusan', 'erdeljan', 'eric', 'etves',
            'filipovic', 'gacesa', 'galetin', 'gardasevic', 'gardijan',
            'gavrilovic', 'gligoric', 'glisic', 'glusinac', 'grabez',
            'gudzevic', 'hajdukovic', 'hajradin', 'hamsa', 'horgas', 'ilic',
            'jablanovic', 'jacimovski', 'jaglicic', 'jaksic', 'jancic',
            'janjic', 'jankovic', 'jasnic', 'jelenkovic', 'jevernica',
            'jevtic', 'jevtovic', 'jocovic', 'joksimovic', 'jovancevic',
            'jovanov', 'jovanovic', 'jovic', 'jovicic', 'kalajdzic',
            'karanovic', 'karatosic', 'karic', 'katarina', 'kefi', 'kikovic',
            'kirjakovic', 'klecin', 'knezevic', 'kocic', 'kocka', 'kojic',
            'kordic', 'kostadinovski', 'kostic', 'kovac', 'kovacevic',
            'kozomara', 'krsanac', 'krsman', 'krstic', 'krtinic', 'kunovac',
            'kuruc', 'kusic', 'latifovic', 'lekic', 'loncar', 'maksic',
            'maksimovic', 'malesevic', 'marincev', 'marinkovic', 'marinovic',
            'marjanovic', 'markovic', 'matic', 'mehmetovic', 'mihajlovic',
            'mijailovic', 'mijus', 'miladinovic', 'milanovic', 'milenkovic',
            'miletic', 'milicevic', 'milijanka', 'milja', 'miljevic',
            'milojevic', 'miloradovic', 'milosavljevic', 'milosevic',
            'miskovic', 'misovic', 'mitic', 'mitkovic', 'mitrijelovic',
            'mitrovic', 'mohamed', 'momic', 'mrdalj', 'mrsic', 'mutavdzic',
            'najdanovic', 'nemet', 'nesic', 'nestorovic', 'nikic', 'nikolic',
            'niksic', 'novakovic', 'obradovic', 'ognjenovic', 'ostojic',
            'padjen', 'palic', 'palmarovic', 'parlic', 'paunovic', 'pavlovic',
            'pejcic', 'pekez', 'pelicic', 'perencevic', 'pesic', 'petkovic',
            'petronic', 'petrovic', 'popovic', 'premovic', 'pucar', 'puskar',
            'racic', 'racipovic', 'rackovic', 'radenkovic', 'radicevic',
            'radojevic', 'radovanovic', 'radovic', 'ragipovic', 'rajak',
            'rajcevic', 'rajic', 'ramovic', 'randzic', 'rankov', 'redzovic',
            'ristanovic', 'ristic', 'ristovic', 'rosic', 'ruzicic', 'saponjic',
            'savovic', 'selakovic', 'simeunovic', 'simonovic', 'sismis',
            'skundric', 'slobodanka', 'smajilagic', 'snezana', 'sovrlic',
            'spajic', 'spasic', 'spasojevic', 'spasovski', 'sreckovic',
            'stamenic', 'stamenkovic', 'stance', 'stanisic', 'staniskovic',
            'stefanovic', 'steinfeld', 'stepanovic', 'stijacic', 'stoiljkovic',
            'stojanovic', 'stojiljkovic', 'stojisavljevic', 'stojkovic',
            'stupar', 'sutic', 'svircevic', 'tadic', 'tarabic', 'tesic',
            'tesla', 'todorovic', 'todosijevic', 'tomasevic', 'tomic', 'tosic',
            'trbovic', 'valrabenstajn', 'vasiljevic', 'velimirovic', 'vidic',
            'vlajkovic', 'vojinovic', 'vojt', 'vuckovic', 'vujaklija',
            'vukasinovic', 'vukelic', 'vukovic', 'vuksic', 'vulovic',
            'zabrdac', 'zecevic', 'zikljic', 'zivadinovic', 'zivanovic',
            'zivkovic'}

firstnames = {'adisa', 'aleksandar', 'aleksandra', 'aleksej', 'alma', 'ana',
              'andjelka', 'andrija', 'aneta', 'angelina', 'anka', 'ankica',
              'anna', 'biljana', 'bogdan', 'bogdanka', 'bojan', 'bojana',
              'borka', 'brana', 'branimir', 'branka', 'brankica', 'bratislava',
              'cvetanka', 'danica', 'danijela', 'dejan', 'desanka', 'djordje',
              'djurdjevka', 'djuro', 'dobrila', 'dobrina', 'draga', 'dragan',
              'dragana', 'dragica', 'dragoljub', 'dragoslava', 'dragutin',
              'duran', 'dusan', 'dusko', 'elvira', 'emilija', 'emir', 'fatima',
              'frosinka', 'gligorije', 'gojko', 'gordana', 'gorica',
              'grozdana', 'grujic', 'hakija', 'ilic', 'ilija', 'ilinka',
              'ilonka', 'irena', 'isakov', 'ivan', 'ivana', 'ivanka', 'izeta',
              'janja', 'janos', 'jasmina', 'jasna', 'jelena', 'jelisaveta',
              'jelka', 'jokic', 'jorgovanka', 'jovan', 'jovanka', 'katica',
              'koviljka', 'latinka', 'leposava', 'lidija', 'ljiljana',
              'ljubica', 'ljubinka', 'ljubo', 'ljubomir', 'luka', 'marica',
              'marija', 'marina', 'marko', 'mehdi', 'mihajlo', 'mikailo',
              'milan', 'mile', 'milena', 'milenka', 'milenko', 'milia',
              'milica', 'milijana', 'milivoje', 'miljana', 'milka', 'miloje',
              'milos', 'milosava', 'milovan', 'milunka', 'miodrag', 'mira',
              'mirjana', 'mirko', 'mirkov', 'miroslav', 'mitar', 'momirka',
              'nada', 'nadezda', 'nadica', 'natasa', 'nebojsa', 'nenad',
              'nevena', 'nikola', 'nikolic', 'nina', 'nurija', 'olenka',
              'olga', 'olivera', 'pajo', 'pajovic', 'peko', 'petar', 'petja',
              'predrag', 'radmila', 'radmilo', 'radojka', 'radomir',
              'radoslava', 'radovan', 'radun', 'rajka', 'rakic', 'ratka',
              'ratko', 'rodoljub', 'rosa', 'rosanda', 'rozalija', 'salih',
              'sandra', 'sasa', 'savka', 'sefida', 'sladjana', 'slavica',
              'slavisa', 'slavka', 'slavko', 'slobodan', 'slobodanka',
              'smilja', 'snezana', 'sonja', 'spasa', 'spiro', 'spomenka',
              'srbinka', 'stana', 'stanica', 'stanka', 'stanko', 'stefan',
              'svetislav', 'svetlana', 'svjetlana', 'tomislav', 'trajko',
              'veliborka', 'velinka', 'vera', 'verica', 'veroljub', 'veselin',
              'vesna', 'vezira', 'vinka', 'vladan', 'vladanka', 'vladimir',
              'vukasin', 'vukosava', 'zarko', 'zdravko', 'zivica', 'zivko',
              'zivorad', 'zivoslav', 'zoran', 'zorana', 'zorica', 'zorka'}

# 'vlajkovic', 'vuckovic', 'vuksic'

pending = {'true', 'false'}


def is_pending(s: str):
    """ pending() documentation.
    """

    if 'true' is s.lower():
        return True

    return False


# patients = []


class Patient(object):
    """Patient class documentation.
    """
    def __init__(self,
                 firstname,
                 lastname,
                 month,
                 admDate,
                 diagnosis,
                 pending,
                 rest,
                 source):
        """
        """

        self.firstname = firstname
        self.lastname = lastname
        self.month = month
        self.admDate = admDate
        self.diagnosis = diagnosis
        self.pending = pending
        self.rest = rest
        self.source = source

    def display(self):
        print('%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % (
            self.firstname,
            self.lastname,
            self.month,
            self.admDate,
            self.diagnosis,
            self.pending,
            self.rest,
            self.source))


def has_alpha(s: str):
    """Checks if given string contains word letters. It does so by converting
    given string to lower case or to upper case and comparing result with the
    original string. If given string does not contain word letters lower and
    upper case versions will match with original. If given string does contain
    word letters lower and upper case versions would differ.

    @s: string to check.

    Returns: True if string contains word letters, otherwise it returns False.
    """

    if s != s.lower() or s != s.upper():
        return True

    return False


def print_data(al):
    """ printdata() documentation.
    """

    alldg = set()

    for line in al:
        rest = line.rstrip('\n')
        tokens = rest.split(' ')
        # wt = tokens[0]
        # mt = tokens[1]
        # ln = tokens[2].lower()
        # fn = tokens[3].rstrip('-').lower()
        # firstnames.add(fn)
        dg = tokens[4].rstrip('-\n')

        if has_alpha(dg):
            alldg.add(dg.lower())

        # rs = ' '.join(tokens[4:]).rstrip('\n')
        # print('%-5s %-9s %-20s %-20s %s' % (wt, mt, ln, fn, dg))

    pprint(alldg)


def word_frequency(string: str, pstr: str = '[A-Za-z]+', cutoff: int = 0):
    """Extracts all words from a given string and counts occurence of each word.

    Default pattern for matching words is:
        '[A-Za-z]+'

       @str: String to search for a given pattern.
      @pstr: String containg regular expression pattern.
    @cutoff: Integer representing threshold cutoff string length. All strings
             that do not satisfy condition len(s) > cutoff are disregarded.
             Default value is 0.

    Returns: dictionary object which keys are words and values are number of
             occurences of a given word.
    """
    words = defaultdict(int)
    wpt = re.compile(pstr)

    for match in wpt.finditer(string):
        word = match.group(0).lower()
        words[word] += 1

    return words


def find_dates(string: str,
               pstr: str = '[0-9]([0-9]|\.)+[0-9]',
               cutoff: int = 1):
    """Find dates in a given string.

    Default pattern for matching dates is:
        '[0-9]([0-9]|\.)+[0-9]'

    We differentiate date from other numbers by date has to have some kind of
    delimiter ('.', '-', '/') between day, month and year. We diregard numbers
    that do not contain dot. We are also matching dates without year,
    e.g. dd.mm. or dd.mm or d.mm, ...

       @str: String to search for a given pattern.
      @pstr: String containg regular expression pattern.
    @cutoff: Integer representing threshold cutoff string length. All strings
             that do not satisfy condition len(s) > cutoff are disregarded.
             Default value is 1.

    Returns: list object containig all matched dates.
    """
    dates = list()
    dpt = re.compile(pstr)

    for match in dpt.finditer(string):
        matchstr = match.group(0)
        if -1 != matchstr.find('.'):
            dates.append(matchstr)

    return dates


def find_phones(string: str,
                pstr: str = '[0-9]([0-9]|-|/|\s)+[0-9]',
                cutoff: int = 5):
    """Find phone numbers in a given string.

    Default pattern for matching phone numbers is:
        '[0-9]([0-9]|-|/|\s)+[0-9]'

    We assume that match containg phone number hes to be longer than 5
    characters, including delimiters -,/,:space:.

       @str: String to search for a given pattern.
      @pstr: String containg regular expression pattern.
    @cutoff: Integer representing threshold cutoff string length. All strings
             that do not satisfy condition len(s) > cutoff are disregarded.
             Default value is 5.

    Returns: list object containig all matched phones.
    """

    phones = list()
    dpt = re.compile(pstr)

    for match in dpt.finditer(string):
        matchstr = match.group(0)

        # if -1 != matchstr.find('/') or -1 != matchstr.find('-'):

        # Phone number can contain spaces, and that breaks things a bit.
        # Lets select just strings containing numbers with more than five
        # carachetrs.
        if cutoff < len(matchstr):
            phones.append(matchstr)

    return phones


def find_numbers(string: str, pstr: str = '[0-9]+', cutoff: int = 1):
    """Find integer numbers in a given string.

    Default pattern for matching numbers is:
        '[0-9]+'

       @str: String to search for a given pattern.
      @pstr: String containg regular expression pattern.
    @cutoff: Integer representing threshold cutoff string length. All strings
             that do not satisfy condition len(s) > cutoff are disregarded.
             Default value is 1.

    Returns: list object containig all matched numbers.
    """

    numbers = list()
    dpt = re.compile(pstr)
    for match in dpt.finditer(string):
        matchstr = match.group(0)

        if cutoff < len(matchstr):
            numbers.append(matchstr)

    return numbers


def clean_text(string: str, presdts: bool = False, cospcs: bool = True):
    """Removes all characters which are not alpha-numeric except space(s). It
    also changes them to lower letter and removes leading or trailing spaces.

        @str: String to clean.
    @presdts: Boolean flag indicating should dates in a text be preserved or
              not. If dates are not to be preserved, then date format
              delimiters are deleted too. Default value is 'False'.
     @cospcs: Boolean flag indicating should multiple sequential space
              characters should be replaced with single space character.
              Default value is 'True'.

    Returns: string containing cleansed text.
    """

    pattern = '[^a-zA-Z0-9\s]+'
    if presdts:
        pattern = '[^a-zA-Z0-9\.\s]+'

    result = re.sub(pattern, '', string).lower().strip()

    # Convert multiple spaces to single space
    if cospcs:
        result = re.sub('\s\s+', '', result)

    return result


def extractdata(al):
    """ extractdata() documentation.
    """

    # patients = []

    for line in al:
        rest = line.rstrip('\n')
        tokens = rest.split(' ')

        patient = Patient(None, None, None, None, None, None, None, None)

        patient.pending = is_pending(tokens[0])
        # Remove pending from line
        rest = rest.replace(tokens[0], '')

        patient.month = tokens[1].lower()
        # Remove month from line
        rest = rest.replace(tokens[1], '')

        # Check for lastnames
        patient.lastname = []
        for name in lastnames:
            if -1 != rest.find(name.capitalize()):
                patient.lastname.append(name.capitalize())
                rest = rest.replace(name.capitalize(), '')
                # Since we can have multiple lastnames per line cycle through
                # all lastanems

        # Check for firstname
        patient.firstname = []
        for name in firstnames:
            if -1 != rest.find(name.capitalize()):
                patient.firstname.append(name.capitalize())
                rest = rest.replace(name.capitalize(), '')
                # Since we can have multiple firstnames per line cycle through
                # all lastanems

        # Check for diognose
        patient.diagnosis = []
        for diagnosis in diagnoses:
            if -1 != rest.find(diagnosis.capitalize()):
                patient.diagnosis.append(diagnosis)
                rest = rest.replace(diagnosis.capitalize(), '')
                # Since we can have multiple diagnosis per line cycle through
                # all lastanems

        patient.rest = rest
        patient.source = line.rstrip('\n')

        patient.display()

        # patients.append(patient)

    # return patients
