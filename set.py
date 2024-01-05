nummbers = [12,45,56,12,45,86];
print(nummbers)

numb = {12,45,56,45,89}
# unique sets
print(numb)

numbers_set = set(nummbers)
print(numbers_set)



numbers_set.add(77)
numbers_set.remove(77)
numbers_set.add(78)
print(numbers_set)

# tuples hocce immutable



# labmdaa

multi = lambda x,y: x*y
print(multi(2,2))

numbersss = [12,34,56]

def doublt(x):
    return x * 2
  

doubleNumbers = map(doublt,numbersss)
print(doubleNumbers)


# comprehensive
aray = [12,34,56,78,5]

oddnumers = [num for num in aray if num % 2 ==1]
print(oddnumers)