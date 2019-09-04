# Easy Crackme 1: Crack the algorithm by skudo

 Description: Crack the algorithm and use it to complete this challenge
Filename: encrypt

The first thing that we do is we create a "key" from the string "iamsupersecur3"

This function starts off by creating an integer with the sum of the hex value of the string above: 0x55A

Next this value is passed into the following calculation: 

v12 = 0x122B * (v11 ^ (v11 + 0x99AF) ^ 0x834C);

Which we expect to result in 0x1C86635

BP: 0x2368, we expect RAX to be: 0x1C86635 -- is this correct? -- yup this looks good


From here we just xor the previous byte of the string with the last byte of the xor operation with the initial one being 0xB

## Solving normally

I wrote a python script to dump out the information we need

## Solving with ANGR

It looks like ANGR doesn't support the C++ runtime super well, so I'm going to punt on this one for now and in the future stick to C


# Easy Crackme #2 Crack The Door
https://crackmes.one/crackme/5b5b386033c5d46b771434b8

# Easy Crackme #3 my_first_crack
https://crackmes.one/crackme/5ab77f6433c5d40ad448cae0
