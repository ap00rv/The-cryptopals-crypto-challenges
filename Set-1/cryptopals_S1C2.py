#!/usr/bin/python3.5

#Matasano Cryptopals Challenge 2 - Set 1


print("Matasano Cryptopals Challenge 2 from Set 1\n\n\n")

print("Challenge URL:  https://cryptopals.com/sets/1/challenges/2\n\n\n")

print("This program produces XOR of two equal lenght buffers\n\n\n")


#Dictionary to convert hex to binary
Hex_to_bin = {'0':'0000', '1':'0001', '2':'0010', '3':'0011', '4':'0100', '5':'0101',
'6':'0110', '7':'0111', '8':'1000', '9':'1001', 'A':'1010', 'B':'1011',
'C':'1100', 'D':'1101', 'E':'1110', 'F':'1111' }


#Binary string variables

bin_string1 = ''
bin_string2 = ''


# Get hex string from user and convert all alphabets to uppercase

hex_string1 = input("\n\n\nPlease enter the first hex string: ")
hex_string2 = input("\n\n\nPlease enter the second hex string :")

#convert to uppercase
hex_string1 = hex_string1.upper()
hex_string2 = hex_string2.upper()

if len(hex_string1) != len(hex_string2):
    print("Lenghts of strins are not equal !")


#Using Hex_to_bin dictionary, convert the hex string to binary
def Conv_Hex_To_Bin(e):
    bin_string = ''
    for i in range(len(e)):
        for j in Hex_to_bin.keys() :
            if e[i] ==  j:
                bin_string = bin_string + Hex_to_bin[j]
    return bin_string


bin_string2 = Conv_Hex_To_Bin(hex_string2)
bin_string1 = Conv_Hex_To_Bin(hex_string1)


print ("\n\n\nBinary value of ", hex_string1, "is\n\n\n", bin_string1)
print ("\n\n\nBinary value of ", hex_string2, "is\n\n\n", bin_string2)
#debug - print ("length of hex string" , len(hex_string))

#XOR function
result = ''

for i in range(len(bin_string1)):
    for j in [bin_string1[i]] :
        for k in [bin_string2[i]] :
            if j == k:
                result = result + '0'
            else:
                result = result + '1'

print ("\n\n\nresult of XOR is:\n\n", result)
fin_result = hex(int(result,2))
print("\n\n\nresult in hex format is", fin_result)

#debug
#if fin_result == '0x746865206b696420646f6e277420706c6179':
#print("success")
