from config import credential_dict
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


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
    
    return driver
    
def find_page(driver):
    page_name = input("Input the instagram page: \n")
    
    url = f'https://www.instagram.com/{page_name}'
    driver.get(url)
    driver.implicitly_wait(10)
    #check to see if inputted page is real
    try:
        driver.find_element(By.XPATH, value='//span[text()="Sorry, this page isn\'t available."]')
    except NoSuchElementException:
        return True
    else:
        return False

def follow_all(driver):
    followers_button = driver.find_element(By.XPATH, value="//a[contains(@href, 'followers')]").click()
    followers = driver.find_elements(By.XPATH, value="//div[contains(@class, 'x1dm5mii')]")
    for follower in followers:
        button = follower.find_element(By.TAG_NAME, value='button').click()
    print('done')


if  __name__ == "__main__":
    browser = main()
    valid_page = find_page(browser)
    if  valid_page:
        follow_all(browser)
    else:
        print('enter valid page')
        find_page(browser)
