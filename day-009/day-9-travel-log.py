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
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
def add_new_country(country_visited, number_of_visits, list_cities_visited):
    new_country = {
        "country": country_visited, 
        "visits": number_of_visits,
        "cities": list_cities_visited
    }
    travel_log.append(new_country)
    print(f"You've visited {country_visited} {number_of_visits} times.")

    cities_visited = ""
    for city in list_cities_visited:
        if city  != list_cities_visited[-1]:
            cities_visited += city
            cities_visited += " and "
        else:
            cities_visited += city
    print(f"You've been to {cities_visited}")


#🚨 Do not change the code below
add_new_country(country_visited="Russia", number_of_visits=2,list_cities_visited=["Moscow", "Saint Petersburg", "Abakan", "Bely"])
print(travel_log)