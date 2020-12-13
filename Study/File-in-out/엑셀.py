import codecs
infile = codecs.open("ex.csv", "r", "utf-8")

for line in infile.readlines():
    line = line.strip()
    print(line)
    wlist = line.split(",")
    for word in wlist:
        print(" ", word)
