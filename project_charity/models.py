from django.db import models
from ckeditor.fields import RichTextField


class SocialMedia(models.Model):
    instagram = models.CharField(max_length=200, verbose_name='Инстаграм')
    whatsapp = models.CharField(max_length=200, verbose_name='Ватсап')
    facebook = models.CharField(max_length=200, verbose_name='Фейсбук')
    vk = models.CharField(max_length=200, verbose_name='Вконтакте', blank=True, null=True)
    twitter = models.CharField(max_length=200, verbose_name='Твиттер', blank=True, null=True)


    def __str__(self):
        return 'Социальные сети'

    class Meta:
        verbose_name_plural = 'Социальные сети'
        verbose_name = 'Социальная сеть'


class Props(models.Model):
    mbank = RichTextField()



    class Meta:
        verbose_name_plural = 'Gallery'
        verbose_name = 'Gallery'


class Partner(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название партнёра')
    image = models.ImageField(upload_to='partner-image', blank=True, null=True, verbose_name='Логотип партнера')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Партнёры'
        verbose_name = 'Партнёр'


class HelpCase(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название случая')
    description_title = models.TextField()
    image_title = models.ImageField(upload_to='help_cases/', blank=True, null=True)
    image_slider_1 = models.ImageField(upload_to='help_cases/', blank=True, null=True)
    image_slider_2 = models.ImageField(upload_to='help_cases/', blank=True, null=True)
    description_full = models.TextField()
    address = models.CharField(max_length=200, verbose_name='Адрес', blank=True, null=True)
    contact = models.CharField(max_length=200, verbose_name='Контактный номер', blank=True, null=True)
    requisites = models.CharField(max_length=200, verbose_name='Реквизиты', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Случаи помощи'
        verbose_name = 'Случай помощи'


class About_page_text(models.Model):
    text = RichTextField()
    image = models.ImageField(upload_to='help_cases/', blank=True, null=True)

    def __str__(self):
        return 'Текст'
    class Meta:
        verbose_name_plural = 'Текст в самой странице о нас'
        verbose_name = 'Текст в самой странице о нас'


class About_us_mainpaig(models.Model):
    text = RichTextField()

    def __str__(self):
        return 'Текст'
    class Meta:
        verbose_name_plural = 'Текст внизу главной страницы'
        verbose_name = 'Текст внизу главной страницы'


class Gallery_1(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название картинки')
    image = models.ImageField(upload_to='help_cases/', blank=True, null=True)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = 'Картинки галлереи 1'
        verbose_name = 'Картинки галлереи 1'


class Gallery_2(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название картинки')
    image = models.ImageField(upload_to='help_cases/', blank=True, null=True)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = 'Картинки галлереи 2'
        verbose_name = 'Картинки галлереи 2'


class Gallery_3(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название картинки')
    image = models.ImageField(upload_to='help_cases/', blank=True, null=True)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = 'Картинки галлереи 3'
        verbose_name = 'Картинки галлереи 3'


class Gallery_4(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название картинки')
    image = models.ImageField(upload_to='help_cases/', blank=True, null=True)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = 'Картинки галлереи 4'
        verbose_name = 'Картинки галлереи 4'


class Gallery_5(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название картинки')
    image = models.ImageField(upload_to='help_cases/', blank=True, null=True)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = 'Картинки галлереи 5'
        verbose_name = 'Картинки галлереи 5'


class Gallery_6(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название картинки')
    image = models.ImageField(upload_to='help_cases/', blank=True, null=True)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = 'Картинки галлереи 6'
        verbose_name = 'Картинки галлереи 6'


class Gallery_7(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название картинки')
    image = models.ImageField(upload_to='help_cases/', blank=True, null=True)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = 'Картинки галлереи 7'
        verbose_name = 'Картинки галлереи 7'


class Gallery_8(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название картинки')
    image = models.ImageField(upload_to='help_cases/', blank=True, null=True)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = 'Картинки галлереи 8'
        verbose_name = 'Картинки галлереи 8'


class Gallery_9(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название картинки')
    image = models.ImageField(upload_to='help_cases/', blank=True, null=True)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = 'Картинки галлереи 9'
        verbose_name = 'Картинки галлереи 9'


class Gallery_10(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название картинки')
    image = models.ImageField(upload_to='help_cases/', blank=True, null=True)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = 'Картинки галлереи 10'
        verbose_name = 'Картинки галлереи 10'


class Gallery_11(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название картинки')
    image = models.ImageField(upload_to='help_cases/', blank=True, null=True)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = 'Картинки галлереи 11'
        verbose_name = 'Картинки галлереи 11'


class Gallery_12(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название картинки')
    image = models.ImageField(upload_to='help_cases/', blank=True, null=True)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = 'Картинки галлереи 12'
        verbose_name = 'Картинки галлереи 12'

class Email(models.Model):
    full_name = models.CharField(max_length=200, verbose_name='ФИО')
    address = models.CharField(max_length=200, verbose_name='Почта клиентов')
    text = models.TextField(verbose_name='Текст')


    class Meta:
        verbose_name_plural = 'Почтовые адреса'
        verbose_name = 'Почтовые адреса'