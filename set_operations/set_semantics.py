from coin_flip.core import np


class SetSemantics:

    """
    Basic class to test out set operations such as: union, intersect, complement
    TODO: Expand to infer probability from sets

    Input
    -----
    - given_set: The representation of a sample space
    """

    def __init__(self, given_set: set):
        self._set = given_set
        self._set_list = list(given_set)

    def get_random_subset(self, subset_size):
        random_idx = np.random.randint(0, len(self._set), subset_size)
        random_subset = [] * subset_size
        for space_index in random_idx:
            random_subset.append(self._set_list[space_index])

        return set(random_subset)

    @staticmethod
    def set_intersection(set_1: set, set_2: set):
        msg = "First set: {0} and second set: {1}, intersect in: {2}".format(set_1, set_2, set_1 & set_2)
        print(msg)

    @staticmethod
    def set_union(set_1: set, set_2: set):
        msg = "First set: {0} and second set: {1}, have in union: {2}".format(set_1, set_2, set_1 | set_2)
        print(msg)

    def set_complement(self, set_1: set):
        set_diff = self._set.difference(set_1)
        msg = "The set difference between the sample space: {0} and the given set: {1} is {2}".format(self._set,
                                                                                                      set_1,
                                                                                                      set_diff)
        print(msg)


if __name__ == "__main__":
    sample_space = {'HH', 'HT', 'TH', 'TT'}
    set_semantics = SetSemantics(sample_space)
    rand_subset_1 = set_semantics.get_random_subset(3)
    rand_subset_2 = set_semantics.get_random_subset(2)
    set_semantics.set_intersection(rand_subset_1, rand_subset_2)
