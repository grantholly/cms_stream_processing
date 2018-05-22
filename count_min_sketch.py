import mmh3


class CountMinSketch(object):
    """
    linear write and read time with fixed memory size
    with a tunable accuracy 
    d rows for d hash functions
    w columns for size of d row
    greater w reduces hash collisions and increases accuracy
    at the cost of memory
    sizing the sketch means choosing a value epsilon
    where epsilon is the error in counting within a factor
    of epsilon with a probability of sigma
    size = e/epsilon hashes = ceil(ln(1/sigma)) 
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
        have something here to check types so that
        integers get the fast linear congruential generator
        and everything else gets murmur3?  premature optimization trap?
        https://en.wikipedia.org/wiki/Linear_congruential_generator
        """
        for i in range(self.hashes):
            _hash = mmh3.hash(item, i) % self.size
            self.sketch[i][_hash] += 1
            
    def count(self, item):
        counts = []

        for k, v in zip(self.sketch, range(self.hashes)):
            search_key = mmh3.hash(item, v) % self.size
            counts.append(k[search_key])
        return min(counts)
        

        
    

