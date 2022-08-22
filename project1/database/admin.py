from django.contrib import admin
from .models import номенклатура, цена, корзина, заказы,тип_сыра
# Register your models here.
admin.site.register(тип_сыра)
admin.site.register(номенклатура)
admin.site.register(цена)
admin.site.register(корзина)
admin.site.register(заказы)