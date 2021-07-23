# Вытягивает ссылки на картинки из Медиафайлов после первоначальной подгрузки страницы (без прокрутки до начала)

from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.common.exceptions import NoSuchElementException

import time

options = webdriver.ChromeOptions()
#options.add_argument('headless')
options.add_argument("--disable-notifications")
options.add_argument(
   'user_agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36')  # для открытия headless-браузера
browser = webdriver.Chrome(executable_path=r'C:\chromedriver\chromedriver.exe', options=options)

email = input('Email facebook:')
password = input('Password facebook:')
url = input('Введите URL на медиа группы:')
#https://www.facebook.com/groups/1151106061594709/media

def auth_fb():
    try:
        print('Авторизация на Facebook...')
        browser.get('https://www.facebook.com/')
        browser.find_element_by_css_selector('#email').send_keys(email)
        browser.find_element_by_css_selector('#pass').send_keys(password)
        browser.find_element_by_name('login').click()
        time.sleep(3)
    except NoSuchElementException:
        print('Авторизация не выполнена.')

def parse_images(url):
    browser.get(url)
    time.sleep(2)
    html = browser.page_source
    soup = BeautifulSoup(html, 'html.parser')
    for link in soup.find_all('img'):
        print(link.get('src'))
    # сохранение картинки
    """ 
    for each in img:
        url = each.get('src')
        data = urlopen(url)
        with open(os.path.join(download_folder), "wb") as f:
            f.write(data.read())
    """

auth_fb()
parse_images(url)
