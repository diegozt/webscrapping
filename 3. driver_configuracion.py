from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service  import Service

# Configracion de las opciones
options = webdriver.ChromeOptions()
# Elimina los mensajes de consola
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

url = 'https://www.sbs.gob.pe/'
driver.get(url)
