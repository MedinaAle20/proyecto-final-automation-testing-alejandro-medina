# PreProyecto - Automatizacion SauceDemo
ALEJANDRO MEDINA

## Proposito del proyecto

Este proyecto automatiza pruebas web sobre el sitio https://www.saucedemo.com/.
El objetivo es validar flujos principales de una tienda demo, como login,
catalogo de productos, menu lateral y carrito de compras.

## Tecnologias utilizadas

- Python
- Selenium WebDriver
- Pytest
- Pytest HTML
- Google Chrome

## Instalacion de dependencias

Desde la carpeta del proyecto ejecutar el comando:

pip install -r requeriments.txt

## Ejecucion de pruebas

Para ejecutar todas las pruebas usar:

pytest

Para generar un reporte HTML usar:

pytest tests/test_saucedemo.py -v --html=reporte.html

El reporte se genera en el archivo:

reporte.html

## Evidencias

El proyecto genera un log de ejecucion en:

logs/ejecucion.log

Si una prueba falla, se guarda automaticamente una captura de pantalla en:

screenshots/

## Pruebas incluidas

- Login con credenciales validas.
- Validacion del catalogo de productos.
- Validacion del menu lateral.
- Agregado de productos al carrito.
