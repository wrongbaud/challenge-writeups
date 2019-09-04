import struct

instr = "imsupersecur3"
testStr = "SvenJoergenIkeaBirdWaterSheepBoatCowPeePeePooPoo"
strSum = 0

# First get the sum of all the characters in the string
for c in instr:
    strSum += ord(c)
print "{:X}".format(strSum)

# Next we calculate the "key" from this sum
# since we are treating it as a single byte, lets make sure we're only using the last 8 bits
v12 = 0x122B * (strSum ^ (strSum + 0x99AF) ^ 0x834C)
print "V12 {:X}".format(v12)
v12 &=0xFF

# Gerneate the final value for createKey
v8 = 0
for x in instr:
    print "{}".format(ord(x) ^ v12)
    v8 += ord(x) ^ v12
initialKey = v8 % 100
print "createKey Result: {:X}".format(initialKey)

# the last loop which calls encryptByte on the testStr, xors it with the previous 
# character in the string, for the first iteration is uses the result of createKey
f = open("key.test",'wb')
for x in testStr:
    val = ord(x) ^ initialKey
    initialKey = initialKey ^ ord(x)
    f.write(struct.pack('B',val))
f.close()
