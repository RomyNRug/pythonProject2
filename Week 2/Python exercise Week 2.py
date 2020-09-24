#Exercise Python Week 2

#Bike = 11 KM per Hour
#walking = 5 KM per Hour
#Car = 50 KM per Hour
#Trip is 75 KM away

bike = 11
walk = 5
car = 50
distance = 75

#in minutes
extra_bike= 5
extra_car= 15
extra_walk= 5
avg_speed= 45
avg_externalities = 30


name = input("What did you use to travel?")
extra = input("Did there occur any delay before departure")
speed = input("Did your trip take longer due to fatigue etc.?")
externalities = input ("Did you have to stop at gas station and/or was there a traffic jam?")

drive_time = distance /name
hour_time = drive_time + (speed/60) + (externalities/60) + (extra/60)

print ("Your time to arrive at the destination was ", hour_time)







