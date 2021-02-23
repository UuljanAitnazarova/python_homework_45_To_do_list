from django.db import models


class Task(models.Model):

    STATUS_CHOICES = [
        ('new', 'Новая'), 
        ('in_progress', 'В процессе'),  
        ('done', 'Сделано')
        ]

    description = models.CharField(max_length=200, null=False, blank=False, verbose_name="Описание")
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, null=False, blank=False, default=STATUS_CHOICES[0], verbose_name='статус')
    date_completed = models.DateField(blank=True, null=True, verbose_name='Дата выполнения')


    def __str__(self):
        return self.description