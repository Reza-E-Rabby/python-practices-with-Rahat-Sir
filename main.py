user_weight = input("What is your Weight(lbs): ")
if float(user_weight)<100:
    print("User Weight Cannot be less than 100")
    user_weight = input("What is your Weight(lbs): ")

else:
    weight_in_kg= float(user_weight) * 0.5
    if weight_in_kg>100:
        print("U are Heavier than 100 KG, Your Weight:-" + str(weight_in_kg) + "KG")

    else:
        print("U are Lighter than 100 KG, Your Weight:-" + str(weight_in_kg) + "KG")

print(type(weight_in_kg))