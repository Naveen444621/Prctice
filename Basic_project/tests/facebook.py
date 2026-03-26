from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

# Step 1: Start browser
driver = webdriver.Chrome(service=Service(executable_path="C:\\Users\\NAVEEN KUMAR\\OneDrive\\Documents\\VS CODE\\Basic_project\\drivers\\chromedriver.exe"))

# Step 2: Open website
driver.get("https://www.amazon.in/")
driver.implicitly_wait(10)
driver.maximize_window()  
driver.title  
print(driver.title) 

driver.find_element(By.XPATH,"//a//span[contains(text(),'Account ')]").click()  # Click on the "Account & Lists" link

driver.implicitly_wait(15)

Login_page=driver.find_element(By.XPATH,"//input[@id='ap_email_login']")
Login_page.send_keys("sanjeevinaveenkumar391@gmail.com")

driver.implicitly_wait(10)

driver.find_element(By.XPATH,"//input[@class='a-button-input']").click()  # Click on the "Continue" button

driver.implicitly_wait(10)

element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//label[contains(text(),' Password')]")))

pass_word = driver.find_element(By.XPATH,"//input[@id='ap_password']")

driver.implicitly_wait(10)

pass_word.send_keys("Navee@444")

driver.implicitly_wait(10)

driver.find_element(By.ID,"signInSubmit").click()  
driver.implicitly_wait(10)
print("Login successful")

element = driver.find_element(By.XPATH, "//a//span[contains(text(),'Account ')]")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
element.click()  
driver.implicitly_wait(20)

element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'Your Account')]")))
print("Your Account page is displayed :", element.text)
print("thank you for script")


