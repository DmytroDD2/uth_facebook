import time
import logging
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait


logging.basicConfig(filename='out.log', level=logging.INFO)

def login_facebook(email, password):
    try:
        logging.info("Starting login to Facebook")
        driver = webdriver.Chrome()
        driver.get("https://www.facebook.com")

        logging.info("Locating login fields")
        email_input = driver.find_element(By.ID, "email")
        password_input = driver.find_element(By.ID, "pass")

        logging.info("Entering login credentials")
        email_input.send_keys(email)
        password_input.send_keys(password)
        password_input.send_keys(Keys.RETURN)

        logging.info("Waiting for page to load")
        time.sleep(5)

        if "captcha" in driver.current_url:
            logging.warning("reCAPTCHA detected. Manual verification required.")
            return

        wait = WebDriverWait(driver, 10)
        profile_pic = wait.until(
            EC.presence_of_element_located((By.XPATH, "//*[local-name()='svg']//*[local-name()='image']")))

        profile_pic_url = profile_pic.get_attribute("xlink:href")
        logging.info(f"Profile picture URL: {profile_pic_url}")
        print(f"Profile picture URL: {profile_pic_url}")

    except Exception as e:
        logging.error(f"An error occurred: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    email = "email"
    password = "pass"

    login_facebook(email, password)