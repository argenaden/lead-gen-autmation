from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from extension_interaction import interact_with_extension


def login_linkedin(driver, linkedin_username, linkedin_password):
    driver.get("https://www.linkedin.com/login")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username"))).send_keys(linkedin_username)
    driver.find_element(By.ID, "password").send_keys(linkedin_password)
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()

    sales_nav_link = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'span[title="Sales Nav"]'))
    )
    sales_nav_link.click()
    driver.switch_to.window(driver.window_handles[2])
    time.sleep(4)

    saved_searches_button = WebDriverWait(driver, 30).until(
       EC.element_to_be_clickable((By.XPATH, '//button[@data-x--link--saved-searches]'))
    )
    saved_searches_button.click()
    time.sleep(5)
    link, datetime_attribute = open_first_link_with_datetime(driver)
    open_link_in_new_tab(driver, link)

    interact_with_extension()


def open_first_link_with_datetime(driver):
    panel_items = driver.find_elements(By.CLASS_NAME, "_panel-item_yma0zx")

    for panel_item in panel_items:
        try:
            datetime_element = panel_item.find_element(By.XPATH, './/time[@datetime]')
            datetime_attribute = datetime_element.get_attribute("datetime")

            if datetime_attribute:
                link = panel_item.find_element(By.TAG_NAME, 'a')
                return link, datetime_attribute

        except NoSuchElementException:
            print("Datetime attribute or link not found in this panel item")

    return None, None


def open_link_in_new_tab(driver, link):
    if link is not None:
        driver.execute_script(f'window.open("{link.get_attribute("href")}", "_blank");')
