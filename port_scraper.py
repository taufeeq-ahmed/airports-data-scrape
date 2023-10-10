from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import json
from re import sub
driver = webdriver.Chrome()
driver.implicitly_wait(10)
def snake_case(s):
        return '_'.join(
            sub('([A-Z][a-z]+)', r' \1',
            sub('([A-Z]+)', r' \1',
            s.replace('-', ' '))).split()).lower()

def get_airport_data(selector):
        try:
            aiport_data_table_rows = driver.find_elements(By.CSS_SELECTOR,selector)
    
            airport_data = {}
            for p in range(0,len(aiport_data_table_rows)):
        
                row = aiport_data_table_rows[p]
                cells = row.find_elements(By.CSS_SELECTOR,'*')

                property = cells[0].text.lower()
                value = cells[1].text
                airport_data[snake_case(property)]=value
            return airport_data
        except NoSuchElementException:
            print("No Airport data")

def get_runway_data(selector):
        try:
            runway_table_rows = driver.find_elements(By.CSS_SELECTOR,selector)
    
            runway_data=[]
            prev_length=0
            prev_width=0
            prev_surface=0
            for p in range(1,len(runway_table_rows)):
        
                row = runway_table_rows[p]
                cells = row.find_elements(By.CSS_SELECTOR,'*')

            
                if len(cells)==8:
                    true_heading = cells[1].text
                    magnetic_heading = cells[2].text
                    length = cells[3].text
                    width = cells[4].text
                    surface = cells[5].text
                    latitude = cells[6].text
                    longitude = cells[7].text
                    prev_width=width
                    prev_length=length
                    prev_surface=surface
                
                    runway_data.append({
                        "true_heading":true_heading,
                        "magnetic_heading":magnetic_heading,
                        "length":length,
                        "width":width,
                        "surface":surface,
                        "latitude":latitude,
                        "longitude":longitude
                    })
                else: 
                    true_heading = cells[1].text
                    magnetic_heading = cells[2].text
                    latitude = cells[-1].text
                    longitude = cells[-2].text
                
                    runway_data.append({
                        "true_heading":true_heading,
                        "magnetic_heading":magnetic_heading,
                        "length":prev_length,
                        "width":prev_width,
                        "surface":prev_surface,
                        "latitude":latitude,
                        "longitude":longitude
                    })
        
            return runway_data
        except NoSuchElementException:
            print("No Airport data")

def get_nearby_data(selector):
        try:
            nearby_table_rows = driver.find_elements(By.CSS_SELECTOR,selector)
    
            nearby_data = []
            for p in range(0,len(nearby_table_rows)):
        
                row = nearby_table_rows[p]
                cells = row.find_elements(By.CSS_SELECTOR,'*')

                name = cells[3].text
                distance = cells[5].text
                direction = cells[6].text
                
                nearby_data.append({
                    "aiport_name":name,
                    "distance":distance,
                    "direction":direction
                })
            
            return nearby_data
        except NoSuchElementException:
            print("No Airport data")


def get_airport_full_data(link):
    driver.get(link)
    
    airport_data_selector = 'body > div.bg-primary.text-white.tab-height.position-relative > div > div.row > div.col-lg-5.pl-lg-3.mb-4.mb-lg-5 > table > tbody > tr'
    runway_data_selector = 'body > div.bg-primary.text-white.tab-height.position-relative > div > div.row > div.col-xl-9.mb-4.mb-xl-5.pr-xl-5 > div > table > tbody > tr'
    nearby_data_selector = 'body > div.bg-primary.text-white.tab-height.position-relative > div > div.row > div:nth-child(8) > div:nth-child(2) > table > tbody > tr'

    try:
        airport_button = driver.find_element(By.CSS_SELECTOR,'body > div.pb-2 > div > div > div > ul > li:nth-child(5) > a')
        airport_button.click()
    except NoSuchElementException:
            return {
                "aiport_data":{},
                "runway_data":[],
                'nearby_data':[]
            }

    airport_all_data = {
        "aiport_data":get_airport_data(airport_data_selector),
        "runway_data":get_runway_data(runway_data_selector),
        'nearby_data':get_nearby_data(nearby_data_selector)
    }
    return airport_all_data


def start_scrape():
    all_links_file = open('/Users/specter/Documents/COGOPORT/Repos/airports-scrape/all_unique_links.json')
    all_links = json.loads(all_links_file.read())
    
    airports_data =[]
    for i in range(1000,len(all_links)):
        airport_full_data = get_airport_full_data(all_links[i])
        airports_data.append(airport_full_data)
        print(i)
        if( (i+1)%500 == 0):
            json_data = json.dumps(airports_data)
            with open("first_"+str(i+1)+".json", "w") as outfile:
                outfile.write(json_data) 
        
    return airports_data

start_scrape()


