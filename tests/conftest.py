import logging
import subprocess
import time
import pytest
from appium import webdriver
from utils.android_utils import android_get_desired_capabilities
from datetime import datetime


@pytest.fixture(scope='session')
def run_appium_server():
    """Запуск appium сервера"""
    subprocess.Popen(
        ['appium', '-a', 'localhost', '-p', '4723', '--allow-insecure', 'adb_shell'],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        stdin=subprocess.DEVNULL,
        shell=True
    )
    time.sleep(5)


@pytest.fixture(scope='session')
def get_udid(run_appium_server):
    """Визначення udid пристрою через subprocess"""
    udid_bytes = subprocess.check_output(["adb", "devices"])
    udid = udid_bytes.decode()
    return udid.split('\n')[1].split('\t')[0]


@pytest.fixture(scope='session')
def driver(get_udid):
    """Ініціалізація драйверу пристрою"""
    logging.basicConfig(filename='test_results.log', level=logging.INFO)
    capabilities = android_get_desired_capabilities()
    capabilities['udid'] = get_udid
    driver = webdriver.Remote('http://localhost:4723/wd/hub', capabilities)
    yield driver
    driver.quit()


def pytest_terminal_summary(terminalreporter):
    """Збирання логів виконаних тестів після їх проходження"""
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    file_path = f"logs/test_{datetime.now().date().strftime('%d.%m.%Y')}_{datetime.now().time().strftime('%H.%M.%S')}"
    handler = logging.FileHandler(file_path)
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    for elem in terminalreporter.stats.get('failed', []):
        logger.error(f"Test {elem.nodeid} FAILED!. Duration: {elem.duration}")
    for elem in terminalreporter.stats.get('passed', []):
        logger.info(f"Test {elem.nodeid} PASSED!. Duration: {elem.duration}")
