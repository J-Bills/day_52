from config import credential_dict
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import InvalidArgumentException


def main():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('detach', True)
    #chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options)
    
    driver.get('https://www.instagram.com/')
    username_field = driver.find_element(By.NAME, value='username').send_keys(credential_dict.get('username'))
    password_field = driver.find_element(By.NAME, value='password').send_keys(credential_dict.get('password'))
    submit_button = driver.find_element(By.XPATH,value="//button[contains(@type, 'submit')]").click()
    driver.implicitly_wait(10)
    
    #have user input page to load
    return driver
    
def find_page(driver):
    page_name = input("Input the instagram page: \n")
    
    url = f'https://www.instagram.com/{page_name}/followers'
    driver.get(url)
    driver.implicitly_wait(10)
    # page_name = input("Input the instagram page: \n")
    # try:
    #     driver.get(f'https//www.instagram.com/{page_name}')
    # except InvalidArgumentException:
    #     print('invalid instagram page\n')
    #     find_page(driver)
    pass

def follow_all(driver):
    pass


if  __name__ == "__main__":
    browser = main()
    find_page(browser)
    follow_all(browser)