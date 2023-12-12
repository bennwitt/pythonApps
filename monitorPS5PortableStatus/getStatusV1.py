import csv
from bs4 import BeautifulSoup, Comment
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from eyemsg import send_imessage
import pydantic

iMSGRecipient = "###########" #16085551234
ps5PortalRemotePlayerURL = "https://direct.playstation.com/en-us/buy-accessories/playstation-portal-remote-player?smcid=pdc:us-en:web-pdc-accessories-playstation-portal-remote-player:buttonblock-buy-now"
#ps5PortalRemotePlayerURL = "https://direct.playstation.com/en-us/buy-accessories/dualsense-wireless-controller"

def getStatus(url: str):
    options = webdriver.ChromeOptions()
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
    browser = webdriver.Chrome(options=options)
    timeout = 5

    try:
        browser.get(url)
        WebDriverWait(browser, timeout).until(EC.presence_of_all_elements_located((By.TAG_NAME, 'button')))
        pageSource = browser.page_source
        soup = BeautifulSoup(pageSource, 'html.parser')

        hidebutton = soup.find('button', class_='btn transparent-orange-button js-analyitics-tag add-to-cart hide')

        if hidebutton:
            print("Add Button Still Hidden")
            send_imessage(iMSGRecipient, "👎🏼 PlayStation Portal Remote Player: Add Button Still Hidden BOO!")
        else:
            print("Add Button Active")
            send_imessage(iMSGRecipient, "👍🏼 PlayStation Portal Remote Player: Add Button Active BUY BUY BUY!")
    
    finally:
        browser.quit()

def loop_getStatus(url, interval=600, duration=8*7200):
    start_time = time.time()
    end_time = start_time + duration

    while time.time() < end_time:
        getStatus(url)
        time.sleep(interval)

if __name__ == "__main__":

    loop_getStatus(ps5PortalRemotePlayerURL)
