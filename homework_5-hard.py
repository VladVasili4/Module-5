from time import sleep

""" Общее ТЗ:
Реализовать классы для взаимодействия с платформой, каждый из которых будет содержать методы добавления видео, 
авторизации и регистрации пользователя и т.д."""


class UrTube:
    def __int__(self):
        self.users = []
        self.videos = []
        self.current_user = 'user'


    def log_in(self, login, password):   # Ищет такого юзера, и если есть, current_user меняет на него
        self.login = login
        self.password = password



    def register(self, nickname, password, age):    # Добавляет пользователя, если его нет
        self.nickname = nickname
        self.password = password
        self.age = age




    def log_out(self):     # для сброса текущего пользователя на None
        print('Извините, Вам не рекомендуется посещение данного канала')
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
    def __int__(self, age, nickname, password, password_confirm):
        self.nickname = nickname
        # if age.isdigit:
        self.age = age
        print(self.age)
        if password == password_confirm:
            self.password = password
            pass


if __name__ == '__main__':
    database = UrTube()


    while True:
        choice = input('Выберите нужное действие : \n1 - Вход\n2 - Регистрация\n')
        if choice == '1':
            log = input('Введите Ваш логин :')
            pas = input('Введите Ваш пароль :')
            print(f"Отлично, Ваш логин {log}, Ваш пароль {pas}. Проверяем...")
            input()
            # if nickname in database.users:
            #
            #     pass
        if choice == '2':
            age = input("Сколько Вам лет?  ")
            while age.isdigit():
                age = int(age)
                if age <= 18:
                    print('Извините, Вам не рекомендуется посещение данного канала')
                    exit
                else: print('ok')
            else: print('Извините, введите, пожалуйста цифрами')



            nickname = input('Введите Ваш логин :')
            password = input('Введите Ваш пароль :')
            password_confirm = input('Повторите пароль :')


