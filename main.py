import time
import json
import random
import openai
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

CHROMEDRIVER_PATH = '/Users/simransachdeva/Downloads/chromedriver' 
COOKIES_FILE = 'cookies.json'
OPENAI_API_KEY = ''  # OpenAI API key here

openai.api_key = OPENAI_API_KEY

def setup_driver():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    
    service = Service(CHROMEDRIVER_PATH)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    return driver

def save_cookies(driver, filename):
    """Save cookies to a JSON file."""
    with open(filename, 'w') as file:
        json.dump(driver.get_cookies(), file)

def load_cookies(driver, filename):
    """Load cookies from a JSON file."""
    with open(filename, 'r') as file:
        cookies = json.load(file)
        for cookie in cookies:
            driver.add_cookie(cookie)

def open_bumble():
    driver = setup_driver()

    driver.get("https://bumble.com/app")

    time.sleep(5)

    try:
        load_cookies(driver, COOKIES_FILE)
        print("Cookies loaded successfully.")
    except FileNotFoundError:
        print("Cookies file not found. Please log in manually.")
        return 

    driver.refresh()

    time.sleep(5)

    # Here, you should be logged in if the cookies are valid. but still just in case lol let's add a print statement
    print("You should be logged into Bumble.")

    return driver

def generate_chat_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=150
    )
    
    return response.choices[0].message['content'].strip()

def send_message(driver, message):
    try:
        message_box = driver.find_element(By.XPATH, '//textarea[@placeholder="Type a message"]')  
        message_box.send_keys(message)
        message_box.send_keys("\n")
        print("Message sent:", message)
    except Exception as e:
        print("Error sending message:", e)

def get_last_message(driver):
    try:
        last_message = driver.find_element(By.XPATH, '(//div[contains(@class, "message")])[last()]//div[contains(@class, "text")]').text  # Update this XPath if necessary
        return last_message
    except Exception as e:
        print("Error retrieving last message:", e)
        return None

def main():
    driver = open_bumble()

    if driver:
        driver.get("https://bumble.com/app/connections")
        time.sleep(5)

        matches = driver.find_elements(By.XPATH, '//div[contains(@class, "connection")]')
        if matches:
            random_match = random.choice(matches)

            random_match.click()
            time.sleep(5) 

            last_message = get_last_message(driver)

            if last_message:
                prompt = f"Generate a fun and engaging response to the following message, keep the tone semi-formal but conversational, no corporate jargon. sound flirty but keep it subtle: '{last_message}'"
                
                chat_response = generate_chat_response(prompt)

                send_message(driver, chat_response)
            else:
                print("No last message found.")

        else:
            print("No matches found.")

        time.sleep(5) 
        driver.quit()

if __name__ == "__main__":
    main()
