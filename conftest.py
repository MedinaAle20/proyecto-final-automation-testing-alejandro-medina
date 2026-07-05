import json
import logging
from datetime import datetime
from pathlib import Path

import pytest

from utils.helpers import get_driver


# Carpetas donde quedan el reporte, los logs y las capturas.
REPORTS_DIR = Path("reports")
LOGS_DIR = REPORTS_DIR / "logs"
SCREENSHOTS_DIR = REPORTS_DIR / "screenshots"
DATA_FILE = Path("data") / "users.json"

LOGS_DIR.mkdir(parents=True, exist_ok=True)
SCREENSHOTS_DIR.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    filename=LOGS_DIR / "ejecucion.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    force=True,
)


def pytest_addoption(parser):
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Ejecuta las pruebas UI sin abrir el navegador.",
    )


@pytest.fixture(scope="session")
def test_data():
    # Datos externos para no dejar usuarios y checkout escritos dentro de los tests.
    with DATA_FILE.open(encoding="utf-8") as file:
        return json.load(file)


@pytest.fixture
def driver(request):
    # Cada test UI usa un navegador nuevo, asi los tests son independientes.
    driver = get_driver(headless=request.config.getoption("--headless"))
    yield driver
    driver.quit()


def pytest_runtest_logstart(nodeid, location):
    logging.info(f"Inicia test: {nodeid}")


def pytest_runtest_logreport(report):
    if report.when == "call":
        logging.info(f"Resultado test: {report.nodeid} - {report.outcome}")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    resultado = yield
    reporte = resultado.get_result()

    if reporte.when == "call" and reporte.failed:
        driver = item.funcargs.get("driver")

        if driver:
            # Si falla un test UI, guarda una captura con nombre del test y hora.
            fecha = datetime.now().strftime("%Y%m%d_%H%M%S")
            nombre_archivo = f"{item.name}_{fecha}.png"
            ruta_captura = SCREENSHOTS_DIR / nombre_archivo

            driver.save_screenshot(str(ruta_captura))
            logging.error(f"Captura guardada por fallo: {ruta_captura}")

            extra = getattr(reporte, "extras", [])
            pytest_html = item.config.pluginmanager.getplugin("html")
            if pytest_html:
                extra.append(pytest_html.extras.image(str(ruta_captura)))
                reporte.extras = extra
