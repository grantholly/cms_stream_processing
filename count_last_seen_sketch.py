import datetime
import time

import mmh3

from count_min_sketch import CountMinSketch


class CountLastSeenSketch(CountMinSketch):
    """
    sub class of CountMinSketch
    instead of recording the count of a given hash digest
    into the sketch, we are going to recrod the time stamp
    """
    def insert(self, item):
        for i in range(self.hashes):
            _hash = mmh3.hash(item, i) % self.size
            self.sketch[i][_hash] = datetime.datetime.utcnow()

    def last_seen(self, item):
        timestamps = []
        for k, v in zip(self.sketch, range(self.hashes)):
            for j in k:
                search_key = mmh3.hash(item, v) % self.size
                timestamps.append(k[search_key])
        return max(timestamps)

def tuple_test():
    clss = CountLastSeenSketch(size=100, hashes=2)

    for i in (1,1,1,1,1,2,3,2,2,8,8,3,0,0,1,34,7657,12,68,9,1,28,735,87,3,4,4,5,6,7,81,4,3,5,6,4,2,1,1,1,3,6,2,7,9,6,3,2,4,6,8,9,9,9,7,3,2,45,7,3,65,3,5,9,4,1,23,5,12,1,1,1,1,34,2,7,1,2,8,2,67,9,34,12,56,79,4,2,2,7,235,86,685,):
        clss.insert(str(i))
        time.sleep(1)

    print(clss.__dict__)

    print(clss.last_seen('1'))

tuple_test()
