SUPPORTED_AIPORT_TYPES = ['midsized airport','large airport']

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import json
driver = webdriver.Chrome()

driver.get("https://metar-taf.com/countries")

selector = 'body > div.bg-primary.text-white > div > div > div:nth-child(1) > section:nth-child(2) > nav  > a'

euroCountriesLength = len(driver.find_elements(By.CSS_SELECTOR, selector))

EUROPE_LINKS = []


for p in range(0, euroCountriesLength):
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
                    EUROPE_LINKS.append(airport_link)
    
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

    
json_data = json.dumps(EUROPE_LINKS)
with open("europe_airport_links.json", "w") as outfile:
    outfile.write(json_data)
driver.quit()


