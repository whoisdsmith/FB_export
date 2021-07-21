import info
import media
import participants
import posts3
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

def main():
    print('Что вы хотите извлечь?')
    wish = input('Введите участники/медиа/информация/посты:')
    for case in switch(wish):
        if case('участники'):
            participants.get_html()
            break
        if case('медиа'):
            media.parse_images()
            break
        if case('информация'):
            info.parse_info()
            break
        if case('посты'):
            posts3.parse_url()
            break

main()

"""if __name__ == '__main__':
    main()"""

class switch(object):
    def __init__(self, value):
        self.value = value  # значение, которое будем искать
        self.fall = False   # для пустых case блоков

    def __iter__(self):     # для использования в цикле for
        """ Возвращает один раз метод match и завершается """
        yield self.match
        raise StopIteration

    def match(self, *args):
        """ Указывает, нужно ли заходить в тестовый вариант """
        if self.fall or not args:
            # пустой список аргументов означает последний блок case
            # fall означает, что ранее сработало условие и нужно заходить
            #   в каждый case до первого break
            return True
        elif self.value in args:
            self.fall = True
            return True
        return False