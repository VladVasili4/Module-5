from time import sleep

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

    def log_in(self, login, password):
        print('UrTube.users:', UrTube.users)    # Ищет такого юзера, и если есть, current_user меняет на него,
        self.login = login                        # нужен цикл по распаковке списка и проверке на наличие
        self.password = password                  # Здесь по умолчанию подразумевается, что юзер существует в базе
        if len(self.users) > 0:
            for i in range(0, len(UrTube.users)):
                self.urs = UrTube.users[i]           # по идее это список из трех переменных login, password, age
                if self.login == self.urs[0]:
                    print(self.urs)
                    if hash(self.password) == hash(self.urs[1]):
                        UrTube.current_user = self.urs
                        print(f'Добро пожаловать. Теперь UrTube.current_user = {UrTube.current_user}')
                        start()
                    else:
                        print('Пароль не верен. Попробуйте еще раз')
                        start()
                else:
                    print('Tакой пользователь не зарегистрирован. Сначала зарегистрируйтесь')
                    start()
        else:
            print('Tакой пользователь не зарегистрирован. Сначала зарегистрируйтесь')
            start()

    def register(self, nickname, password, age):
        if UrTube.users:
            for i in range(0, len(UrTube.users)):
                self.urs = UrTube.users[i]
                if nickname == self.urs[0]:
                    print(f'Пользователь {nickname} уже существует')
                    start()
        self.nickname = nickname
        self.password = password
        self.age = age
        self.current_user = [self.nickname, self.password, self.age]
        print(f'UrTube.current_user заменен на {self.nickname} ')
        self.users.append(self.current_user)
        print('База пользователей "self.users" :', self.users)
        start()

    def log_out(self):  # для сброса текущего пользователя на None2
        print('До свидания, до новых встреч')
        del self.current_user

    def add(self, *video):
        """ принимает неограниченное кол-во объектов класса Video и все добавляет в videos,
            если с таким же названием видео ещё не существует. В противном случае ничего не происходит. """
        self.video = list(video)
        print('self.video :', self.video)
        for v in self.video:
            # tit = v.title
            if not v in self.videos:
                self.videos.append(v.title)
                print(UrTube.videos)
            # else:
            #     self.videos = self.videos
        start()

    def get_videos(self, word_):
        """ принимает поисковое слово и возвращает список названий всех видео, содержащих поисковое слово.
               Следует учесть, что слово 'UrbaN' присутствует в строке 'Urban the best' (не учитывать регистр)."""
        res = []
        for i in self.videos:
            self.word_ = word_
            if self.word_.lower() in i.lower():
                vibor = [i]
                res += vibor
        print(res)
        # start()

    def watch_video(self, title):
        """принимает название фильма, если не находит точного совпадения(вплоть до пробела), то ничего не воспроизводится,
            если же находит - ведётся отчёт в консоль на какой секунде ведётся просмотр.
            После текущее время просмотра данного видео сбрасывается."""
        """ Для паузы между выводами секунд воспроизведения можно использовать функцию sleep из модуля time.
                Воспроизводить видео можно только тогда, когда пользователь вошёл в UrTube.
                В противном случае выводить в консоль надпись: "Войдите в аккаунт, чтобы смотреть видео"
                Если видео найдено, следует учесть, что пользователю может быть отказано в просмотре, т.к. есть ограничения 18+.
                Должно выводиться сообщение: "Вам нет 18 лет, пожалуйста покиньте страницу"
                После воспроизведения нужно выводить: "Конец видео"""
        if title in self.videos:
            if self.current_user:
                print('self.current_user:', self.current_user)
                for i in range(0, len(self.video)):
                    vid = self.video[i]
                    if title == vid.title:
                        if self.age > 17 or (self.age < 17 and not vid.adult_mode):
                            for i in range(0, vid.duration):
                                # print(i)
                                sleep(1)
                                vid.time_now = i
                            # input('watch_video')
                            print('Конец видео')
                            exit()
                        else:
                            print("Вам нет 18 лет, пожалуйста покиньте страницу")
                            self.log_out()
                else:
                    input('exit')
                    start()
            else:
                print('Tакой пользователь не зарегистрирован. Сначала зарегистрируйтесь')
            start()
        print('Такого видео нет')
        start()

class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title                                                         # заголовок, строка
        self.duration = duration                                                   # продолжительность, секунды
        self.time_now = 0                                                          # секунда остановки, изначально 0
        self.adult_mode = adult_mode
        self.v = [self.title, self.duration, self.time_now, self.adult_mode]

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age
        print(f'Создали юзера c именем {self.nickname}, у которого пароль {self.password}, ему {self.age} лет')
        ur.register(self.nickname, self.password, self.age)

def register_():
    nickname = input('Введите Ваш логин :')
    password = ''
    age = input('Введите Ваш возраст :')  # проверка возраста
    if age.isdigit():
        age = int(age)
    else:
        print('Извините, попробуйте еще раз и введите возраст цифрами')
        register_()

    def password_check():
        pass_word = input('Введите Ваш пароль (Длина пароля не меннее 8 знаков. '  # проверка пароля
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
                user = User(nickname, password, age)
            else:
                print('пароли не совпадают, попробуйте еще раз')
                password_check()
        else:
            print('Пароль не соответствует уровню сложности, попробуй еще раз')
            password_check()

    password_check()

if __name__ == '__main__':
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    def start():
        choice = input('Выберите нужное действие : \n1 - Вход\n2 - Регистрация\n3 - Добавление видео\n'
                       '4 - Поиск видео\n5 - Просмотр фильма\n')

        if choice == '1':
            login = input('Введите Ваш логин :')
            password = input('Введите Ваш пароль :')
            ur.log_in(login, password)

        if choice == '2':
            register_()

        if choice == '3':
           ur.add(v1, v2)

        if choice == '4':
            print(ur.get_videos('лучший'))
            print(ur.get_videos('ПРОГ'))
            print(ur.get_videos('ДЕвуШКА'))
            # ur.watch_video()
            start()

        if choice == '5':
            choice5 = input('Что будете смотреть? \n1 - Лучший язык программирования 2024 года\n'
                            '2 - Для чего девушкам парень программист?')

            if choice5 == '1':
                ur.watch_video('Лучший язык программирования 2024 года')
                input('stop49')

            if choice5 == '2':
                ur.watch_video('Для чего девушкам парень программист?')
                input('stop50')

    start()







