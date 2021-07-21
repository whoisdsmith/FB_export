# выводит текст из постов - собирает ссылки на все загруженные в HTML посты и открывает каждый пост по ссылке.
# После чего извлекает код страницы и переводит из bs4.elem.ResultSet в list.
# Извлекает из полученного листа строки и удаляет все теги HTML.
# Информация может дублироваться

import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import re

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument("--disable-notifications")
#options.add_argument(
#    'user_agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36')  # для открытия headless-браузера
browser = webdriver.Chrome(executable_path=r'C:\chromedriver\chromedriver.exe', options=options)

email = input('Email facebook:')
password = input('Password facebook:')
url = input('Введите URL группы:')

links = [] #хранение ссылок на посты в bs4.elem.ResultSet
data = [] # хранение ссылок на посты в строках
content = [] # информация из поста

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


def get_links(data):
    cleaner1 = re.compile('<.*href="')
    cleaner2 = re.compile('" role.*a>')
    i = 0
    for i in range(len(data)):
        data[i] = re.sub(cleaner1, '', data[i])
        data[i] = re.sub(cleaner2,'',data[i])
    return data

def clean_html(data):
    cleaner = re.compile('<.*?>')
    i = 0
    for i in range(len(data)):
        clean_text = re.sub(cleaner,'',data[i])
        print(clean_text)
    return clean_text

def parse_url():
    print('Заходим в группу...')
    print('Scraping...')
    browser.get(url)
    time.sleep(2)

    browser.execute_script("window.scrollTo(0,700)")
    time.sleep(2)
    my_html = browser.page_source
    soup = BeautifulSoup(my_html, 'html.parser')
    post = soup.find_all(
        class_='oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl gmql0nx0 gpro0wi8 b1v8xokw')
    for links in post:
        data.append(str(links))
    get_links(data)

def open_post(data):
    i = 0
    for i in range(len(data)):
        browser.get(data[i])
        time.sleep(1)
        html = browser.page_source
        soup = BeautifulSoup(html, 'html.parser')
        posts = soup.find_all(class_={'gmql0nx0 l94mrbxd p1ri9a11 lzcic4wl aahdfvyu hzawbc8m'
                                     ,'kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x c1et5uql ii04i59q'
                                     ,'o9v6fnle cxmmr5t8 oygrvhab hcukyx3x c1et5uql ii04i59q'
                                     ,'oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl gmql0nx0 gpro0wi8 b1v8xokw'})
        for post in posts:
            content.append(str(post))
        time.sleep(1)
    print(clean_html(content))

auth_fb()
parse_url()
open_post(data)
