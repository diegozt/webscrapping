from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service  import Service


chrome_manager = ChromeDriverManager().install()
service = Service(chrome_manager)

driver = webdriver.Chrome(service=service)

url = 'https://www.sbs.gob.pe/'
driver.get(url)
