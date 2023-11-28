from django.db import models

# Create your models here.
class InfoUser(models.Model):
    image = models.ImageField(
        upload_to="image_user/",
        verbose_name="Загрузите фото"
    )
    name = models.CharField(
        max_length=100,
        verbose_name="Введите ФИО"
    )
    work = models.CharField(
        max_length=50,
        verbose_name="Введите профессию"
    )
    descriptions = models.TextField(
        verbose_name="Введите биографию"
    )

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name="Информация пользователя"
        verbose_name_plural = "Информация пользователей"

class About(models.Model):
    first_name = models.CharField(
        max_length=255,
        verbose_name="Имя"
    )
    last_name = models.CharField(
        max_length=255,
        verbose_name="Фамилия"
    )
    age = models.CharField(
        max_length=3,
        verbose_name="Возраст"
    )
    nation = models.CharField(
        max_length=255,
        verbose_name="Нация"
    )
    adress = models.CharField(
        max_length=255,
        verbose_name="Адрес"
    )
    phone = models.CharField(
        max_length=255,
        verbose_name="Телефонный номер"
    )
    email = models.EmailField(
        verbose_name="Почта"
    )
    telegram = models.CharField(
        max_length=255,
        verbose_name="Телеграм"
    )
    language = models.CharField(
        max_length=255,
        verbose_name="Знания языка"
    )
    year = models.CharField(
        max_length=255,
        verbose_name="Годы опыта"
    )
    projects = models.CharField(
        max_length=255,
        verbose_name="Завершенные проекты"
    )
    clients = models.CharField(
        max_length=255,
        verbose_name="Счастливые клиенты"
    )
    awards = models.CharField(
        max_length=255,
        verbose_name="Полученные награды"
    )

    def __str__(self) -> str:
        return f"{self.first_name} - {self.last_name}"
    
    class Meta:
        verbose_name="Обо мне"
        verbose_name_plural = "Обо мне"

class Skills(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Название"
    )
    number = models.CharField(
        max_length=255,
        verbose_name="Процент"
    )

    def __str__(self) -> str:
        return f"{self.title} - {self.number}"
    
    class Meta:
        verbose_name="Мои скилы"
        verbose_name_plural = "Мой скил"

class Contact(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Имя"
    )
    email = models.EmailField(
        verbose_name="Почта"
    )
    message = models.TextField(
        verbose_name="Сообщение"
    )

    def __str__(self) -> str:
        return f"{self.name} -- {self.email}"
    
    class Meta:
        verbose_name="Обратная связь"
        verbose_name_plural = "Обратная связь"

class Experience(models.Model):
    year = models.CharField(
        max_length=255,
        verbose_name="Год"
    )
    job = models.CharField(
        max_length=255,
        verbose_name="Работа"
    )
    place = models.CharField(
        max_length=255,
        verbose_name="Место"
    )
    description = models.TextField(
        verbose_name="Что вы делали"
    )

    def __str__(self) -> str:
        return f"{self.year} - {self.job}"
    
    class Meta:
        verbose_name="Годы опата"
        verbose_name_plural = "Год опыта"

class Education(models.Model):
    year = models.CharField(
        max_length=255,
        verbose_name="Год"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Научная степень"
    )
    place = models.CharField(
        max_length=255,
        verbose_name="Место"
    )
    description = models.TextField(
        verbose_name="Что вы делали"
    )
    def __str__(self) -> str:
        return f"{self.year} - {self.title}"
    
    class Meta:
        verbose_name="Годы обучение"
        verbose_name_plural = "Год обучение"