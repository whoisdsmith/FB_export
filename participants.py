# возвращает список ссылок на участников путем прокрутки страницы до первого участника

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
url = input('Введите URL на страницу с участниками:')
#https://www.facebook.com/groups/1151106061594709/members

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

def parse_url():
    html = browser.page_source
    soup = BeautifulSoup(html, 'html.parser')
    #participants_data = soup.find_all(href=True, class_='oajrlxb2 gs1a9yip g5ia77u1 mtkw9kbi tlpljxtp qensuy8j ppp5ayq2 goun2846 ccm00jje s44p3ltw mk2mc5f4 rt8b4zig n8ej3o3l agehan2d sk4xxmp2 rq0escxv nhd2j8a9 q9uorilb mg4g778l btwxx1t3 pfnyh3mw p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x tgvbjcpo hpfvmrgz jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso l9j0dhe7 i1ao9s8h esuyzwwr f1sip0of du4w35lb lzcic4wl abiwlrkh p8dawk7l')
    for link in soup.find_all('a',class_='nc684nl6'):
        print(link.get('href'))

def get_html():
    print('Заходим в группу...')
    print('Список участников...')
    browser.get(url)
    pause_scroll = 2
    last_height = browser.execute_script("return document.body.scrollHeight")
    print('Scrolling...')

    while True:
        browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(pause_scroll)
        new_height = browser.execute_script("return document.body.scrollHeight")

        if new_height == last_height:
            break
        last_height = new_height

auth_fb()
get_html()
parse_url()
