import statistics


def mean(times):
    return statistics.mean(times)


def all(times):
    return {
        'mean': mean(times) * 1000000
    }
