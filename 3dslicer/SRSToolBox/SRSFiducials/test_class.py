class DicomAttributesInterface(dict):
    def __init__(self, case=None):
        if case:
            self['a'] = 1
            self['b'] = 2
            self['c'] = 3
        else:
            self['a'] = None
            self['b'] = None
            self['c'] = None
