import statistics


def mean(times):
    return statistics.mean(times)


def pN(p, times):
    if len(times) == 0:
        raise Error("List should not empty")
    if len(times) == 1:
        return times[0]
    return sorted(times)[ int((p/100) * len(times)) - 1 ]


def p95(times):
    return pN(95, times)


def p99(times):
    return pN(99, times)


def p50(times):
    return pN(50, times)


def all(times):
    return {
        'mean': mean(times) * 1000000,
        'p99': p99(times) * 1000000,
        'p95': p95(times) * 1000000,
        'p50': p50(times) * 1000000,
    }
