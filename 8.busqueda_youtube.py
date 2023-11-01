from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service  import Service

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By # Importacion para el tipo de Busqueda
from time import sleep


# Configracion de las opciones
options = webdriver.ChromeOptions()
# Elimina los mensajes de consola
options.add_argument('--no-headless')                # Oculta el navegador
options.add_argument('--no-sandbox')                # Restringir el acceso a recursos(solo en Chrome) | Se utiliza para desactivar el sandbox del navegador Chrome                            
options.add_argument('--disable-dev-shm-usage')     # deshabilita el uso de una region de memoria compartida | evita datos temporales
options.add_argument('--disable-notifications')     # desactiva la funcionalidad de notificaciones del navegador
options.add_argument('start-maximized')             # maximizar la pantalla
options.add_argument('--disable-extensiones')       # impide que el navegador cargue y ejecute extensiones
options.add_experimental_option('excludeSwitches', ['enable-logging'])  # elimina los mensajes de consola

driver = webdriver.Chrome(options=options)

url = 'https://www.youtube.com/'
driver.get(url)

xpath_btn_buscar = '//input[@id="search"]'
boton_buscar = driver.find_element(by=By.XPATH, value=xpath_btn_buscar)
boton_buscar.send_keys('Musica de los 80')
boton_buscar.send_keys(Keys.ENTER)

sleep(2)

xpath_detail = '//h3[count(text()) > 2]'
elemento_detail = driver.find_elements(By.XPATH, xpath_detail)

datos = [i.text for i in elemento_detail]

# Exportar
ruta_archivo = './data_youtube/data.txt'
file = open(ruta_archivo, "w")
datos_texto = "\n".join(datos)
file.write(datos_texto)
file.close()
