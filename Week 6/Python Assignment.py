#Revisiting exercise 2.4.2

distance = input("How far is your destination in kilometers?")
transportation= input("What was your mode of transportation?")
distance_time= float(distance)
total_km= 0
total_time= 0 # in minutes
avg_bike= 11 #11 kilometers/hour
total_break_time= 0
tot_bike_time=0
total_bike_time= 0
extra_bike_time= 0

for _ in distance:
    if transportation == "car":
        avg_car_km_h= 50    #average km per hour
        total_km += avg_car_km_h
        gas_stop= input("Did you have to stop for gas during your trip?")
        if gas_stop == "yes":
            total_time += 10 #minutes
        ####can add other variables
    if transportation == "bike":
        avg_bike_km_h =11
        total_km += avg_bike_km_h
        tot_bike_time= total_km/avg_bike_km_h
        bike_shed= input("Did you have to take the bike out of the shed?")
        if bike_shed == "yes":
            extra_bike_time = (5/60)
    total_bike_time = extra_bike_time + tot_bike_time
    if transportation == "walk":
        externality_walk = input("Did you experience any delay due to fatigue and therefore took breaks?") #why does it come back here?
        avg_walk_km_h= 5
        total_km += avg_walk_km_h
        walk_time= (distance_time/avg_walk_km_h)
        if externality_walk == "yes":
            amount_breaks= input("how many breaks did you take?")
            if amount_breaks == "yes":
                avg_break_time = (0.25)#15/60
                amount_breaks = float()
                total_break_time= amount_breaks*avg_break_time
                walk_time += total_break_time
        #elif externality_walk == "no":
         #       total_break_time = 0

total_time= walk_time+ total_break_time + total_bike_time #why is it not adding break time?
print("The time you took to your destination is ",total_time, " ,defined in hours including externalities")










