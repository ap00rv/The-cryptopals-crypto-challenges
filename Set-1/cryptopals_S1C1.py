#!/usr/bin/python3.5

#Matasano Cryptopals Challenge 1 - Set 1
#reference : https://blogs.oracle.com/rammenon/entry/base64_explained
print("Matasano Cryptopals Challenge 1 from Set 1\n\n\n")

print("Challenge URL:  https://cryptopals.com/sets/1/challenges/1\n\n\n")

print("This program converts any given hex string to base64 format.\n\n\n")


#Dictionary to convert hex to binary
Hex_to_bin = {'0':'0000', '1':'0001', '2':'0010', '3':'0011', '4':'0100', '5':'0101',
'6':'0110', '7':'0111', '8':'1000', '9':'1001', 'A':'1010', 'B':'1011',
'C':'1100', 'D':'1101', 'E':'1110', 'F':'1111' }


#Dictionary mapping decimal to Base64
base_64_dict =  { i : '' for i in range(0,64,1)}
for y in range(0,26,1):
    base_64_dict[y] = chr(y+65)
for y in range(26,52,1):
    base_64_dict[y] = chr(y+71)
for y in range(52,62,1):
    base_64_dict[y] = chr(y-4)

base_64_dict[62] = '+'
base_64_dict[63] = '/'


print  ("\n\n\nDictionary mapping decimal to Base64\n\n\n", base_64_dict)


#Binary string variable

bin_string = ''

# Get hex string from user and convert all alphabets to uppercase
hex_string = input("\n\n\nPlease enter the hex string you want to convert :")
print("\n\n\nYou entered: \n", hex_string)
hex_string = hex_string.upper()
print("\n\n\nConverting lowercase alphabets to uppercase:\n\n\n", hex_string)


#Using Hex_to_bin dictionary, convert the hex string to binary


for i in range(len(hex_string)) :
    for j in Hex_to_bin.keys() :
        if hex_string[i] ==  j:
            bin_string = bin_string + Hex_to_bin[j]

print ("\n\n\nBinary value of the hex string is: \n", bin_string)
#debug - print ("length of hex string" , len(hex_string))
print ("\n\n\nlength of binary string:\n",len(bin_string))


#Put the padding zeroes at the end of binary string

print ("\n\n\nPadding with extra 0s if necessary.......")

if len(bin_string) > 24 and len(bin_string) % 24 != 0 :
    for k in ( 24 - (len(bin_string) % 24)):
        bin_string = bin_string + '0'
elif len(bin_string) < 24:
    for k in range(24 - len(bin_string)):
        bin_string = bin_string + '0'
else:
    pass

if len(bin_string) %24 == 0:
    print ("\n\n\nPadding succesful ! ")


print ("\n\n\nPadded binary string:\n", bin_string)
print ("\n\n\nLength of padded string: \n", len(bin_string))



#Grouping the padded binary into groups of 6 bits and then mapping it to the base_64_dict
#inlcude code for padding with = symbol

print ("\n\n\nConverting to Base64.....\n\n", bin_string)
fin_base64_string = ''
r = 0
i=1
while i <= (len(bin_string)) / 6 :

    fin_base64_string = fin_base64_string + base_64_dict[int((bin_string[r:r + 6]),2)]
    r = r + 6
    i = i+1


#debug code
#if fin_base64_string == 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t' :

print ("\n\n\nConversion complete ! Please check the results below with the expected solution\n\n\n")


print ("The base64 encoded string is : ",fin_base64_string)
print ("\n\n\nLength of base64 encoded string: ",len(fin_base64_string))
