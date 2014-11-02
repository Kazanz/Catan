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

    original = {'s': 4, 'f': 4, 'w': 4, 'o': 3, 'b': 3, 'd': 1}
    exp = {'s': 2, 'f': 2, 'w': 2, 'o': 2, 'b': 2, 'd': 1}


class NumberPool(_BasePool):
    """This object returns a list of available number tiles. The default fields
    are the total in each expansion. NOT cumulative."""

    original = {2: 1 , 3: 2, 4: 2, 5: 2, 6: 2, 8: 2, 9:2, 10: 2, 11: 2, 12: 1}
    exp = {2: 2 , 3: 3, 4: 3, 5: 3, 6: 3, 8: 3, 9: 3, 10: 3, 11: 3, 12: 2}


class CatanMap():
    """This is the main map object display. This class randomizes itself."""
    width = {'orig':5, 'exp':7}

    def __init__(self, *args, **kwargs):
        self.version = kwargs.pop('version')
        self.players = kwargs.pop('players')
        self.landpool = LandPool(version=self.version, players=self.players)
        self.numberspool = NumberPool(version=self.version, players=self.players)
        self.land = None
        self.numbers = None

    def randomize(self):
        land = self._get_random_pool(self.land, 'land')
        nums = self._get_random_pool(self.numbers, 'numbers')
        return land, nums, self.width.get(self.version)

    def _get_random_pool(self, pool, name):
        if not pool: pool = getattr(self, name + 'pool').generate()
        shuffle(pool)
        setattr(self, name, pool)
        return [pool.pop() for unused_i in range(0, len(pool))]
