from selenium import webdriver


# Variable de la ruta del chromedriver
ruta = r'chromedriver'
# Configuracion del driver
driver = webdriver.Chrome(executable_path=ruta)
# 
url = 'https://www.sbs.gob.pe/'
driver.get(url)
