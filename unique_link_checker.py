import json
 
all_links_file = open('/Users/specter/Documents/COGOPORT/Repos/airports-scrape/all_links.json')
all_links = json.loads(all_links_file.read())

unique_links_set = set(all_links)
unique_links_list = list(unique_links_set);

json_data = json.dumps(unique_links_list)
with open("all_unique_links.json", "w") as outfile:
    outfile.write(json_data)