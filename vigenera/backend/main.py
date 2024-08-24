from vigenera.backend.VigeneraBackend import VigeneraBackend

my_vigenera = VigeneraBackend()
# change the text to what you want to encrypt or decrypt
text = 'ECKM JC JW CPHBLC'
#text = "HELP  ME MY  FRIEND"

# change your key to anything of any length
key = "XYZ"

# setting the values, leave the lines like this
my_vigenera.text = text
my_vigenera.key = key


# change the action to 0(Zero) if you want to decrypt
action = 1

# executing your action
my_vigenera.encrypt() if action else my_vigenera.decrypt()

# you can now run the script
