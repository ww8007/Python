import codecs

infile = codecs.open("hi.txt", "r", "utf-8")
outfile = codecs.open("output.txt", "w", "utf-8")

i=1
for line in infile:
    outfile.write(str(i)+"."+line)
    i = i+1
infile.close()
outfile.close()