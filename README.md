# Proyecto Final - Automation Testing

Autor: Alejandro Medina

## Proposito del proyecto

Este proyecto es un framework de automatizacion de pruebas desarrollado en Python para la entrega final del curso. Incluye pruebas UI sobre SauceDemo y pruebas API sobre JSONPlaceholder, aplicando Page Object Model, datos externos, reportes HTML, logging y screenshots automaticos ante fallos.

Sitio web demo: https://www.saucedemo.com/

API publica: https://jsonplaceholder.typicode.com/

## Tecnologias utilizadas

- Python
- Pytest
- Selenium WebDriver
- Requests
- Pytest HTML
- Page Object Model
- Git y GitHub

## Estructura del proyecto

```text
.
├── conftest.py
├── data/
│   └── users.json
├── pages/
│   ├── base_page.py
│   ├── cart_page.py
│   ├── checkout_page.py
│   ├── inventory_page.py
│   ├── login_page.py
│   └── menu_page.py
├── reports/
│   ├── logs/
│   │   └── ejecucion.log
│   └── screenshots/
├── requirements.txt
├── tests/
│   ├── api/
│   │   └── test_jsonplaceholder_api.py
│   └── ui/
│       └── test_saucedemo_ui.py
└── utils/
    └── helpers.py
```

## Instalacion de dependencias

Desde la carpeta raiz del proyecto:

```bash
pip install -r requirements.txt
```

## Ejecucion de pruebas

Ejecutar todos los tests:

```bash
pytest
```

Ejecutar solo pruebas UI:

```bash
pytest tests/ui
```

Ejecutar solo pruebas API:

```bash
pytest tests/api
```

Ejecutar pruebas UI sin abrir la ventana del navegador:

```bash
pytest tests/ui --headless
```

## Reporte HTML

Generar el reporte HTML:

```bash
pytest --html=reports/reporte.html --self-contained-html
```

El reporte queda disponible en:

```text
reports/reporte.html
```

El reporte muestra los tests ejecutados, su estado, duracion y detalles de fallos. Si una prueba UI falla, el framework guarda una captura y la agrega al reporte cuando el plugin Pytest HTML esta disponible.

## GitHub Actions

El proyecto incluye un workflow basico en:

```text
.github/workflows/tests.yml
```

Este workflow se ejecuta en cada push o pull request hacia `master` o `main`. Instala las dependencias, ejecuta la suite completa en modo headless y publica el reporte HTML como artefacto del pipeline.

## Logs y screenshots

El log de ejecucion se guarda en:

```text
reports/logs/ejecucion.log
```

Los screenshots automaticos por fallo se guardan en:

```text
reports/screenshots/
```

El nombre de cada captura incluye el nombre del test y la fecha/hora, por ejemplo:

```text
test_login_invalido_20260705_153000.png
```

## Datos de prueba

Los datos externos se encuentran en:

```text
data/users.json
```

Incluyen usuario valido, usuarios invalidos, datos de checkout y productos esperados del catalogo.

## Pruebas UI incluidas

- Login exitoso con usuario valido.
- Login invalido con datos incorrectos y usuario bloqueado.
- Validacion del catalogo de productos.
- Agregado de productos al carrito.
- Checkout completo.
- Validacion del menu lateral y logout.

## Pruebas API incluidas

- GET de lista de usuarios.
- POST de creacion de usuario.
- DELETE de usuario.

## Buenas practicas aplicadas

- Page Object Model para separar interaccion con la pagina y logica de tests.
- Tests independientes entre si.
- Uso de waits explicitos en Selenium.
- Datos de prueba externos en JSON.
- Logging centralizado.
- Screenshots automaticos ante fallos.
- Separacion clara entre pruebas UI y API.
