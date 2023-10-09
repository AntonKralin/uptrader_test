from django.db import models


# Create your models here.
class Menu(models.Model):
    """main menu object"""
    title = models.CharField(max_length=100,
                             unique=True, verbose_name='Название меню')
    link = models.CharField(max_length=255, verbose_name='Ссылка на меню')

    def __str__(self):
        return self.title


class MenuItem(models.Model):
    """item of menu object"""
    title = models.CharField(max_length=100, verbose_name='Название')
    link = models.CharField(max_length=255, verbose_name='Ссылка')
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE,
                             verbose_name='Пункт меню')
    parent = models.ForeignKey('self', on_delete=models.CASCADE,
                               blank=True, null=True,
                               verbose_name='Родительский пункт меню')

    def __str__(self):
        return self.title
