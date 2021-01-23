def distance_from_zero(x):

    if type(x)==int or type(x) == float:
        return abs(x)

    elif x=="-5.6":
        return "What"

    else:
        return "Nope"

print(distance_from_zero(-5.6))
