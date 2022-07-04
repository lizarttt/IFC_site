from django.db import models


class TourPost(models.Model): # Создание модели турниров
    title = models.CharField('Названия турнира', max_length=13)
    image = models.ImageField(upload_to='images')
    description = models.TextField('Описание турнира', max_length=200)
    geo = models.CharField('Геолокация', max_length=50)
    data = models.DateField('Дата', blank=True, null=True)
    time = models.TimeField('Время', auto_now=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Турниры'
        verbose_name_plural = 'Турнир'


class RaitingModel(models.Model): # Создание модели под таблицу рейтинга
    weight = models.CharField('Весовая категория', max_length=40)
    champion = models.CharField('Имя чемпиона', max_length=30)
    image = models.ImageField(upload_to='images')
    one_fighter = models.CharField('Первое место рейтинга', max_length=30)
    two_fighter = models.CharField('Второе место рейтинга', max_length=30)
    three_fighter = models.CharField('Третье место рейтинга', max_length=30)
    four_fighter = models.CharField('Четвертое место рейтинга', max_length=30)
    five_fighter = models.CharField('Пятое место рейтинга', max_length=30)

    def __str__(self):
        return self.weight

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинг'


class FighterModel(models.Model): # создание модели бойца для списка бойцов
    username = models.CharField('Кличка бойца', max_length=40)
    name = models.CharField('Имя и Фамилия', max_length=30)
    TYPES = (
        ('Лёгкий', 'light'),
        ('Средний', 'middle'),
        ('Полутяжёлый', 'heavywight')
    )
    type_education = models.CharField(verbose_name='Весовая', max_length=20, choices=TYPES)
    stats = models.CharField('Рекорд (В-П-Н)', max_length=10)
    image = models.ImageField(upload_to='images')
    geo = models.CharField('Место рождения', max_length=100)
    years = models.CharField('Возраст', max_length=2)
    weight = models.CharField('Вес', max_length=3)
    arms = models.CharField('Длина рук', max_length=3)
    growth = models.CharField('Рост', max_length=3)
    link = models.CharField('Ссылка на W-cloud', max_length=120)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Карточки бойцов'
        verbose_name_plural = 'Карточки бойцов'


class StatisticsModel(models.Model): # создание модели под статистиков боёв
    types_f = (
        ('warning', 'Ничья'),
        ('success', 'Победа'),
        ('secondary', 'В разработке')
    )
    type_fight = models.CharField(verbose_name='Статус боя', max_length=20, choices=types_f)
    status_fight = models.CharField('Статус - НИЧЬЯ/ В РАЗРАБОТКЕ/ ПОБЕДА P1 ИЛИ P2', max_length=25)
    name_1 = models.CharField('Имя первого бойца', max_length=30)
    name_2 = models.CharField('Имя второго бойца', max_length=30)
    result = models.CharField('Результат боя, если нет. То прочерк', max_length=8)
    TYPES = (
        ('Лёгкий', 'light'),
        ('Средний', 'middle'),
        ('Полутяжёлый', 'heavywight')
    )
    type_education = models.CharField(verbose_name='Весовая', max_length=20, choices=TYPES)
    data = models.DateField('Дата', blank=True, null=True)

    def __str__(self):
        return f'{self.name_1} vs {self.name_2}'

    class Meta:
        verbose_name = 'Статистика боёв'
        verbose_name_plural = 'Статистика боёв'









