from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
import time

# Keep browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://orteil.dashnet.org/cookieclicker/')
driver.maximize_window()

# Click the consent
driver.find_element(By.CLASS_NAME, value="fc-cta-consent").click()
time.sleep(2)
# Click the language button
driver.find_element(By.CLASS_NAME, value="langSelectButton").click()
time.sleep(5)

cookies_per_second = 0
timeout = time.time() + 60*5
# timeout = time.time() + 15

while True:
    product_timeout = time.time() + 10
    
    while True:
        if time.time() < product_timeout:
            ## click the cookie
            driver.find_element(By.ID, value="bigCookie").click()
        else:
            ## click the product available
            ## get the class: enabled products in the div id: products
            products_available = driver.find_elements(By.CSS_SELECTOR, value='.product.enabled')
            ## click the last one available
            if len(products_available) > 0:
                products_available[len(products_available)-1].click()
            break

    if time.time() > timeout:
        ## get the cookies per second value
        try:
            cookies_per_second = driver.find_element(By.XPATH, value='//*[@id="cookiesPerSecond"]').text.split()[-1]
        except StaleElementReferenceException as e:
            cookies_per_second = driver.find_element(By.XPATH, value='//*[@id="cookiesPerSecond"]').text.split()[-1]
        break

driver.quit()
print (cookies_per_second)