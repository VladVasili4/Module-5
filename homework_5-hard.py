import io
import os
import sys
import warnings
import termcolor
import pip
from typing import Any, Iterable
from time import sleep
# pip install termcolor
from termcolor import colored, cprint




""" Общее ТЗ:
Реализовать классы для взаимодействия с платформой, каждый из которых будет содержать методы добавления видео, 
авторизации и регистрации пользователя и т.д."""


class UrTube:
    """
    Каждый объект класса UrTube должен обладать следующими атрибутами и методами:
     Атриубты: users(список объектов User), videos(список объектов Video), current_user(текущий пользователь, User)
    Метод log_in, который принимает на вход аргументы: login, password и пытается найти пользователя в users с такими
    же логином и паролем. Если такой пользователь существует, то current_user меняется на найденного. Помните,
    что password передаётся в виде строки, а сравнивается по хэшу.
    Метод register, который принимает три аргумента: nickname, password, age, и добавляет пользователя в список, если
    пользователя не существует (с таким же nickname). Если существует, выводит на экран: "Пользователь {nickname} уже
    существует". После регистрации, вход выполняется автоматически.
    Метод log_out для сброса текущего пользователя на None.
    Метод add, который принимает неограниченное кол-во объектов класса Video и все добавляет в videos, если с таким же
    названием видео ещё не существует. В противном случае ничего не происходит.
    Метод get_videos, который принимает поисковое слово и возвращает список названий всех видео, содержащих поисковое
    слово.
    Следует учесть, что слово 'UrbaN' присутствует в строке 'Urban the best' (не учитывать регистр).
    Метод watch_video, который принимает название фильма, если не находит точного совпадения(вплоть до пробела),
    то ничего не воспроизводится, если же находит - ведётся отчёт в консоль на какой секунде ведётся просмотр.
    После текущее время просмотра данного видео сбрасывается.
    """
    users = []
    videos = []
    current_user = []
    def __init__(self):
       pass


    def log_in(self, login, password):       # Ищет такого юзера, и если есть, current_user меняет на него,
        self.login = login                     # нужен цикл по распаковке списка и проверке на наличие
        self.password = password                # Здесь по умолчанию подразумевается, что юзер существует в базе
        if len(UrTube.users) > 0:
            input('stop1')
            for i in range(0, len(UrTube.users)):
                input('stop2')
                self.urs = UrTube.users[i]          # по идее это список из трех переменных login, password, age
                input('stop3')
                if self.login == self.urs[0]:
                    print(self.urs)
                    input('stop4')
                    if hash(self.password) == hash(self.urs[1]):
                        input('stop6')
                        UrTube.current_user = self.urs
                        print(f'Добро пожаловать на наш видеохостинг. Теперь UrTube.current_user = {UrTube.current_user}')
                        input('Ждите')
                        start2()
                    else:
                        print('Пароль не верен. Попробуйте еще раз')
                        start()
                else:
                    print('Tакой пользователь не зарегистрирован. Сначала зарегистрируйтесь')
                    start()
        else:
            print('Извините, такой пользователь не зарегистрирован. Сначала зарегистрируйтесь')
            start()

    def register(self, nickname, password, age):    # Добавляет пользователя, если его нет
        self.nickname = nickname
        self.password = password
        self.age = age
        input(' ddd')
        self.usr = [self.nickname, self.password, self.age]
        if self.usr in UrTube.users:
            print(f'Пользователь {self.nickname} уже существует')
            UrTube.current_user = self.usr
            print(f'UrTube.current_user заменен на {self.nickname} ')
        else:
            UrTube.users.append(self.usr)
        print('База пользователей "self.users" :', self.users)
        UrTube.current_user = self.usr
        start2()

        pass



    def log_out(self):     # для сброса текущего пользователя на None
        print('До свидания, до новых встреч')
        del self





    def add(self, *video):
        """ принимает неограниченное кол-во объектов класса Video и все добавляет в videos,
            если с таким же названием видео ещё не существует. В противном случае ничего не происходит. """
        self.videos('video')
        pass


    def get_videos(self):
        """ принимает поисковое слово и возвращает список названий всех видео, содержащих поисковое слово.
               Следует учесть, что слово 'UrbaN' присутствует в строке 'Urban the best' (не учитывать регистр)."""
        pass




    def watch_video(self):
        """принимает название фильма, если не находит точного совпадения(вплоть до пробела), то ничего не воспроизводится,
            если же находит - ведётся отчёт в консоль на какой секунде ведётся просмотр.
            После текущее время просмотра данного видео сбрасывается."""
        """ Для паузы между выводами секунд воспроизведения можно использовать функцию sleep из модуля time.
                Воспроизводить видео можно только тогда, когда пользователь вошёл в UrTube.
                В противном случае выводить в консоль надпись: "Войдите в аккаунт, чтобы смотреть видео"
                Если видео найдено, следует учесть, что пользователю может быть отказано в просмотре, т.к. есть ограничения 18+.
                Должно выводиться сообщение: "Вам нет 18 лет, пожалуйста покиньте страницу"
                После воспроизведения нужно выводить: "Конец видео"""
        pass


