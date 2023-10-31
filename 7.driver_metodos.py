from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service  import Service

from selenium.webdriver.common.by import By # Importacion para el tipo de Busqueda
from time import sleep


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

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

url = 'https://www.sbs.gob.pe/'
driver.get(url)

# Busca el elemento boton: LUPA
# Todas las etiquetas a que tengan el atributo equivalente a search-btn: //a[@id="search-btn"]
xpath_elemento_boton_buscar = '//a[@id="search-btn"]'
elemento_boton_buscar = driver.find_element(by=By.XPATH, value=xpath_elemento_boton_buscar)

# Tomar imagen del elemento
nombre_archivo = 'captura.png'
ruta_archivo = f'./evidencias/{nombre_archivo}'
elemento_boton_buscar.screenshot(ruta_archivo)
# Hacer click en el elemento capturado
elemento_boton_buscar.click()
# Obtenemos el input del buscador 
xpath_elemento_input_buscar = "//input[@id='TextoBuscador']"
elemento_input_buscar = driver.find_element(by=By.XPATH, value=xpath_elemento_input_buscar)
# Ingresamos un valor en el input
input_buscar = 'Valorizacion de Instrumentos'
elemento_input_buscar.send_keys(input_buscar)
#Introducir una tecla en particular dentro del input
from selenium.webdriver.common.keys import Keys
elemento_input_buscar.send_keys(Keys.ENTER)
# Esperamos 1 segundos
sleep(1)
xpath_elementos_links = '//div[@class="seek-result"]//div[@class="seek-result--text"]//h3//a'
elementos_buscar = driver.find_elements(by=By.XPATH, value=xpath_elementos_links)
# Elegir el primer elemento
primer_elemento = elementos_buscar[0]
# Extraemos el HREF del primer elemento
href = primer_elemento.get_attribute('href')
# Cargamos la pagina
driver.get(href)
# Tomar imagen de pantalla
nombre_archivo = 'pantallazo.png'
ruta_archivo = f'./evidencias/{nombre_archivo}'
driver.save_screenshot(ruta_archivo)
# Hacer scroll a la pantalla
driver.execute_script("window.scrollTo(0, 2000)")
sleep(1)

