from Scripts.selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

# Define Chrome options
chrome_options = Options()
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])


# pytest.fixture ile test ortamını yapılandırabiliriz & her teste başlamadan önce belirli işlemleri gerçekleştirmek
# için.
#@pytest.fixture(params=["chrome", "firefox"])  # fixture decorator ile belirli işlevler tanımlanır.
@pytest.fixture
def driver(request):
    #browser = request.param
    browser = request.config.getoption("--browser")
    print(f"Creating {browser} driver")
    # Use the defined chrome_options when creating the webdriver
    if browser == "chrome":
        my_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    elif browser == "firefox":
        my_driver = driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    else:
        raise TypeError(f"Expected 'chrome' or 'firefox', but got {browser}")
    my_driver.implicitly_wait(10)
    yield my_driver
    print(f"Closing {browser} driver")
    my_driver.quit()


def pytest_addoption(
        parser):  # Özel komut satırı  -- Test davranışı ve yapılandırılması ile ilgli özel komut satırı çalıştırmak için.
    parser.addoption(
        "--browser", action="store", default="chrome", help="browser to execute tests(chrome or firefox)"
    )
    # parser.addoption işlevi komut satırı seçeneklerini tanımlamaya ve bu seçenekleri
    # pytest çalıştırıcısına iletmek için kullanılır.
    # Komut satırı kullanımı:  pytest --browser chrome
    # Komut satırı kullanımı : pytest --browser firefox
    # Özellikle testlerin farklı platformlarda veya tarayıcılarda
    # çalıştırılması gerektiğinde bu tür seçeneklerin kullanılması yaygındır.

# Notes: yield ve return farkı: return: bir test işlemi veya kaynağı oluşturur ve test işlemi tamamlandığında bu
# kaynağı temizlemez. yield:yield ifadesi, bir test işlemi veya özel bir kaynak (örneğin, bir web sürücüsü) oluşturur
# veya hazırlar ve test işlemi tamamlandığında bu kaynağı temizler. Bu, testin başında bir ön hazırlık yapmanıza ve
# test sonunda kaynakları düzgün bir şekilde temizlemenize olanak tanır. yield kullanıldığında, test işlevi bir
# jeneratör işlevi olarak kabul edilir ve yield ifadesinin ardından işlevin çalışması durur ve kaynak veya veri test
# işlemine sağlanır. Test tamamlandığında, temizlik işlemleri otomatik olarak yapılır.
