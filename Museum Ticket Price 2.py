# Days of the week
DaysOfTheWeek = ["monday", "tuesday", "wednesday", "thursday", "friday", " saturday", "sunday"]

# Asking for age, day, and coupons
age = input("What is your age? : ")
day_of_week = input("What day of the week you will visit on? : ")
coupon = input("Coupon Code: ")

# To allow the user to insert and combination of lower or capital letters this converts it all to lowercase in the code
lowercase_day = day_of_week.lower()

# Checks that both age and day are valid
if age.isalpha() or int(age) < 0:
    print("Age is invalid")
elif lowercase_day not in DaysOfTheWeek:
    print("Day is invalid")
else:
    # Cost for kids (5 and under)
    if int(age) <= 5:
        cost = 0
    # Cost for youth (6 to 17)
    elif 17 >= int(age) >= 6:
        if lowercase_day == "monday":
            cost = 5
        elif lowercase_day == "tuesday" or "wednesday" or "thursday":
            cost = 10
        elif lowercase_day == "friday" or " saturday" or "sunday":
            cost = 15
    # Cost for adults (18 to 64)
    elif 64 >= int(age) >= 18:
        if lowercase_day == "monday" or "tuesday" or "wednesday" or "thursday":
            cost = 15
        elif lowercase_day == "friday" or " saturday" or "sunday":
            cost = 25
    # Cost for seniors (65+)
    elif int(age) >= 65:
        if lowercase_day == "monday" or "tuesday" or "wednesday" or "thursday":
            cost = 10
        elif lowercase_day == "friday" or " saturday" or "sunday":
            cost = 15
    # Applying coupons
    if coupon == "HALFOFF":
        cost /= 2
    elif coupon == "MINUS5":
        cost -= 5
    else:
        cost -= 0
    # Printing the final cost
    if cost <= 0:
        print(" ")
        print("Price: $0.00 (FREE)")
    else:
        print(" ")
        print("Price: $" + str(cost))









