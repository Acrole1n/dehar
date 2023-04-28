import os, sys, subprocess

banned = [] #[".php", ".asp"]

infile = sys.argv[1]
outdir = sys.argv[2]

input = open(infile, "r", encoding="utf-8").read().splitlines()

lis2 = []
for x in input:
	if ('"url"' in x) and not(any(i in x for i in banned)):
		lis2.append(x.split('"')[3].split("?")[0])

lis2 = list(dict.fromkeys(lis2))

open("./wgettemp.txt", "w", encoding="utf-8").write("\n".join(lis2))
subprocess.call("wget -x -i ./wgettemp.txt -P %s" % outdir, shell=True)
os.remove("./wgettemp.txt")
