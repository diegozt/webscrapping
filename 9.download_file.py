from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service  import Service

from selenium.webdriver.common.by import By # Importacion para el tipo de Busqueda
from time import sleep
import requests
from os import path, mkdir


# Configracion de las opciones
options = webdriver.ChromeOptions()
# Elimina los mensajes de consola
# options.add_argument('--no-headless')               # Oculta el navegador
options.add_argument('--no-sandbox')                # Restringir el acceso a recursos(solo en Chrome) | Se utiliza para desactivar el sandbox del navegador Chrome                            
options.add_argument('--disable-dev-shm-usage')     # deshabilita el uso de una region de memoria compartida | evita datos temporales
options.add_argument('--disable-notifications')     # desactiva la funcionalidad de notificaciones del navegador
options.add_argument('start-maximized')             # maximizar la pantalla
options.add_argument('--disable-extensiones')       # impide que el navegador cargue y ejecute extensiones
options.add_experimental_option('excludeSwitches', ['enable-logging'])  # elimina los mensajes de consola

driver = webdriver.Chrome(options=options)

url = 'https://the-internet.herokuapp.com/download'
driver.get(url)
sleep(2)

# Buscar elemento
xpath_input = "//div[@id='content']//div[@class='example']//a"
elementos_links: list = driver.find_elements(By.XPATH, xpath_input)

# Crear carpeta en caso no exista
download_path = r'./descargas'
if not path.exists(download_path):
    mkdir(download_path)

for elemento in elementos_links:
    nombre = elemento.text
    download_path_file = path.join(download_path, nombre)
    # Link
    href = elemento.get_attribute('href')
    # Descargar file
    response = requests.get(href)
    with open(download_path_file, 'wb') as f:
        f.write(response.content)

