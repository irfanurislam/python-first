# def increment(number,by):
#     return number + by

# print(increment(2,3)) 


def mul(*list):
    total = 1
    for number in list:
        total = total * number
    return total

print(mul(2,3,4,5))


def save_user(**user):
    print(user["name"])

save_user(new12=2,name="admin")                                                                                 