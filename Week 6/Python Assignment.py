#Revisiting exercise 2.4.2

distance = float(input("How far is your destination in kilometers?"))
transportation= input("What was your mode of transportation?")
#distance= float(distance)
total_km= 0
total_time= 0 # in minutes
avg_bike= 11 #11 kilometers/hour

for i in distance:
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
        bike_shed= input("Did you have to take the bike out of the shed?")
        if bike_shed == "yes":
            total_time += 5 #minutes
    if transportation == "walk":
        avg_walk_km_h= 5
        total_km += avg_walk_km_h
        walk_time= (avg_walk_km_h*distance)/60
        externality_walk= input("Did you experience any delay due to fatigue and therefore took breaks?")
        if externality_walk == "yes":
            amount_breaks= input("how many breaks did you take?")
            if amount_breaks == "yes":
                avg_break_time = 15
                amount_breaks = float()
                total_break_time= amount_breaks*avg_break_time
                walk_time += total_break_time
        total_time+= walk_time
    print(total_time)










