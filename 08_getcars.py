cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}
cars


def get_all_jeeps(cars=cars):
    """return a comma  + space (', ') separated string of jeep models (original order)"""
    jeeps = str()
    for car in cars['Jeep']:
        jeeps += car
        jeeps += ', '
    jeeps = jeeps[:-2]
    return jeeps
get_all_jeeps()
type(get_all_jeeps())
cars
def get_first_model_each_manufacturer(cars=cars):
    """return a list of matching models (original ordering)"""
    first_car = []
    for key, value in cars.items():
        first_car.append(value[0])
    return first_car
get_first_model_each_manufacturer()
print(get_first_model_each_manufacturer())
cars
def get_all_matching_models(cars=cars, grep='trail'):
    """return a list of all models containing the case insensitive
       'grep' string which defaults to 'trail' for this exercise,
       sort the resulting sequence alphabetically"""
    search_car = []
    for key,value in cars.items(): # getting each key and val for the dic
        for val in value: # the values are all lists which i can loop around
            if grep.lower() in val.lower():
                search_car.append(val)
    return sorted(search_car)
get_all_matching_models()
print(get_all_matching_models())
cars

def sort_car_models(cars=cars):
    """sort the car models (values) and return the resulting cars dict"""
    cars_sorted = {k: cars[k] for k in sorted(cars)}
    type(cars_sorted)
    for key,value in cars_sorted.items():
        value.sort()
    return cars_sorted
sort_car_models()

cars
