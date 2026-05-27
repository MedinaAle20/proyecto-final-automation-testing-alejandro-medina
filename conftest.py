import pytest
import logging
from datetime import datetime
from pathlib import Path
from utils.helpers import get_driver


LOGS_DIR = Path("logs")
SCREENSHOTS_DIR = Path("screenshots")

LOGS_DIR.mkdir(exist_ok=True)

logging.basicConfig(
    filename=LOGS_DIR / "ejecucion.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


@pytest.fixture
def driver():
    driver = get_driver()
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
            SCREENSHOTS_DIR.mkdir(exist_ok=True)
            fecha = datetime.now().strftime("%Y%m%d_%H%M%S")
            nombre_archivo = f"{item.name}_{fecha}.png"
            ruta_captura = SCREENSHOTS_DIR / nombre_archivo

            driver.save_screenshot(str(ruta_captura))
            logging.error(f"Captura guardada por fallo: {ruta_captura}")
