def computepay(hours,rate):

    if hours<=40:
        return hours * rate
    elif hours>40:
        overtime = hours - 40
        return overtime * 1.5 * rate + 40 * rate


print("\n\nPay:")
print(computepay(55,10))



