from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://ru.wikipedia.org')
driver.get('https://mail.ru')
driver.get('https://yandex.ru')
driver.get('https://google.ru')
driver.quit()