def hotel_cost(days):
    return 140 * days


def plane_ride(city):
    if city == "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475


def rental_car_cost(days):
    if days < 3:
        return 40 * days

    elif days >= 3 & days < 7:
        return days * 40 - 30

    elif days >= 7:
        return 40 * days - 50


def trip_cost(city, days, spending_money):
    return hotel_cost(days) + plane_ride(city) + rental_car_cost(days) + spending_money


print(trip_cost("Tampa", 5, 500))
