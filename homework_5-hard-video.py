
from time import sleep

""" Общее ТЗ:
Реализовать классы для взаимодействия с платформой, каждый из которых будет содержать методы добавления видео, 
авторизации и регистрации пользователя и т.д."""

class UrTube:
    users = []
    videos = []
    current_user = []
    def __init__(self):
        pass

    def add(self, *video):
        """ принимает неограниченное кол-во объектов класса Video и все добавляет в videos,
            если с таким же названием видео ещё не существует. В противном случае ничего не происходит. """
        print('В add передано', video)
        input('stop2')








        # if not any(v.title == i.tittle for v in self.videos:
        #     self.videos.append(i)
        # # self.flm = video

        # if len(UrTube.videos) > 0:
        #     for i in range(0, len(UrTube.videos)):
        #         self.flm = UrTube.videos[i]
        #         if self.title == self.flm[0]:
        #             input('Есть фильм, что дальше?')
        #         else:
        #             UrTube.videos.append(self.flm)


        print(UrTube.videos)
        input('pause1')
        # self.film = [self.title, self.duration, self.time_now, self.adult_mode ]
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
    def __init__(self, title, duration, adult_mode = False):
        self.title = title                                # заголовок, строка
        self.duration = duration                           # продолжительность, секунды
        self.time_now = 0                            # секунда остановки, изначально 0
        self.adult_mode = adult_mode
        self.v = [self.title, self.duration, self.time_now, self.adult_mode]
        print(f'Создали фильм c названием {self.title}, длительность которого  {self.duration}')
        print(f'Объект класса Video: {self.v}')
        UrTube.add(title, duration, adult_mode)

v = Video('Лучший язык программирования 2024 года', 200)

if __name__ == '__main__':
    my_canal = UrTube()
