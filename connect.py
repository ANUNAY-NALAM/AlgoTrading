from kiteconnect import KiteConnect
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
from pyotp import TOTP


cwd = os.chdir("D:\\OneDrive\\Zerodha KiteConnect API\\1_account_authorization")

def autologin():
    token_path = "api_key.txt"
    key_secret = open(token_path,'r').read().split()
    kite = KiteConnect(api_key=key_secret[0])#intiate kit trading object
    service = webdriver.chrome.service.Service('./chromedriver')#starting crome driver
    service.start() 
    options = webdriver.ChromeOptions()
    options.add_argument('--headless') #if don't want to browser to render you can use headless in selenium
    options = options.to_capabilities()
    driver = webdriver.Remote(service.service_url, options)#starting an object called driver and passing service url
    driver.get(kite.login_url())
    driver.implicitly_wait(10)#waiting for url to render completly
    #find element by html path by locating it
    username = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]/form/div[1]/input')
    password = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]/form/div[2]/input')
    username.send_keys(key_secret[2])#send user name(typing username)
    password.send_keys(key_secret[3])#typing password using path
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]/form/div[4]/button').click()#click the login button
    pin = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div[1]/div[2]/div/div[2]/form/div[1]/input')
    totp = TOTP(key_secret[4])#entering totp
    token = totp.now()
    pin.send_keys(token)
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div[1]/div[2]/div/div[2]/form/div[2]/button').click()
    time.sleep(10)
    request_token=driver.current_url.split('request_token=')[1][:32]#taking the request token and saving
    with open('request_token.txt', 'w') as the_file:
        the_file.write(request_token)
    driver.quit()

autologin()
