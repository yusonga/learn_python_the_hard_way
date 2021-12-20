#create a mapping of stat to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
    }

    #creat a basic set of states and some cities in them
cities = {
        'CA': 'San Francisco',
        'MI': 'Detoit',
        'FL': 'Jacksonville'
        }
    #add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

    #print out some cities
print('_' * 10)
print("NY State has: ", cities['NY'])
print("OR State has: ", cities['OR'])

# print some states
print('_' * 10)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])


    # do it by using the state then cities dic
print('_' * 10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

# print every state abbreviation
print('_' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

#print evert city in state
print('_' * 10)
for abbrev, city in list(states.items()):
    print(f"{abbrev} has the city {city}")

#now do both at the same time
print('_' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

print('_' * 10)
        #safely get a abbreviation by stat that might not be Theres
state = states.get('Texas')

if not state:
    print("Sorry, no Texas.")

            #get a city with a default value
city  = cities.get('TX', 'Does Not Exist')
print(f"The city for the state 'TX' is: {city}")
