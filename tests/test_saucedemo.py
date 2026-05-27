from utils.helpers import login
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_login(driver):
    
    login(driver, "standard_user", "secret_sauce")
    assert "inventory.html" in driver.current_url
    
    title = driver.find_element(By.CSS_SELECTOR, ".title").text
    assert title == "Products"
    print("Login exitoso")
    
def test_catalogo_productos(driver):
    
    login(driver, "standard_user", "secret_sauce")
    assert "inventory.html" in driver.current_url
    print("Login exitoso")
    
    title = driver.find_element(By.CSS_SELECTOR, ".title").text
    assert title == "Products"
    print("Lista de productos visibles")
    
    productos = driver.find_elements(By.CSS_SELECTOR, "[data-test='inventory-item']")
    assert len(productos) > 0
    
    #nombre = productos[0].find_element(By.CSS_SELECTOR, "[data-test='inventory-item-name']").text
    #assert nombre == "Sauce Labs Backpack"
    #print('Producto encontrado "Sauce Labs Backpack"')
    
    for producto in productos:
        nombre = producto.find_element(By.CSS_SELECTOR, "[data-test='inventory-item-name']").text
        precio = producto.find_element(By.CSS_SELECTOR, "[data-test='inventory-item-price']").text
        print(f'Producto encontrado "{nombre}" - Precio: {precio}')
    
def test_validacion_interfaz(driver):
    
    login(driver, "standard_user", "secret_sauce")
    assert "inventory.html" in driver.current_url
    print("Login exitoso")
    
    title = driver.find_element(By.CSS_SELECTOR, ".title").text
    assert title == "Products"
    print("Lista de productos visible")
    
    menu = driver.find_element(By.ID, "react-burger-menu-btn")
    assert menu.is_displayed()
    print("Menu visible")
    menu.click()
    print("Click exitoso en menu")
    
    wait = WebDriverWait(driver, 10)
    opciones_menu = {
        "inventory-sidebar-link": "All Items",
        "about-sidebar-link": "About",
        "logout-sidebar-link": "Logout",
        "reset-sidebar-link": "Reset App State",
    }
    
    for data_test, texto_esperado in opciones_menu.items():
        opcion = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, f"[data-test='{data_test}']"))
        )
        assert opcion.is_displayed()
        assert opcion.text == texto_esperado
        print(f'Boton "{texto_esperado}" visible')
    
def test_agregar_al_carrito(driver):
    
    login(driver, "standard_user", "secret_sauce")
    assert "inventory.html" in driver.current_url
    print("Login exitoso")
    
    title = driver.find_element(By.CSS_SELECTOR, ".title").text
    assert title == "Products"
    print("Lista de productos visibles")
    
    wait = WebDriverWait(driver, 10)
    
    #productos = driver.find_element(By.CSS_SELECTOR, "[data-test='inventory-item-name']").text
    productos = driver.find_elements(By.CSS_SELECTOR, "[data-test='inventory-item-name']")
    nombres_productos = [producto.text for producto in productos]

    for nombre_producto in nombres_productos:
        print(nombre_producto)
    
    driver.find_element(By.CSS_SELECTOR, "[data-test='add-to-cart-sauce-labs-backpack']"
    ).click()
    
    driver.find_element(By.CSS_SELECTOR, "[data-test='add-to-cart-sauce-labs-bike-light']"
    ).click()
    
    driver.find_element(By.CSS_SELECTOR, "[data-test='add-to-cart-sauce-labs-bolt-t-shirt']"
    ).click()
    
    driver.find_element(By.CSS_SELECTOR, "[data-test='add-to-cart-sauce-labs-fleece-jacket']"
    ).click()
    
    driver.find_element(By.CSS_SELECTOR, "[data-test='add-to-cart-sauce-labs-onesie']"
    ).click()
    
    driver.find_element(By.CSS_SELECTOR, "[data-test='add-to-cart-test.allthethings()-t-shirt-(red)']"
    ).click()
    
    print("Click exitoso en 'Add to cart'")
    
    badge = driver.find_element (By.CSS_SELECTOR, "[data-test='shopping-cart-badge']")
    assert badge.text == "6"
    
    driver.find_element(By.CSS_SELECTOR, "[data-test='shopping-cart-link']").click()
    
    productos_carrito = driver.find_elements(By.CSS_SELECTOR, "[data-test='inventory-item-name']")
    
    nombres_carrito = [producto.text for producto in productos_carrito]
    
    assert nombres_carrito == nombres_productos
    
    for nombre_producto in nombres_carrito:
        print(f'Producto "{nombre_producto}" agregado exitosamente')

