import sys

print(sys.argv)
num_arguments = len(sys.argv)
num_files = num_arguments-1
num_sequences = int(num_files/2)

startfiles = sys.argv[1:num_sequences+1]
stopfiles = sys.argv[num_sequences+1:]

print("Start files: \n * " + "\n *".join(startfiles))
print("Stop files: \n * " + "\n *".join(stopfiles))

outfile = open("summary.csv", "w")
outfile.write('#Sequence number, number of start codons, number of stop codons \n' )

for numfile in range(0, num_sequences):
    startfilename = startfiles[numfile]
    stopfilename = stopfiles[numfile]
    with open(startfilename, "r") as startfile:
        numstarts = startfile.read().strip()
    with open(stopfilename, "r") as stopfile:
        numstops = stopfile.read().strip()
    sequencename = startfilename.split("_")[1].split(".")[0]
    sequencename2 = stopfilename.split("_")[1].split(".")[0]
    #if not sequencename == sequencename2:
        #print("Error: Sequences names should look the same, file ordering wrong!")
    outfile.write(sequencename + ", " + numstarts + ", " + numstops + "\n")

outfile.close()
