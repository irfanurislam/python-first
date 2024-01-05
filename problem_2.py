data = 'firebaby'

shift=1
output = ''

for character in data:
    output += chr((ord(character)+ shift-97)% 26 + 97)
print(output)
# aski code print kortece