cities = {
    'Chongqing': {
        'country': 'China',
        'population': '31,910,000',
        'fact': "Chongqing was China's wartime capital during World War II and is now a bustling megacity with a diverse economy."
    },

    'San Francisco': {
        'country': 'United States',
        'population': '809,000',
        'fact': "San Francisco is known for the Golden Gate Bridge."
    },

    'Brussels': {
        'country': 'Belgium',
        'population': '1,250,000',
        'fact': "Brussels is renowned for its delicious cuisine, particularly Belgian waffles."
    }
}

print("Which city would you like to know about?")
print("Here are the cities to select from: Chongqing, San Francisco, Brussels")

cityOption = input()

print(cities[cityOption])