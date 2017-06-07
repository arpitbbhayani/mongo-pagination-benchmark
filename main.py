import time
import stats
import fetch
import dbinit
import populate


def setup(count):
    """Empties the collection and populates with `count` number of documents.
    """
    dbinit.init_collection()
    populate.populate(count)


def benchmark_skiplimit(count, page_size):
    """Fetches all documents from the collection page-wise
    """
    setup(count)
    run_count = 3

    times = []

    page_number, items_fetched = 1, 0

    while True:
        start_time = time.time()
        for i in range(run_count):
            data = fetch.skiplimit(page_size, page_number)
        end_time = time.time()

        if not data:
            break

        items_fetched += len(data)
        page_number += 1

        # Appending time to fetch the page
        times.append((end_time - start_time)/run_count)

    # asserting all items fetched from the collection
    assert items_fetched == count

    # returning the time to fetch each page
    return times


def benchmark_idlimit(count, page_size):
    setup(count)
    run_count = 3

    times = []

    page_number, items_fetched = 1, 0
    last_id = None

    while True:

        start_time = time.time()
        for i in range(run_count):
            data, new_last_id = fetch.idlimit(page_size, last_id)
        end_time = time.time()

        # Update the last_id
        last_id = new_last_id

        if not data:
            break

        items_fetched += len(data)
        page_number += 1

        # Appending time to fetch the page
        times.append((end_time - start_time)/run_count)

    # asserting all items fetched from the collection
    assert items_fetched == count

    # returning the time to fetch each page
    return times


def print_stats(times, count, page_size, approach):
    s = stats.all(times)
    print("\"{}\",{},{},{},{},{},{}".format(approach, count, page_size, s['mean'], s['p99'], s['p95'], s['p50']))


def bench(count, page_size):
    approach = 'skiplimit'
    times = benchmark_skiplimit(count, page_size)
    print_stats(times, count, page_size, approach)

    approach = 'idlimit'
    times = benchmark_idlimit(count, page_size)
    print_stats(times, count, page_size, approach)


if __name__ == '__main__':
    print("\"{}\",\"{}\",\"{}\",\"{}\",\"{}\",\"{}\",\"{}\"".format("Approach", "Count", "Page Size", "Mean (in microseconds)", "p99 (in microseconds)", "p95 (in microseconds)", "p50 (in microseconds)"))

    for count in range(5, 701, 5):
        for page_size in range(10, 101, 10):
            bench(count, page_size)

    for count in range(750, 2001, 50):
        for page_size in range(10, 101, 10):
            bench(count, page_size)

    for count in range(2100, 5001, 100):
        for page_size in range(10, 101, 10):
            bench(count, page_size)

    for count in range(5500, 10001, 500):
        for page_size in range(10, 101, 10):
            bench(count, page_size)
