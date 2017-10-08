from django.db import models


class Call(models.Model):
    name = models.CharField(max_length=30, verbose_name='Имя')
    phone = models.CharField(max_length=30, verbose_name='Телефон')
    message = models.TextField(verbose_name='Название')
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.phone

    class Meta:
        verbose_name = 'Call'
        verbose_name_plural = 'Call'
