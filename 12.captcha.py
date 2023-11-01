from selenium import webdriver
from selenium.webdriver.common.by import By # Importacion para el tipo de Busqueda
from selenium.webdriver.common.action_chains import ActionChains

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

driver = webdriver.Chrome(options=options)

url = "http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html"
driver.get(url)
sleep(2)

# Buscar elemento origen
xpath_a = "//div[@id='box1']"
source_element = driver.find_element(By.XPATH, xpath_a)

# Buscar elemento destino
xpath_b = "//div[@id='box106']"
target_element = driver.find_element(By.XPATH, xpath_b)

# Instanciamos el actions
actions = ActionChains(driver)

# Generamos el efecto de movimiento
actions.drag_and_drop_by_offset(source_element, 200, 0).perform()

sleep(2)

# Realizamos el otro movimiento
actions.drag_and_drop(source_element, target_element).perform()

sleep(2)
