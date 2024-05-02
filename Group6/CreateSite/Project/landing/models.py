from django.db import models

class Product(models.Model):
    class Meta:
        verbose_name = 'Букет'
        verbose_name_plural = 'Букеты'
        
    title = models.CharField(max_length=30, unique=True, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    img = models.CharField(max_length=100, verbose_name='Путь к изображению')
    old_price = models.IntegerField(null=True, verbose_name='Старая цена')
    price = models.IntegerField(verbose_name='Новая цена')

    def __str__(self):
        return self.title

class Consumer(models.Model):
    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
    
    name = models.CharField(max_length=30, verbose_name='Имя')
    phone = models.CharField(max_length=12, verbose_name='Телефон')
    comment = models.TextField(blank=True, null=True, verbose_name='Комментарий')
    is_agree = models.BooleanField(default=False, verbose_name='Согласие')

    def __str__(self):
        phone_number_formatted = f'8-{self.phone[0:3]}-{self.phone[3:6]}-{self.phone[6:8]}-{self.phone[8:10]}'
        return self.name+' '+phone_number_formatted