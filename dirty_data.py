data = "antEri0our\n\t>>"

# print(data)

notun_data = data.lower()
output_data = ""
print(notun_data)

for sonkha in notun_data:
    print(sonkha)
    if(sonkha == 'a') or (sonkha == 'e')  or (sonkha == 'i')  or (sonkha == 'o')  or (sonkha == 'u'):
        output_data += sonkha + " "
print(output_data)
    