import json
 
african = open('/Users/specter/Documents/COGOPORT/Repos/airports-scrape/airports_links/african_airport_links.json')
antarctica = open('/Users/specter/Documents/COGOPORT/Repos/airports-scrape/airports_links/antarctica_airport_links.json')
asia = open('/Users/specter/Documents/COGOPORT/Repos/airports-scrape/airports_links/asia_airport_links.json')
europe = open('/Users/specter/Documents/COGOPORT/Repos/airports-scrape/airports_links/europe_airport_links.json')
north_american = open('/Users/specter/Documents/COGOPORT/Repos/airports-scrape/airports_links/north_american_airport_links.json')
south_american = open('/Users/specter/Documents/COGOPORT/Repos/airports-scrape/airports_links/south_american_airport_links.json')
oceania = open('/Users/specter/Documents/COGOPORT/Repos/airports-scrape/airports_links/oceania_airport_links.json')

data = [
    json.loads(african.read()),
    json.loads(antarctica.read()),
    json.loads(asia.read()),
    json.loads(europe.read()),
    json.loads(north_american.read()),
    json.loads(oceania.read()),
    json.loads(south_american.read()),
]

resData =[]

for country in data:
    for portLink in country:
        resData.append(portLink)
        
json_data = json.dumps(resData)
with open("all_links.json", "w") as outfile:
    outfile.write(json_data)

