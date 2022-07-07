from django.db import models


class Employee(models.Model):
    fullname = models.CharField(max_length=255, verbose_name='Полное имя')
    post = models.CharField(max_length=50, verbose_name='Должность')
    hiring_date = models.DateField(verbose_name='Дата приема на работу')
    salary = models.IntegerField(verbose_name='Зарплата')
    boss = models.ForeignKey('Boss', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.fullname} - {self.post}'

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'


class Boss(models.Model):
    fullname = models.CharField(max_length=255, verbose_name='Полное имя')
    hiring_date = models.DateField(verbose_name='Дата приема на работу')
    salary = models.IntegerField(verbose_name='Зарплата')

    def __str__(self):
        return f'{self.fullname} - Boss'

    class Meta:
        verbose_name = 'Начальник'
        verbose_name_plural = 'Начальники'
