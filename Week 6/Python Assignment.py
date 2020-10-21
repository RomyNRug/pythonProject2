#Revisiting exercise 2.4.2

distance = input("How far is your destination in kilometers? Please enter a number here:")
transportation= input("What was your mode of transportation? Choose between car, bike or walk: ")
distance_time= float(distance)
total_time= 0

for _ in distance:
    if transportation == "car":
        avg_car_km_h= 50
        total_time= distance_time/avg_car_km_h
        gas_stop= input("Did you have to stop for gas during your trip?")
        if gas_stop == "yes":
            total_time += (10/60)

    elif transportation == "bike":
        avg_bike_km_h= 11
        total_time= distance_time/avg_bike_km_h
        bike_shed= input("Did you have to take the bike out of the shed?")
        if bike_shed == "yes":
            total_time += (5/60)

    elif transportation == "walk":
        avg_walk_km_h= 5
        total_time= (distance_time/avg_walk_km_h)
        externality_walk = input("Did you experience any delay due to fatigue and therefore took breaks? Type yes or no: ")
        if externality_walk == "yes":
            amount_breaks= input("How many breaks did you take? Please enter the number here:")
            if amount_breaks == "yes":
                breaks_ = float(amount_breaks)
                total_time += (breaks_*(15/60))

# if a new mode of transportation is added such as train. a new if transportation =="train"
# should be added with its corresponding average km/h and externalities in the case of those.

    if transportation == "train":
        avg_train_km_h= 150
        total_time= (distance_time/avg_train_km_h)

print("The time you took to your destination is ",round(total_time,1), "hours ,defined in hours including externalities")







