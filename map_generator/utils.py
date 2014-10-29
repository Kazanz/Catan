from random import shuffle


class _BasePool(object):
    def __init__(self, *args, **kwargs):
        self.version = kwargs.pop('version')
        self.players = kwargs.pop('players')

    def generate(self):
        if self.version == "original":
            if self.players < 5:
                dictionary = self.original
            else:
                dictionary = {key: self.original[key] + self.exp[key]
                              for key in self.original.keys()}
        return self._dictionary_to_list(dictionary)

    def _dictionary_to_list(self, dictionary):
        full_list = []
        for item, count in dictionary.iteritems():
            for unused_i in range(0, count):
                full_list.append(item)
        return full_list


class LandPool(_BasePool):
    """This object returns a list of available land tiles. The default fields
    are the total in each expansion. NOT cumulative."""

    original = {'g': 4, 'l': 4, 'w': 4, 'o': 3, 'b': 3, 'd': 1}
    exp = {'g': 2, 'l': 2, 'w': 2, 'o': 2, 'b': 2, 'd': 1}


class NumberPool(_BasePool):
    """This object returns a list of available number tiles. The default fields
    are the total in each expansion. NOT cumulative."""

    original = {2: 1 , 3: 2, 4: 2, 5: 2, 6: 2, 8: 2, 9:2, 10: 2, 11: 2, 12: 1}
    exp = {2: 1 , 3: 2, 4: 2, 5: 2, 6: 2, 8: 2, 9:2, 10: 2, 11: 2, 12: 1}


class CatanMap(LandPool, NumberPool):
    """This is the main map object display. This class randomizes itself."""
    def __init__(self, *args, **kwargs):
        self.board_size = kwargs.pop('board_size')
        super(CatanMap, self).__init__(*args, **kwargs)
        self.landpool = self.generate()

    def randomize(self, hard=False):
        if hard or not self.landpool: self.landpool = self.generate()
        shuffle(self.landpool)
        return [self.landpool.pop() for unused_i in range(0, self.board_size)]
