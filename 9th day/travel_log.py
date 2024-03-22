country = "Brazil" # Add country name
visits = 2 # Number of visits
list_of_cities = ["Sao Paulo", "Rio de Janeiro"] # create list from formatted string

travel_log = [
  {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
  },
  {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  },
]
# Do NOT change the code above 👆

# TODO: Write the function that will allow new countries
# to be added to the travel_log. 
def add_new_country(country, visits, list_of_cities):
    travel_log.append({
        "country": country,
        "visits": visits,
        "cities": list_of_cities
    })

# Do not change the code below 👇
add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")


travel_log2 = {
    "France": {
        "Paris": {  
                    "num_of_visits": 4,
                    "would_visit_again": True,
                    "favourite_restaurants": ["McDo", "Escargot", "Grenouille", "Ratatouille"]
                },
        "Lille": 3,
        "Dijon": 8,
        "Marseilles": 0,
        "Charbonnières-des-Bains": 0
    },
    "Germany": {
        "Berlin": True,
        "Regensburg": False,
        "Stuttgart": True,
        "Hamburg": True
    }
}

travel_log2["France"]["Lille"]
