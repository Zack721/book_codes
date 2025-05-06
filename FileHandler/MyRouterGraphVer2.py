import math

SPEED = 70

class Station:
    def __init__(self, station_id,coords):
        self.station_id = station_id     
        self.coords = coords  # west then north (x, y) is tuple
        self.trains_passed_by = set() # is set
        self.neighbour_st = dict() #is dictionary

class Train:
    def __init__(self, train_id, route):
        self.train_id = train_id
        self.route = route #is list
        self.speed = SPEED 

def GetTrainsPassingBy(station, train_list):   #station here is an object of the class "Station"
    for train in train_list:
        for st in train.route:
            if station.station_id == st.station_id:
                station.trains_passed_by.add(train)
                break

def LinkingNeighbours(train_list): #doing my own thing, calcs distance between the current and next station in route
    for train in train_list:
        for refernce_station in train.route:
            for station in train.route:
                if refernce_station != station:
                    distance = DistanceCalc(refernce_station.coords, station.coords)
                
                    refernce_station.neighbour_st[station.station_id] = distance
            
def DistanceCalc(coords1, coords2): #doing my own thing, calcs distance between the current and next station in route
            first_x ,first_y= coords1 #is tuple, dont let the [] confuse u my G 
            second_x, second_y = coords2

            #lines 31 to 45
            # Convert degrees to radians
            first_x = math.radians(first_x)
            first_y = math.radians(first_y)
            second_x = math.radians(second_x)
            second_y = math.radians(second_y)

            # Differences
            dx = second_x - first_x
            dy = second_y - first_y

            #Haversine formula
            a = math.sin(dy / 2)**2 + math.cos(first_y) * math.cos(second_y) * math.sin(dx / 2)**2
            c = 2 * math.asin(math.sqrt(a))
            r = 6371  # Earth radius in kilometers
            return c * r
            
if __name__ == "__main__":
    stations_list = []
    train_list = [] #no diddy lol

    #STation creation here and append to stations_list with arguments:stattion_id, coordinates
    stations_list.append(Station("cannon street station",( 0.0903, 51.5114)))
    stations_list.append(Station("St. James Park station",( 0.1337, 51.4995)))
    stations_list.append(Station("water loo station",( 0.1134, 51.5032)))
    stations_list.append(Station("London Bridge station ",( 0.0848, 51.5043)))
    stations_list.append(Station("wimbledon park tube station",(0.1994, 51.4344 )))
    stations_list.append(Station("London King's Cross Station", ( 0.1238, 51.5308)))
    stations_list.append(Station("London Paddington Station", ( 0.1750, 51.5152)))
    stations_list.append(Station("London Liverpool Street Station", ( 0.0824, 51.5178)))
    stations_list.append(Station("London Victoria Station", ( 0.1439, 51.4965)))
    stations_list.append(Station("Euston Station", (0.1337, 51.5281)))
    
    
    #Train creation here and append to train_list with arguments:train_id, route(list of stations it'll pass)
    train_list.append(Train("Goku", [stations_list[1], stations_list[4],stations_list[6], stations_list[8], stations_list[9]]))#get the stations objects straight from the list of stations
    train_list.append(Train("Luffy", [stations_list[0], stations_list[2], stations_list[3], stations_list[5], stations_list[7]]))
    train_list.append(Train("Flash", [stations_list[1], stations_list[3], stations_list[4], stations_list[7], stations_list[8]]))


    for station in stations_list:    #finds trains passing by for all stations
        GetTrainsPassingBy(station, train_list)

    LinkingNeighbours(train_list)

    for station in stations_list: #proof it works
        print(station.neighbour_st)
    
    