class Video:
    def __int__(self, *args):
        self.title = 'title'                                # заголовок, строка
        self.duration = 'duration'                            # продолжительность, секунды
        self.time_now = 0                            # секунда остановки, изначально 0
        self.adult_mode = False
        pass


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age
        print(f'Создали юзера c именем {self.nickname}, у которого пароль {self.password}, ему {self.age} лет')
        my_canal.register(nickname, password, age)

def enter_():
    log = input('Введите Ваш логин :')
    pasw = input('Введите Ваш пароль :')
    my_canal.log_in(log, pasw)
    input("Ждем.......")

def register_():
    nickname = input('Введите Ваш логин :')
    password = ''
    age = input('Введите Ваш возраст :')        # проверка возраста
    if age.isdigit():
        age = int(age)
    else:
        print('Извините, попробуйте еще раз и введите возраст цифрами')
        register_()
    def password_check():
        pass_word = input('Введите Ваш пароль (Длина пароля не меннее 8 знаков. '               # проверка пароля
                           'Он должен содержать заглавные буквы, строчные буквы и цифры:')
        abc_ = []
        if len(pass_word) > 8:
            a = '0'
            b = 0
            c = 0
            for i in range(0, len(pass_word)):
                sign = pass_word[i]
                if sign.isdigit():
                    a = 1
                else:
                    d = 0
                if sign.islower():
                    b = 1
                else:
                    d = 0
                if sign.isupper():
                    c = 1
                else:
                    d = 0
            abc_ = [a, b, c]
        else:
            print('Пароль слишком короткий, попробуй снова')
            password_check()
        if abc_ == [1, 1, 1]:
            print('Ok')
            nonlocal password
            password = pass_word
            password_confirm = input('повторите пароль ')
            if hash(password) == hash(password_confirm):
                # password = hash(password)
                user = User(nickname, password, age)
            else:
                print('пароли не совпадают, попробуйте еще раз')
                password_check()
        else:
            print('Пароль не соответствует уровню сложности, попробуй еще раз')
            password_check()
    password_check()

def start2():
    choice2 = input('Переходим к действиям с видео, Но для начала проверим все функции входа\n '
                    'Выберите нужное действие : \n1 - Вход\n2 - Регистрация\n')
    if choice2 == '1':
        log = input('Введите Ваш логин :')
        pasw = input('Введите Ваш пароль :')
        my_canal.log_in(log, pasw)

    if choice2 == '2':
        register_()

    pass



if __name__ == '__main__':
    my_canal = UrTube()

    def start():
        choice = input('Выберите нужное действие : \n1 - Вход\n2 - Регистрация\n')

        if choice == '1':
            login = input('Введите Ваш логин :')
            password = input('Введите Ваш пароль :')
            my_canal.log_in(login, password)

        if choice == '2':
            register_()
    start()







