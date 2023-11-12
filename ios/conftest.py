from _pytest.fixtures import fixture
from appium.options.ios import XCUITestOptions
from appium.webdriver.appium_service import AppiumService
from appium import webdriver

APPIUM_PORT = 4723
APPIUM_HOST = '127.0.0.1'


@fixture(scope='session')
def appium_service():
    service = AppiumService()
    service.start(
        # Check the output of `appium server --help` for the complete list of
        # server command line arguments
        args=['--address', APPIUM_HOST, '-p', str(APPIUM_PORT)],
        timeout_ms=20000,
    )
    yield service
    service.stop()


@fixture
def ios_driver_factory():
    options = XCUITestOptions()
    options.device_name = "iPhone 15 Pro Max"
    options.platformVersion = "iOS 17.0"
    options.app = 'com.apple.mobilesafari'

    # Appium1 points to http://127.0.0.1:4723/wd/hub by default
    yield webdriver.Remote(f'http://{APPIUM_HOST}:{APPIUM_PORT}', options=options)
