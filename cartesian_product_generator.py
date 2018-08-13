def cartesian_product_generator(*args):
    sets = []
    counters = []
    finished = False

    def cascade_counters_incrementation(n):
        nonlocal finished
        if n >= len(counters):
            finished = True
            return 0
        counters[n] += 1
        if counters[n] > len(sets[n]):
            counters[n] = 1
            return cascade_counters_incrementation(n + 1)

    for i in args:
        sets.append(i)
        counters.append(1)
    if args:
        counters[0] = 0

    while True:
        cascade_counters_incrementation(0)
        if finished:
            break
        else:
            yield tuple([sets[i][counters[i] - 1] for i in range(len(sets))])
