### Komal Yaseen 

### This file reads the user input and constructs the objects that
### will generate the program's output. This file contains the 
### if __name__ == '__main__' block to make it executable. 

import mapquest_module
import classes_module

def user_interface():
    '''Prints out output based on specified user input.'''
    user_input2 = _number_of_specific_locations()

    json_result = []
    for i in range(len(user_input2) -1):
        json_result.append(mapquest_module.get_result(mapquest_module.build_url(user_input2[i], user_input2[i+1])))

    user_input = _number_of_specific_outputs()
    all_the_classes = []
    try:
        for i in user_input:
            if i == 'STEPS':
                all_the_classes.append(classes_module.Steps())
            elif i == 'TOTALDISTANCE':
                all_the_classes.append(classes_module.TotalDistance())
            elif i == 'TOTALTIME':
                all_the_classes.append(classes_module.TotalTime())
            elif i == 'LATLONG':
                all_the_classes.append(classes_module.LatLong())
    finally:
        for element in all_the_classes:
            element.generate(json_result)

def _number_of_specific_locations():
    '''Retrieves user input. User types in number specifying number of locations, 
    and then lists locations. Returns locations specified.'''
    while True:
        try:
            number_of_locations = int(input())
            locations = []
            for item in range(number_of_locations):
                locations.append(input())
            return locations
        except:
            print('The number you have entered is invalid. Please try again')

def _number_of_specific_outputs():
    '''Retrieves user input. User types in number specifying number of desired outputs,
    and lists which outputs they want. Returns outputs specified.'''
    while True:
        try:
            number_of_outputs = int(input())
            outputs = []
            for item in range(0,number_of_outputs):
                outputs.append(input().upper())
            return outputs
        except:
             print('The number you have entered is invalid. Please try again')

        
if __name__ == '__main__':
    user_interface()
    print('Directions Courtesy of MapQuest; Map Data Copyright OpenStreetMap Contributors')
