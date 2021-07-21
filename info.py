# выводит информацию о группе с помощью атрибута class
# Так как на class подвязаны многие объекты, может выводить лишнюю информацию (например: непрочитанные уведомления)

from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.common.exceptions import NoSuchElementException
import time
import re

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument("--disable-notifications")
# options.add_argument(
#    'user_agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36')  # для открытия headless-браузера
browser = webdriver.Chrome(executable_path=r'C:\chromedriver\chromedriver.exe', options=options)

email = input('Email facebook:')
password = input('Password facebook:')
url = input('Введите URL на инфо группы:')

def auth_fb():
    try:
        print('Авторизация на Facebook...')
        browser.get('https://www.facebook.com/')
        browser.find_element_by_css_selector('#email').send_keys(email)
        browser.find_element_by_css_selector('#pass').send_keys(password)
        browser.find_element_by_name('login').click()
        time.sleep(3)
        browser.get(url)
        time.sleep(2)
    except NoSuchElementException:
        print('Авторизация не выполнена.')
    parse_info()

def clean_html(data):
    cleaner = re.compile('<.*?>')
    i = 0
    for i in range(len(data)):
        clean_text = re.sub(cleaner,'',data[i])
        print(clean_text)
    return clean_text

def parse_info():
    print('Заходим в Инфо...')
    html = browser.page_source
    soup = BeautifulSoup(html, 'html.parser')
    info = soup.find_all(class_={'d2edcug0 hpfvmrgz qv66sw1b c1et5uql lr9zc1uh jagab5yi g1cxx5fr ekzkrbhg oo9gr5id',
                                 'd2edcug0 hpfvmrgz qv66sw1b c1et5uql lr9zc1uh sq6gx45u j5wam9gi knj5qynh oo9gr5id'
                                 'd2edcug0 hpfvmrgz qv66sw1b c1et5uql lr9zc1uh gfeo3gy3 a3bd9o3v knj5qynh oo9gr5id',
                                 'a8c37x1j ni8dbmo4 stjgntxs l9j0dhe7 ojkyduve',
                                 'd2edcug0 hpfvmrgz qv66sw1b c1et5uql lr9zc1uh jagab5yi g1cxx5fr lrazzd5p m9osqain',
                                 'd2edcug0 hpfvmrgz qv66sw1b c1et5uql lr9zc1uh gfeo3gy3 a3bd9o3v knj5qynh oo9gr5id hzawbc8m',
                                 'd2edcug0 hpfvmrgz qv66sw1b c1et5uql lr9zc1uh a8c37x1j keod5gw0 nxhoafnm aigsh9s9 d3f4x2em fe6kdd0r mau55g9w c8b282yb iv3no6db gfeo3gy3 a3bd9o3v knj5qynh oo9gr5id hzawbc8m',
                                 'd2edcug0 hpfvmrgz qv66sw1b c1et5uql lr9zc1uh a8c37x1j keod5gw0 nxhoafnm aigsh9s9 d9wwppkn fe6kdd0r mau55g9w c8b282yb mdeji52x sq6gx45u j5wam9gi knj5qynh m9osqain hzawbc8m'
                                  }) #последние два класса из доп. акка
    data = []
    for x in info:
        data.append(str(x))

    print(clean_html(data))

auth_fb()
