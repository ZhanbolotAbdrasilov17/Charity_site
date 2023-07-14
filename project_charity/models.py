from django.db import models
from ckeditor.fields import RichTextField

class Props(models.Model):
    mbank = RichTextField()


class Gallery(models.Model):
    image1 = models.ImageField(upload_to='desc_image', blank=True, null=True, verbose_name='Картинка gallery')



    class Meta:
        verbose_name_plural = 'Gallery'
        verbose_name = 'Gallery'