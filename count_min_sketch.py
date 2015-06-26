import mmh3


TODO = """
fix list indices if mmh3 has to take strings
"""


class CountMinSketch(object):
    """
    linear write and read time with fixed memory size
    with a tunable accuracy 
    d rows for d has functions
    w columns for size of d row
    greater w reduces hash collisions and increases accuracy
    at the cost of memory
    """
    def __init__(self, size, hashes):
        self.size = size
        self.hashes = hashes
        self.sketch = []
        
        for i in range(hashes):
            _hash_table = [0 for x in range(size)]
            self.sketch.append(_hash_table)

    def insert(self, item):
        """
        right now this just works with ints
        have something here to check types so that
        integers get the fast linear congruential generator
        and everything else gets murmur3
        https://en.wikipedia.org/wiki/Linear_congruential_generator
        """
        for i in range(self.hashes):
            _hash = mmh3.hash(item, i) % self.size
            self.sketch[i][_hash] += 1
            
    def count(self, item):
        counts = []
        for k, v in zip(self.sketch, range(self.hashes)):
            for j in k:
                search_key = mmh3.hash(item, v) % self.size
                counts.append(k[search_key])
        return min(counts)


def fast_linear_congruential_generator(a=11, b=37, c=1):
    """
    a, b, and c values were looked up from a table at
    http://www.cs.princeton.edu/courses/archive/spring03/cs126/assignments/cycle.html
    """
    p = 65537
    return a * b + c % p
    

cms = CountMinSketch(size=100, hashes=2)

for i in (1,1,1,1,1,2,3,2,2,8,8,3,0,0,1,34,7657,12,68,9,1,28,735,87,3,4,4,5,6,7,81,4,3,5,6,4,2,1,1,1,3,6,2,7,9,6,3,2,4,6,8,9,9,9,7,3,2,45,7,3,65,3,5,9,4,1,23,5,12,1,1,1,1,34,2,7,1,2,8,2,67,9,34,12,56,79,4,2,2,7,235,86,685,):
    cms.insert(str(i))

print(cms.__dict__)

print(cms.count("1"))


        
    

