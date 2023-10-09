SUPPORTED_AIPORT_TYPES = ['midsized airport','large airport']

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import json
driver = webdriver.Chrome()

driver.get("https://metar-taf.com/countries")

selector = 'body > div.bg-primary.text-white > div > div > div:nth-child(2) > section:nth-child(3) > nav > a'

countriesLength = len(driver.find_elements(By.CSS_SELECTOR, selector))

AIRPORT_LINKS = []
CONTINENT = 'antarctica'

for p in range(0, countriesLength):
    country = driver.find_elements(By.CSS_SELECTOR,selector)[p]
    country.click()
    print("p is :",str(p))
    
    is_pagination_next = True

    while(is_pagination_next):
            airPortsList = driver.find_elements(By.CSS_SELECTOR,'#w1 > table > tbody > tr')
            for q in range(0,len(airPortsList)):
                airPortsList = driver.find_elements(By.CSS_SELECTOR,'#w1 > table > tbody > tr')
                print("length :"+str(len(airPortsList)))
                print("q is :"+str(q))
                row = airPortsList[q]
                cells = row.find_elements(By.CSS_SELECTOR,'*')
        
                airport_type = cells[-1].text.lower()
                airport_link = cells[1].find_element(By.TAG_NAME,'a').get_attribute('href')
        
                if airport_type in SUPPORTED_AIPORT_TYPES:
                    AIRPORT_LINKS.append(airport_link)
    
            try:
                driver.find_element(By.CSS_SELECTOR,'#w1 > ul')
                
                try:
                    driver.find_element(By.CSS_SELECTOR,'#w1 > ul > li.next.page-item.disabled')
                    is_pagination_next=False
                except NoSuchElementException:
                    is_pagination_next=True
                    
            except NoSuchElementException:
                    is_pagination_next=False
            
            if is_pagination_next:
                print("next_button clicked")
                next_button = driver.find_element(By.CSS_SELECTOR,'#w1 > ul > li.next')
                next_button.click()
                
    driver.get("https://metar-taf.com/countries")

    
json_data = json.dumps(AIRPORT_LINKS)
with open(CONTINENT+"_airport_links.json", "w") as outfile:
    outfile.write(json_data)
driver.quit()


