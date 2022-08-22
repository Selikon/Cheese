from tabnanny import verbose
from django.db import models
from django.forms import IntegerField
from django.urls import reverse

class тип_сыра (models.Model):
    тип_сыра = models.TextField(verbose_name='Тип_сыра', null=True)
    
    def get_absolute_url(self):
        return reverse('types', kwargs= {"pk":self.pk} )

    def __str__(self):
        return self.тип_сыра
    class Meta:
        verbose_name= 'Тип_сыра '
        verbose_name_plural='Тип_сыров'

class номенклатура (models.Model):
    # id = models.IntegerField(primary_key=True)
    название = models.TextField(verbose_name='Название')  # Field name made lowercase.
    доступность_товара = models.IntegerField(verbose_name='Доступность_товара')  # Field name made lowercase.
    id_тип_сыра = models.ForeignKey (тип_сыра, on_delete=models.PROTECT,verbose_name='Тип сыра' )  # Field name made lowercase.
    коментарий = models.TextField (verbose_name='Коментарий',blank=True, null=True)

    def get_absolute_url(self):
        return reverse('cheese', kwargs= {"pk":self.pk} )

    def __str__(self):
        return self.название

    class Meta:
        verbose_name= 'Номенклатура '
        verbose_name_plural='Номенклатуры'

class цена (models.Model):
    # id = models.IntegerField(primary_key=True)
    id_номенклатура=models.ForeignKey(номенклатура,on_delete=models.PROTECT,verbose_name='id_Номенклатура')
    еденица_измерения=models.TextField(verbose_name='Еденица_измерения')
    цена_за_единицу=models.IntegerField(verbose_name='Цена за единицу' )
    
    def get_absolut_url(self):
        return reverse('')
    class Meta:
        verbose_name= 'цена '
        verbose_name_plural='цены'
        
class корзина (models.Model):
    id_покупатели=models.IntegerField(verbose_name='id_Покупатели', blank=True)
    id_номенклатура=models.ForeignKey(номенклатура, on_delete=models.PROTECT, verbose_name='id_Номенклатура')
    объем_покупки=models.IntegerField(verbose_name='Объем покупки')
    Создание=models.DateTimeField(auto_now_add=True,verbose_name='Дата_время_создания')
    Обновление=models.DateTimeField(auto_now=True, verbose_name='Дата_время_обновления')

    class Meta:
        verbose_name= 'корзина '
        verbose_name_plural='корзины'



class заказы(models.Model):
    id_покупатели=models.IntegerField(verbose_name='id_Покупатели', blank=True)
    id_номенклатура=models.ForeignKey(номенклатура, on_delete=models.PROTECT, verbose_name='id_Номенклатура')
    объем_покупки=models.IntegerField(verbose_name='Объем покупки')
    id_адрес_доставки=models.IntegerField(verbose_name='id адрес доставки', blank=True)
    Создание=models.DateTimeField(auto_now_add=True,verbose_name='Дата_время_создания')
    Обновление=models.DateTimeField(auto_now=True, verbose_name='Дата_время_обновления')
    коментарий = models.TextField (verbose_name='Коментарий',blank=True, null=True)
    доставлен=models.BooleanField(default=False, verbose_name='Состояние доставки')

    class Meta:
        verbose_name= 'заказ '
        verbose_name_plural='заказы'


    # def get_absolute_url(self):
    #     return f'/bd/{self.id}'
    
    # class Meta:
    #     verbose_name= 'Номенклатура '
    #     verbose_name_plural='Номенклатуры'
