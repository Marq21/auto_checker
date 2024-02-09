from selenium import webdriver
import time

url2 = "https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/checkbox"
driver = webdriver.Edge()

try:
    driver.get(url=url2)
    time.sleep(5)
    driver.refresh()
    time.sleep(5)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
