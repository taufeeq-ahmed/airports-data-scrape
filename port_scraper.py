from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import json
driver = webdriver.Chrome()

driver.get("https://metar-taf.com/airport/VABB")
driver.implicitly_wait(3)

airport_data_selector = 'body > div.bg-primary.text-white.tab-height.position-relative > div > div.row > div.col-lg-5.pl-lg-3.mb-4.mb-lg-5 > table > tbody > tr'
runway_data_selector = 'body > div.bg-primary.text-white.tab-height.position-relative > div > div.row > div.col-xl-9.mb-4.mb-xl-5.pr-xl-5 > div > table > tbody > tr'
nearby_data_selector = ''

airport_button = driver.find_element(By.CSS_SELECTOR,'body > div.pb-2 > div > div > div > ul > li:nth-child(5) > a')
airport_button.click()

def get_airport_date():
    try:
        aiport_data_table_rows = driver.find_elements(By.CSS_SELECTOR,airport_data_selector)
    
        for p in range(0,len(aiport_data_table_rows)):
        
            row = aiport_data_table_rows[p]
            cells = row.find_elements(By.CSS_SELECTOR,'*')

            property = cells[0].text.lower()
            value = cells[1].text
            print(str(property)+" : "+str(value))
        
    except NoSuchElementException:
        print("No Airport data")
get_airport_date()


def get_runway_data():
    try:
        runway_table_rows = driver.find_elements(By.CSS_SELECTOR,runway_data_selector)
    
        for p in range(0,len(runway_table_rows)):
        
            row = runway_table_rows[p]
            cells = row.find_elements(By.CSS_SELECTOR,'*')

            property = cells[0].text.lower()
            value = cells[1].text
            print(str(property)+" : "+str(value))
        
    except NoSuchElementException:
        print("No Airport data")
get_runway_data()
