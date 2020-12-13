import codecs
# infile = codecs.open("my.txt", "r", "utf-8")
# for line in infile:
#     print(line)
# infile.close()

infile = codecs.open("my.txt", "a", "utf-8")
for line in infile:
    line = line.rstrip()
    print(line)
infile.close()

infile = codecs.open("my.txt", "a", "utf-8")
for line in infile:
    line = line.strip()
    print(line)
infile.close()