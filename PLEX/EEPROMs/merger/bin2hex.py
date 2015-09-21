import os, sys

def toHex(fn):
  fnOut = os.path.splitext(fn)[0] + ".hex"
  ab = bytearray(open(fn, "rb").read())
  with open(fnOut, "w") as f:
    for o in xrange(0, len(ab), 16):
      f.write("%08X:  %s  %s\n" % (o, " ".join("%02X" % b for b in ab[o:o+8]), " ".join("%02X" % b for b in ab[o+8:o+16])))

def main(argv):
  for fn in argv[1:]: toHex(fn)

if __name__=="__main__": main(sys.argv)