### Komal Yaseen

### This file contains multiple classes. Each class searches and retrieves specific 
### information from the parsed json output.

import json

class Steps:
    def generate(self, json: 'json'):
        '''Searches json and prints step by step directions for the route to the location(s)'''
        print('DIRECTIONS')
        for item in json:
          for element in item["route"]["legs"]:
            for subitem in element["maneuvers"]:
              print(subitem["narrative"]);
        print()

class TotalDistance:
    def generate(self, json:'json'):
        '''Searches json and prints the total distance travelled'''
        distance = 0
        for element in json:
            distance += element["route"]["distance"]
        print ("Total Distance: ", round(distance), 'miles')
        print()

class TotalTime:
    def generate(self, json:'json'):
        '''Searches json and calculates and prints the times it takes to travel the route'''
        time = 0
        for element in json:
            time += element["route"]["time"]/60
        print("Total Time: ", round(time), 'minutes')
        print()

class LatLong:
    def generate(self, json:'json'):
        '''Searches json and prints the latitude/longtitude for each location'''
        lat_long = []
        for element in json:
          json_text = element["route"]["locations"]
          for item in json_text:
              if "displayLatLng" in item:
                  lat = item["displayLatLng"]["lat"]
                  long = item["displayLatLng"]["lng"]
                  if lat >=0:
                      if long >=0:
                          lat_long.append(str(abs(round(lat, 2))) + " N " + str(abs(round(long, 2))) + " E")
                      elif long < 0:
                          lat_long.append(str(abs(round(lat, 2)))+ " N " + str(abs(round(long, 2)))+ " W")
                  else:
                      if long >= 0:
                          lat_long.append(str(abs(round(lat, 2))) + " S " + str(abs(round(long, 2))) + " E")
                      elif long < 0:
                          lat_long.append(str(abs(round(lat, 2))) + " S " + str(abs(round(long, 2))) + " W")
        for item in list(set(lat_long)):
                print(item)
        print()
            
        
            

