import undetected_chromedriver.v2 as uc
from selenium.webdriver.common.by import By
import time
import sys

if len(sys.argv) < 5:
    print("Please provide a destination airport, an arrival airport as well as the departure date and return date.")
    print("Airports should be provided using their trigram. Paris(Orly) => ORY, Barcelone => BCN.")
    print("Dates should be provided in the following format : ddmmyyyy")
    print("Example query : ORY BCN 01092021 13092021")
    exit(1)

options = uc.ChromeOptions()
options.add_argument(f'--proxy-server=socks5://127.0.0.1:9050') # TOR
# another way to set profile is the below (which takes precedence if both variants are used
options.add_argument('--user-data-dir=C:\\Users\\axoud\\Desktop\\Wiremind_test\\chrome_profile1')

# just some options passing in to skip annoying popups
options.add_argument('--no-first-run --no-service-autorun --password-store=basic')
driver = uc.Chrome(options=options)

driver.get('https://www.transavia.com/fr-FR/accueil/')  # known url using cloudflare's "under attack mode"

time.sleep(6)

departure_airport_input = sys.argv[1]
departure_airport = driver.find_element(By.ID,"routeSelection_DepartureStation-input")
departure_airport.send_keys(departure_airport_input)

time.sleep(3)

arrival_airport_input = sys.argv[2]
arrival_airport = driver.find_element(By.ID,"routeSelection_ArrivalStation-input")
arrival_airport.send_keys(arrival_airport_input)

time.sleep(4)

span = driver.find_element(By.XPATH, '//span[text()="Rechercher les vols"]')
button_search = span.find_element(By.XPATH,"..")
button_search.click()

time.sleep(10)

flight_numbers = driver.find_elements(By.CLASS_NAME,"flight-number") # "Numéro de vol TO3150 , Numéro de vol TO4033"
times = driver.find_elements(By.XPATH, "//div[contains(@class,'times')]")
prices = driver.find_elements(By.XPATH, "//div[contains(@class,'price')]")