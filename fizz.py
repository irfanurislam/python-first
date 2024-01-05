# def fizz_buzz(input):
#     if input % 3 == 0:
#         result = 'FIzz'

#     else:
#         result = 'Buzz'
#     return result


# print(fizz_buzz(2))


# cleaner code

def fizz_buzz(input):
    if(input % 3 == 0 ) and (input % 5 == 0):
        return "fizBuzz"
    if input % 3 == 0:
        return 'FIzz'
    if input % 5 == 0:
        return 'Buzz'
   

    return input
   

print(fizz_buzz(5))