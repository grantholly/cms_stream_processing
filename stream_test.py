import count_min_sketch
import json

TODO = """
1. import a log file and iterate sending the lines to a cms instance
2. stream messages from nc to a cms instance
  - this will require the creation of a network interface
3. stream messages from activeMQ into cms
  - like before, this will require the creation of an interface
"""

cms = count_min_sketch.CountMinSketch(100, 4)

def file_stream_test(file):
    with open(file) as f:
        for line in f:
            j = json.loads(line)
            print(type(j))
            """
            l = line.split(":")
            for i in l:
                cms.insert(i)
            """
    print(cms.__dict__)
    return cms.count("body")

file_stream_test("/Users/grant.holly/for-fun/python/test_messages.txt")
