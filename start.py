import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from snov_login import login_snov
from linkedin_login import login_linkedin
import config


def main():
    options = Options()
    options.add_argument(f'--load-extension={config.extension_path}')
    options.add_argument(f'--disk-cache-dir={config.disk_cache_dir}')
    options.add_argument("--window-size=1200,800")

    driver = webdriver.Chrome(options=options)

    try:
        login_snov(driver, config.snov_login, config.snov_pwd)
        time.sleep(2)
        login_linkedin(driver, config.linkedin_username, config.linkedin_password)
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
