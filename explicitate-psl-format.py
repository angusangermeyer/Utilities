#!/usr/bin/env python2.7

# This program explicitates the usual calculations performed on PSL formatted files, generating an "ePSL" (explicit PSL) file. 
# File format fields are:
# 1. (Q) query
# 2. (QLen) query length
# 3. (T) target
# 4. (TLen) target length
# 5. (M) number of matches
# 6. (MM) number of mismatches 
# 7. (QGL) query gap length (as in PSL format)
# 8. (TGL) target gap length (as in PSL format)
# 9. (SeqID) sequence identity (of the aligned portion)
# 10. (QSeqID) sequence identity (of the query)
# 11. (TSeqID) sequence identity (of the target)
# 12. (ALen) alignment length
# 13. (QFrac) query aligned fraction
# 14. (TFrac) target aligned fraction
# 15. (BSize) block size (as in PSL format)
# 16. (QStart) block start positions on query (as in PSL format)
# 17. (TStart) block start positions on target (as in PSL format)

import sys
import argparse as ap

p = ap.ArgumentParser()
p.add_argument("--header", action="store_true", help="The input file has the header")
p.add_argument("-i", "--input-file", help="Input PSL file (default: stdin)")
p.add_argument("-o", "--output-file", help="Output ePSL file (default: stdout)")
args = p.parse_args()

try:
	INPUT = open(args.input_file, "r")
except:
	INPUT = sys.stdin

try: 
	OUTPUT = open(args.output_file, "w")
except:
	OUTPUT = sys.stdout

Lines = [line.rstrip("\n\r\n") for line in INPUT]

if args.input_file:
	INPUT.close()

if args.header:
	Lines = Lines[5:]

OUTPUT.write("\t".join(["Q", "QLen", "T", "TLen", "M", "MM", "QGL", "TGL", "SeqID", "QSeqID", "TSeqID", "ALen", "QFrac", "TFrac", "BSize", "QStart", "TStart"]) + "\n")

for line in Lines:
	lst = line.split("\t")
	ALen = str(int(lst[0]) + int(lst[1]))
	SeqID = str(round((float(lst[0]) / float(ALen))*100, 1))
	QSeqID = str(round((float(lst[0]) / float(lst[10]))*100, 1))
	TSeqID = str(round((float(lst[0]) / float(lst[14]))*100, 1))
	QFrac = str(round((float(ALen) / float(lst[10]))*100, 1))
	TFrac = str(round((float(ALen) / float(lst[14]))*100, 1))
	newlst = [lst[9], lst[10], lst[13], lst[14], lst[0], lst[1], lst[5], lst[7], SeqID, QSeqID, TSeqID, ALen, QFrac, TFrac, lst[18], lst[19], lst[20]]
	OUTPUT.write("\t".join(newlst) + "\n")

if args.output_file:
	OUTPUT.close()
