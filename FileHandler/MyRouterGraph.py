import math


class Station:
    def __init__(self, id,coords):
        self.id = id     
        self.coord = coords  # North then west is tuple
        self.trains_passed_by = None # is set
        self.neighbour_st = None #is dictionary

class Train:
    def __init__(self, id, route, speed):
        self.id = id
        self.route = route #is list
        self.speed = speed 

def GetTrainsPassingBy(station, train_list):   #station here is an object of the class "Station"
    for train in train_list:
        for st in train.route:
            if station.id == st.id:
                station.trains_passed_by = st
                break

def DistanceCalc(station1, station2):
    first_x = station1.coords[0]  #is tuple, dont let the [] confuse u my G 
    first_y =

       

if __name__ == "__main__":
    stations_list = []
    train_list = [] #no diddy

    stations_list.append(Station("cannon street station",(51.5114, 0.0903)))
    stations_list.append(Station("St. James Park station",(51.4995, 0.1337)))
    stations_list.append(Station("water loo station",(51.5032, 0.1134)))
    stations_list.append(Station("London Bridge station ",(51.5043, 0.0848)))
    stations_list.append(Station("wimbledon park tube station",(51.4344, 0.1994)))
    stations_list.append(Station("London King's Cross Station", (51.5308, 0.1238)))
    stations_list.append(Station("London Paddington Station", (51.5152, 0.1750)))
    stations_list.append(Station("London Liverpool Street Station", (51.5178, 0.0824)))
    stations_list.append(Station("London Victoria Station", (51.4965, 0.1439)))
    stations_list.append(Station("Euston Station", (51.5281, 0.1337)))

    train_list.append(Train("Goku", [stations_list[1], stations_list[4],stations_list[6], stations_list[8], stations_list[9]]), 70)
    train_list.append(Train("Luffy", [stations_list[0], stations_list[2], stations_list[3], stations_list[5], stations_list[7]]), 70)
    train_list.append(Train("Flash", [stations_list[1], stations_list[3], stations_list[4], stations_list[7], stations_list[8]]), 70)


    
    