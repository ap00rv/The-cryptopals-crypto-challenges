#!/usr/bin/python2.7

#Matasano Cryptopals Challenge 3 - Set 1
#author - Apoorv Munshi

#useful links that can be used to solve this challenges
#https://joernhees.de/blog/2010/09/21/how-to-convert-hex-strings-to-binary-ascii-strings-in-python-incl-8bit-space/
#https://www.math.cornell.edu/~mec/2003-2004/cryptography/subs/frequencies.html
#

import binascii

print "Matasano Cryptopals Challenge 3 from Set 1\n\n\n"
print "Challenge description:  https://cryptopals.com/sets/1/challenges/3\n\n\n"

fre_lett =  {'1':'E','2':'T','3':'A','4':'O','5':'I','6':'N','7':'S',
'8':'R','9':'H','10':'D','11':'L','12':'U','13':'C','14':'M','15':'F','16':'Y','17':'W',
'18':'G','19':'P','20':'B','21':'V','22':'K','23':'X','24':'Q','25':'J','26':'Z',}

ciphertext = raw_input("Please enter the hex encoded ciphertext:")

bin_ciphetext = bin(binascii.hexlify(ciphertext))
#bin_ciphetext = "".join(["{0:08b}".format(int(c,16)) for c in ciphertext])

print bin_ciphetext
