import sys

#print(sys.argv)
#for filename in sys.argv[1:]:
    #print("Got filename: " + filename)

print("# Sequence number, Number of repeats")
for filename in sys.argv[1:]:
    seqnum = filename.split("_")[1]
    with open(filename, "r") as f:
        repnum = f.read()
    print(seqnum + "," + repnum.strip())
