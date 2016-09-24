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

#Dictionary to convert hex to binary
Hex_to_bin = {'0':'0000', '1':'0001', '2':'0010', '3':'0011', '4':'0100', '5':'0101',
'6':'0110', '7':'0111', '8':'1000', '9':'1001', 'A':'1010', 'B':'1011',
'C':'1100', 'D':'1101', 'E':'1110', 'F':'1111' }


#Dictionary used for scoring plaintext

fre_lett =  {'1':'E','2':'T','3':'A','4':'O','5':'I','6':'N','7':'S',
'8':'R','9':'H','10':'D','11':'L','12':'U','13':'C','14':'M','15':'F','16':'Y','17':'W',
'18':'G','19':'P','20':'B','21':'V','22':'K','23':'X','24':'Q','25':'J','26':'Z',}

#Using Hex_to_bin dictionary, convert the hex string to binary
def Conv_Hex_To_Bin(e):
    bin_string = ''
    for i in range(len(e)):
        for j in Hex_to_bin.keys() :
            if e[i] ==  j:
                bin_string = bin_string + Hex_to_bin[j]
    return bin_string

ciphertext = raw_input("Please enter the hex encoded ciphertext:").upper()

bin_ciphertext = ''
bin_ciphertext = bin_ciphertext + Conv_Hex_To_Bin(ciphertext)


print "Ciphertext in binary is\n\n" + str(bin_ciphertext) + "\t\t"
print "Length is \n\n" + str(len(str(bin_ciphertext)))

#Using each ascii character as a key, XOR the key
#with ciphertext and store results in a dictionary

#Dictionary of binary-to-ascii mapping for ASCII characters in the extended ASCII set
key_dict = {}
#33-126
for i in range (32,127,1):
    #key_dict.update({ chr(i) : bin(int(binascii.hexlify(chr(i)), 16))})
    key_dict.update({ (str(bin(int(binascii.hexlify(chr(i)), 16))).replace("0b","",1)).zfill(8) : chr(i) })


print "\n\n\n The dictionary is : \n\n\n\n%r" %key_dict

#Define a scoring dictionary updated after getting plaintext in each iteration of the loop below

Score_dict = {}

for k in key_dict:
    key = ''
    for i in range(len(bin_ciphertext)/8):
        key = key + k

print "\n\n\n\nkey is " + key + "\n\n\n\n"
print "Length of the key is " + str(len(key))
