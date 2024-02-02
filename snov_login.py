from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def login_snov(driver, snov_login, snov_pwd):
    driver.get("https://app.snov.io/login?lang=en")
    driver.switch_to.window(driver.window_handles[0])
    WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-test='email']"))
    ).send_keys(snov_login)
    driver.find_element(By.CSS_SELECTOR, "input[data-test='password']").send_keys(snov_pwd)
    driver.find_element(By.CSS_SELECTOR, "button[data-test='submit-form']").click()
