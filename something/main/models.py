from django.db import models


class Contacts(models.Model):
    email = models.EmailField(verbose_name='email', unique=True)
    name = models.CharField(verbose_name='имя', max_length=50)
    phone_number = models.CharField(verbose_name='Номер телефона', max_length=30)
    object_name = models.CharField(verbose_name='Наименование объекта', max_length=50)
    date = models.DateField(verbose_name='Дата')
    created = models.DateTimeField(verbose_name='Cоздана', auto_now_add=True)

    def __str__(self):
        return 'Форма'

    class Meta:
        ordering = ['-created']
        verbose_name = 'Контактная форма'
        verbose_name_plural = "Контактные формы"