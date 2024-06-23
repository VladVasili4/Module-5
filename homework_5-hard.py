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
    def __int__(self):
       pass


    def log_in(self, login, password):   # Ищет такого юзера, и если есть, current_user меняет на него
        self.login = login
        if self.login in my_canal.users.current_user:
            if UrTube.users[self.login] == hash(password):
                UrTube.current_user = self.login
                print(f'Добро пожаловать на наш видеохостинг. Теперь UrTube.current_user = {UrTube.current_user}')
            else:
                print('Пароль не верен. Попробуйте еще раз')
                enter_()
                input()
        else:
            print('Извините, такой пользователь не зарегистрирован. Попробуйте еще раз')
            start()



    def register(self, nickname, password, age):    # Добавляет пользователя, если его нет
        self.nickname = str(nickname)
        self.password = password
        self.age = age
        UrTube.current_user = User(nickname, password, age)
        UrTube.users.append(UrTube.current_user)
        # self.users[self.nickname] = self.password
        print('self.users :', self.users)
        print(f'Пользователь {self.nickname} уже существует')



    def log_out(self):     # для сброса текущего пользователя на None
        print('До свидания, до новых встреч')
        del self





    def add(self, video):
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
        pass


    def watch_video(self):
        """ Для паузы между выводами секунд воспроизведения можно использовать функцию sleep из модуля time.
        Воспроизводить видео можно только тогда, когда пользователь вошёл в UrTube.
        В противном случае выводить в консоль надпись: "Войдите в аккаунт, чтобы смотреть видео"
        Если видео найдено, следует учесть, что пользователю может быть отказано в просмотре, т.к. есть ограничения 18+.
        Должно выводиться сообщение: "Вам нет 18 лет, пожалуйста покиньте страницу"
        После воспроизведения нужно выводить: "Конец видео"""







class Video:
    def __int__(self, title, duration, time_now, adult_mode):
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
    input()




def register_():
    nickname = input('Введите Ваш логин :')
    age = input('Введите Ваш возраст :')
    if age.isdigit():
        age = int(age)
    else:
        print('Извините, введите, пожалуйста цифрами')
        print()
        # register_()
    password = hash(input('Введите Ваш пароль:'))
    password_confirm = hash(input('Повторите пароль :'))
    if password != password_confirm:
        print('Пароли не совпадают, попробуйте еще раз')
        # start()
    else:
        user = User(nickname, password, age)



# def vozrast_digit():
#     while True:
#         age = input("Сколько Вам лет?  ")
#         if age.isdigit():
#             vozrast_(age)
#         else:
#             print('Извините, введите, пожалуйста цифрами')
#
# def vozrast_(age):
#     age = int(age)
#     if age < 18:
#         print('Вам нет 18 лет, пожалуйста покиньте страницу')
#         exit()
#     else:
#         print('ok')
#         register_(age)


if __name__ == '__main__':
    my_canal = UrTube()

    def start():
        while True:
            choice = input('Выберите нужное действие : \n1 - Вход\n2 - Регистрация\n')
            if choice == '1':
                enter_()

            if choice == '2':
                register_()
    start()







