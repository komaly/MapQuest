MapQuest Directions

Given specific locations, this program connects to the MapQuest Open Directions API
by building a URL with the given locations and making an HTTP request. It retrieves
the parsed JSON result from this request, and displays the specified output by retrieving
the information from the JSON result. 

The user is prompted for the number of locations to retrieve directions for. After
specifying this number, the user is prompted to enter the name of each location. 
The user then inputs how many outputs they desire, and then specifies what types of 
outputs they desire. The user chooses from 4 options: STEPS, TOTALDISTANCE, 
TOTALTIME, or LATLONG. After specifying which options they want to output, the program
connects to the MapQuest Open Directions API, retrieves the JSON result,
and searches the JSON result for the specified output information.