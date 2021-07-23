# выводит информацию о группе с помощью xpaths
# Так как на class подвязаны многие объекты, может выводить лишнюю информацию (например: непрочитанные уведомления)

from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.common.exceptions import NoSuchElementException
import time
import re

options = webdriver.ChromeOptions()
#options.add_argument('headless')
options.add_argument("--disable-notifications")
options.add_argument(
    'user_agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36')  # для открытия headless-браузера
browser = webdriver.Chrome(executable_path=r'C:\chromedriver\chromedriver.exe', options=options)

email = input('Email facebook:')
password = input('Password facebook:')
url = input('Введите URL на инфо группы:')
#https://www.facebook.com/groups/1151106061594709/about

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

def parse_info():
    info_about_group = {
        'main_title': browser.find_element_by_xpath(
            '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[4]/div/div[2]/div/div/div/div[1]/div/div/div/div/div/div[1]/div/div/div/div/div/h2/span/span').text
        , 'title': browser.find_element_by_xpath(
            '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[4]/div/div[2]/div/div/div/div[1]/div/div/div/div/div/div[2]/div[1]/div/div/span/div/div').text
        , 'accessibility': browser.find_element_by_xpath(
            '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[4]/div/div[2]/div/div/div/div[1]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div/div[1]/span/span').text
        , 'access_status': browser.find_element_by_xpath(
            '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[4]/div/div[2]/div/div/div/div[1]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div/div[2]/span/span').text
        , 'visibility': browser.find_element_by_xpath(
            '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[4]/div/div[2]/div/div/div/div[1]/div/div/div/div/div/div[2]/div[3]/div/div/div[2]/div/div[1]/span/span').text
        , 'visible_status': browser.find_element_by_xpath(
            '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[4]/div/div[2]/div/div/div/div[1]/div/div/div/div/div/div[2]/div[3]/div/div/div[2]/div/div[2]/span/span').text
        , 'location': browser.find_element_by_xpath(
            '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[4]/div/div[2]/div/div/div/div[1]/div/div/div/div/div/div[2]/div[4]/div/div/div[2]/div/div/span/span').text
        , 'status': browser.find_element_by_xpath(
            '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[4]/div/div[2]/div/div/div/div[1]/div/div/div/div/div/div[2]/div[5]/div/div/div[2]/div/div/span/span').text
    }

    participants = {
        'main_title': browser.find_element_by_xpath(
            '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[4]/div/div[2]/div/div/div/div[3]/div/div/div/div/div/div[1]/div/div/div/div/div/h2/span/span').text
        ,'admin': browser.find_element_by_xpath(
            '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[4]/div/div[2]/div/div/div/div[3]/div/div/div/div/div/div[2]/div[1]/div/div/div[2]/span/div/div/span').text
    }

    actions = {
        'main_title': browser.find_element_by_xpath(
            '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[4]/div/div[2]/div/div/div/div[4]/div/div/div/div/div/div[1]/div/div/div/div/div/h2/span/span').text
        ,'todays_news': browser.find_element_by_xpath(
            '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[4]/div/div[2]/div/div/div/div[4]/div/div/div/div/div/div[2]/div/div[1]/div/div/div[2]/div/div[1]/span').text
        ,'last_month_news': browser.find_element_by_xpath(
            '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[4]/div/div[2]/div/div/div/div[4]/div/div/div/div/div/div[2]/div/div[1]/div/div/div[2]/div/div[2]/span').text
        ,'number_followers': browser.find_element_by_xpath(
            '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[4]/div/div[2]/div/div/div/div[4]/div/div/div/div/div/div[2]/div/div[2]/div/div/div[2]/div/div[1]/span').text
        ,'last_month_followers': browser.find_element_by_xpath(
            '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[4]/div/div[2]/div/div/div/div[4]/div/div/div/div/div/div[2]/div/div[2]/div/div/div[2]/div/div[2]/span').text
        ,'creation_date': browser.find_element_by_xpath(
            '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[4]/div/div[2]/div/div/div/div[2]/div/div/div/div/div/div[2]/div[1]/div/div/div[2]/div/div[2]/span/span').text
    }
    print(info_about_group.values())
    print(participants.values())
    print(actions.values())

auth_fb()
