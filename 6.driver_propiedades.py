from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service  import Service

# Configracion de las opciones
options = webdriver.ChromeOptions()
# Elimina los mensajes de consola
options.add_argument('--no-headless')               # Oculta el navegador
options.add_argument('--no-sandbox')                # Restringir el acceso a recursos(solo en Chrome) | Se utiliza para desactivar el sandbox del navegador Chrome                            
options.add_argument('--disable-dev-shm-usage')     # deshabilita el uso de una region de memoria compartida | evita datos temporales
options.add_argument('--disable-notifications')     # desactiva la funcionalidad de notificaciones del navegador
options.add_argument('start-maximized')             # maximizar la pantalla
options.add_argument('--disable-extensiones')       # impide que el navegador cargue y ejecute extensiones
options.add_experimental_option('excludeSwitches', ['enable-logging'])  # elimina los mensajes de consola

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

url = 'https://www.sbs.gob.pe/'
driver.get(url)

titulo = driver.title
navegador_nombre = driver.name
direccion_url = driver.current_url
id_ventana = driver.current_window_handle
html = driver.page_source
