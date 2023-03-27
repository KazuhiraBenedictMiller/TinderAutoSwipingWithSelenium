import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

chrome_driver_path = "./chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)

driver.get("http://www.tinder.com")

main_page = driver.current_window_handle

#Accepting Cookies
time.sleep(5)
AcceptCookies = driver.find_element(By.XPATH, '//*[@id="q-1787539962"]/div/div[2]/div/div/div[1]/div[1]/button/div[2]/div[2]')
AcceptCookies.click()

#Logging In
time.sleep(5)
LoginButton = driver.find_element(By.XPATH, '//*[@id="q-1787539962"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
LoginButton.click()

#Choose Facebook and Log in
time.sleep(5)
FBButton = driver.find_element(By.XPATH, '//*[@id="q779046258"]/main/div/div/div[1]/div/div/div[3]/span/div[2]/button/div[2]/div[2]/div/div')
FBButton.click()

#Switch Handle and get in the PopUp Page
for handle in driver.window_handles:
    if handle != main_page:
        login_page = handle
        driver.switch_to.window(login_page)

#Make sure you've Created a Facebook account Linked with a Tinder Profile

FB_EMAIL = YOUR FACEBOOK LOGIN EMAIL
FB_PASSWORD = YOUR FACEBOOK PASSWORD

time.sleep(5)
email_input = driver.find_element(By.NAME, "email")
email_input.send_keys(FB_EMAIL)

password_input = driver.find_element(By.NAME, "pass")
password_input.send_keys(FB_PASSWORD)

time.sleep(2)
password_input.send_keys(Keys.ENTER)

#Return to Main Window

driver.switch_to.window(main_page)

#Acknowledge Tinder Permissions

time.sleep(10)
AcknowledgePosition = driver.find_element(By.CLASS_NAME, "l17p5q9z")
AcknowledgePosition.click()

time.sleep(5)
AcknowledgeNotifications = driver.find_element(By.CLASS_NAME, "l17p5q9z")
AcknowledgeNotifications.click()

while True:
    time.sleep(2)

    try:
        # Hit Dislike Button
        Nope = driver.find_element(By.XPATH, '//*[@id="q-1787539962"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[2]/button/span/span')

        Nope.click()

        # Catches the cases where there is a "Matched" pop-up in front of the "Like" button:
    except ElementClickInterceptedException:
        try:
            #You'd have to work around the CSS Selector of the Item that you want to click on based on different PopUps, I've been Detected and Banned from Tinder :(
            PopUp = driver.find_element(By.CSS_SELECTOR, "INSERT CSS SELECTOR HERE")
            PopUp.click()

        # Catches the cases where the "Nope" button has not yet loaded, so wait 2 seconds before retrying.
        except NoSuchElementException:
            time.sleep(2)

driver.quit()