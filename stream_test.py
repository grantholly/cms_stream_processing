from count_min_sketch import CountMinSketch
import json


def gimme_lines(input_file):
    with open(input_file, "r") as source:
        for line in source:
            yield line

def traverse(val, cms):
    for k, v in val.items():
        if isinstance(v, dict):
            # traverse!
            traverse(v, cms)
        elif isinstance(v, list):
            # do some inserts!
            list(map((lambda x: cms.insert(str(x))), v))
        else:
            cms.insert(str(v))

def tuple_test():
    cms = CountMinSketch(size=100, hashes=2)

    t = (1,1,1,1,1,2,3,2,2,8,8,3,0,0,1,34,7657,12,68,9,1,28,735,87,3,4,4,5,6,7,81,4,3,5,6,4,2,1,1,1,3,6,2,7,9,6,3,2,4,6,8,9,9,9,7,3,2,45,7,3,65,3,5,9,4,1,23,5,12,1,1,1,1,34,2,7,1,2,8,2,67,9,34,12,56,79,4,2,2,7,235,86,685,)

    number_of_ones = len([x for x in t if x == 1])

    for i in t:
        cms.insert(str(i))

    print(cms.__dict__)
    print("number of 1's %i" % number_of_ones)
    print("number of 1's in sketch: %i" % cms.count("1"))

def file_test(sketch_size, hash_functions, input_file, term):
    cms = CountMinSketch(size=sketch_size, hashes=hash_functions)
    tlms = gimme_lines(input_file)

    for tlm in tlms:
        tlm = json.loads(tlm)
        traverse(tlm, cms)

    #print(cms.__dict__)
    print("term '%s' occured %i times" % (term, cms.count(term)))

def main():
#    tuple_test()

#    "/home/gholly/ten_messages.txt"
#    "/home/gholly/thousand_messages.txt
#    "/home/gholly/hundred_thousand_messages.txt`
#    "/home/gholly/message.2017-11-20-23-utc"
    file_test(sketch_size=200000, hash_functions=10,
              input_file="/home/gholly/hundred_thousand_messages.txt",
              term="COMCAST CABLE")

main()
        
            
