from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def auto_check():
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    url = "https://www.ironspider.ca/forms/checkradio.htm"

    try:
        driver.get(url=url)
        driver.implicitly_wait(10)
        chekbox_list = driver.find_elements(By.TAG_NAME, "input")
        driver.implicitly_wait(10)
        for elem in chekbox_list:
            if elem.get_attribute("type") == "checkbox":
                elem.click()
                driver.implicitly_wait(10)
        time.sleep(100)
    except Exception as ex:
        print(ex)
    finally:
        ...
        # driver.close()
        # driver.quit()


if __name__ == '__main__':
    auto_check()
