from unittest import mock
from rest_framework import serializers
from .models import номенклатура, цена

# class Order(ModelSerializer) :       
#     class Meta:
#         model= цена
#         fields= ['id_номенклатура','еденица_измерения','цена_за_единицу']
# class OrderSerializer(ModelSerializer) :
#     class Meta:
#         model= номенклатура
#         fields= ['id','название','доступность_товара','id_тип_сыра','коментарий']
class DBserializer(serializers.ModelSerializer):
    class Meta:
        model= номенклатура
        fields=['id','название','доступность_товара','id_тип_сыра','коментарий']

    
