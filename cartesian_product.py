class CartesianProduct:

    def __init__(self, *args):
        self.sets = []
        self.counters = []
        for i in args:
            self.sets.append(i)
            self.counters.append(1)
        if args:
            self.counters[0] = 0

    def cascade_counters_incrementation(self, n):
        if n >= len(self.counters):
            raise StopIteration
        self.counters[n] += 1
        if self.counters[n] > len(self.sets[n]):
            self.counters[n] = 1
            return self.cascade_counters_incrementation(n+1)

    def __iter__(self):
        return self

    def __next__(self):
        self.cascade_counters_incrementation(0)
        return tuple([self.sets[i][self.counters[i]-1] for i in range(len(self.sets))])
