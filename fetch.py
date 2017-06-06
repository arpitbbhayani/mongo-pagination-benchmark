from dbutil import db


def skiplimit(page_size, page_num):
    """returns a set of documents belonging to page number `page_num`
    where size of each page is `page_size`.
    """
    # Calculate number of documents to skip
    skips = page_size * (page_num - 1)

    # Skip and limit
    cursor = db['students'].find().skip(skips).limit(page_size)

    # Return documents
    return [x for x in cursor]


def idlimit(page_size, last_id):
    """Function returns `page_size` number of documents after last_id
    and the new last_id.
    """
    if last_id is None:
        # When it is first page
        cursor = db['students'].find().limit(page_size)
    else:
        cursor = db['students'].find({'_id': {'$gt': last_id}}).limit(page_size)

    # Get the data
    data = [x for x in cursor]

    if not data:
        # No documents left
        return None, None

    # Since documents are naturally ordered with _id, last document will
    # have max id.
    last_id = data[-1]['_id']

    # Return data and last_id
    return data, last_id
