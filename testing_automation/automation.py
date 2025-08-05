from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
 
service = Service(executable_path='C:/Users/DreamDreams/Documents/VSCode/testing_automation/chromedriver.exe')
 
options = Options()
options.add_experimental_option('detach', True) #this ensures chrome window does not close
 
chrome_browser = webdriver.Chrome(service=service, options=options)
chrome_browser.maximize_window() 
chrome_browser.get('https://omayo.blogspot.com/')

button = chrome_browser.find_element(By.CLASS_NAME, 'dropbtn')
print(button.get_attribute('innerHTML'))

assert 'Dropdown' in chrome_browser.page_source
dispbtn = chrome_browser.find_element(By.ID, 'prompt')
ta = chrome_browser.find_element(By.ID, 'ta1')
ta.clear()
ta.send_keys('I am extra cool')
dispbtn.click()

