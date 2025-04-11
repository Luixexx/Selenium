from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import os

# Crear carpeta de evidencias
if not os.path.exists("evidencias"):
    os.makedirs("evidencias")

# Ruta del driver
service = Service('./chromedriver.exe')
driver = webdriver.Chrome(service=service)

try:
    # 1. Ingreso al sitio
    driver.get('https://www.saucedemo.com/')
    time.sleep(2)
    driver.save_screenshot('evidencias/01_login_page.png')

    login_btn = driver.find_element(By.ID, 'login-button')
    assert login_btn.is_displayed(), "El botón de login no está visible."

    # 2. Login con usuario válido
    driver.find_element(By.ID, 'user-name').send_keys('standard_user')
    driver.find_element(By.ID, 'password').send_keys('secret_sauce')
    login_btn.click()
    time.sleep(2)
    driver.save_screenshot('evidencias/02_logged_in.png')

    # Verificar que se muestra la lista de productos
    productos = driver.find_elements(By.CLASS_NAME, 'inventory_item')
    assert len(productos) > 0, "No se muestran productos después del login."

    # 3. Clic en un producto
    productos[0].find_element(By.CLASS_NAME, 'inventory_item_name').click()
    time.sleep(2)
    driver.save_screenshot('evidencias/03_product_detail.png')

    nombre = driver.find_element(By.CLASS_NAME, 'inventory_details_name').text
    descripcion = driver.find_element(By.CLASS_NAME, 'inventory_details_desc').text
    precio = driver.find_element(By.CLASS_NAME, 'inventory_details_price').text
    boton_add = driver.find_element(By.CLASS_NAME, 'btn_primary')

    assert nombre != "", "No se muestra el nombre del producto."
    assert descripcion != "", "No se muestra la descripción del producto."
    assert precio.startswith("$"), "El precio del producto no es válido."
    assert boton_add.is_displayed(), "El botón de agregar al carrito no está visible."

    # 4. Agregar al carrito
    boton_add.click()
    time.sleep(1)
    driver.save_screenshot('evidencias/04_added_to_cart.png')

    carrito_count = driver.find_element(By.CLASS_NAME, 'shopping_cart_badge').text
    assert carrito_count == "1", "El contador del carrito no es 1."

    boton_remove = driver.find_element(By.CLASS_NAME, 'btn_secondary')
    assert boton_remove.is_displayed(), "El botón 'Remove' no apareció después de agregar al carrito."

    # 5. Ir al carrito
    driver.find_element(By.CLASS_NAME, 'shopping_cart_link').click()
    time.sleep(2)
    driver.save_screenshot('evidencias/05_cart.png')

    items_carrito = driver.find_elements(By.CLASS_NAME, 'cart_item')
    assert len(items_carrito) > 0, "No hay productos en el carrito."

except AssertionError as e:
    print(f"[FALLÓ]: {e}")
except Exception as e:
    print(f"[ERROR]: {e}")
finally:
    driver.quit()
