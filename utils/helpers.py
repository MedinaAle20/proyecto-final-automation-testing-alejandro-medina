from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def get_driver(headless=False):
    # Configuracion comun del navegador para las pruebas de Selenium.
    options = Options()
    options.add_argument("--window-size=1366,768")

    if headless:
        options.add_argument("--headless=new")

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    return driver
