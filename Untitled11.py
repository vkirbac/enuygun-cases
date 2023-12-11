from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

# Define search parameters
destination = "İstanbul"
departure = "İzmir"
date = "2023-12-15"
return_date = "2023-12-20"
passenger_count = 2

#Chrome browser
driver = webdriver.Chrome()

# Open the www.enuygun.com 
driver.get("https://www.enuygun.com/")

# Set 'From' input field
from_parent_div = WebDriverWait(driver, 2).until(
    EC.presence_of_element_located((By.CLASS_NAME, 'AutoSuggestion-module_auto-suggestion__OYLMb'))
)
from_input = from_parent_div.find_element(By.CSS_SELECTOR, 'input[role="combobox"]')
driver.execute_script(f"arguments[0].value = '{departure}';", from_input)

# Set 'To' input field
to_input = WebDriverWait(driver, 2).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-testid="endesign-flight-destination-autosuggestion"] input[role="combobox"]'))
)
from_input.click()
driver.execute_script(f"arguments[0].value = '{destination}';", to_input)

# Perform click actions for 'From' and 'To' inputs
action_chains = ActionChains(driver)
action_chains.move_to_element(from_input).click().send_keys(Keys.DOWN).send_keys(Keys.RETURN).perform()
action_chains.move_to_element(to_input).click().send_keys(Keys.DOWN).send_keys(Keys.RETURN).perform()

# Set departure date
departure_date_input = WebDriverWait(driver, 2).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-testid="enuygun-homepage-flight-departureDate-datepicker"] input[name="departureDate"]'))
)
driver.execute_script(f"arguments[0].value = '{date}';", departure_date_input)

# Set return date
return_date_input = WebDriverWait(driver, 2).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-testid="enuygun-homepage-flight-returnDate-datepicker"] input[name="returnDate"]'))
)
driver.execute_script(f"arguments[0].value = '{return_date}';", return_date_input)

# Select 'Non-stop' option
non_stop_input = WebDriverWait(driver, 2).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'div[class="Flight-module_checkboxWrapper__FlJ4S"] label[data-testid="flight-oneWayCheckbox-label"]'))
)
non_stop_input.click()

# Set passenger count
passenger_count_input = WebDriverWait(driver, 2).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-testid="enuygun-homepage-flight-selectPassengerAndCabin"] input[data-testid="undefined-popover-button"]'))
)
passenger_count_input.send_keys(str(passenger_count))

# Click the search button
search_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'button[data-testid="enuygun-homepage-flight-submitButton"]'))
)
search_button.click()

# Print success message
print("Search successfully performed. Moved to the next page.")
