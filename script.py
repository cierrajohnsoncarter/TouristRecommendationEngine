# List of destinations
destinations = ['Paris, France', 'Shanghai, China', 'Los Angeles, USA',
                'Sao Paulo, Brazil', 'Cairo, Egypt', 'Atlanta, USA', 'Versailles, France']

# First test traveler for tourist engine
test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

# Function to identify each location based on its index in the 'destinations' list


def get_destination_index(destination):
    destination_index = destinations.index(destination)
    return destination_index


print(get_destination_index('Paris, France'))

# Function to get the index of the destination where the traveler is


def get_traveler_location(traveler):
    traveler_destination = traveler[1]
    traveler_destination_index = get_destination_index(traveler_destination)
    return traveler_destination_index


test_destination_index = get_traveler_location(test_traveler)
print(test_destination_index)

# List to maintain a list of attractions
attractions = [[] for destination in destinations]

# Funtion for adding an attraction to a destination that ignores a destination passed that does not exist


def add_attraction(destination, attraction):
    destination_index = get_destination_index(destination)
    try:
        destination_index = get_destination_index(destination)
        attractions_for_destination = attractions[destination_index].append(
            attraction)
    except ValueError:
        return


# Attractions for different locations
add_attraction('Los Angeles, USA', ['Venice Beach', ['beach']])
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", [
               "historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", [
               "garden", "historcical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", [
               "skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("Sao Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("Sao Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", [
               "monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])
add_attraction("Atlanta, USA", ["Coca-Cola Museum", ["museum"]])
add_attraction("Versailles, France", ["Palace of Versailles", ["museum"]])
print(attractions)

# Function to help travelers find interesting places in a new city for them


def find_attractions(destination, interests):
    destination_index = get_destination_index(destination)
    attractions_in_city = attractions[destination_index]
    attractions_with_interest = []
    for attraction in attractions_in_city:
        possible_attraction = attraction
        attraction_tags = attraction[1]
        for interest in interests:
            if interest in attraction_tags:
                attractions_with_interest.append(possible_attraction[0])
                return attractions_with_interest


la_arts = find_attractions('Los Angeles, USA', ['art'])
print(la_arts)

# Function to connect travelers with attractions they are interested in


def get_attractions_for_traveler(traveler):
    traveler_destination = traveler[1]
    traveler_interests = traveler[2]
    traveler_attractions = find_attractions(
        traveler_destination, traveler_interests)

# Message to traveler when application opens to show them what they may be interested in
    interests_string = 'Hi '
    interests_string = interests_string + \
        traveler[0] + " we think you'll like these places around " + \
        traveler_destination + ': '
    for i in traveler_attractions:
        interests_string += i
        return interests_string


results_france = get_attractions_for_traveler(
    ['Cierra', 'Paris, France', ['monument']])
print(results_france)
