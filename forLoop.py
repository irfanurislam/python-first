for x in 'python':
    print(x)

for y in range(0,10,3):
    print(y)

print(type(range(5)))
print([1,2,3,4,5])



names = ["Jhones", "marry"];
found = False
for name in names:
    if name.startswith('J'):
        print("found")
        found = True
        break
    if not found:
        print ("not found")


        # while loop

    guess = 0
    answer = 5
    while answer != guess:
        guess = int(input('Guess:'))
    else:
        pass