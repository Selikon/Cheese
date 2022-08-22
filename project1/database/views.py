
from django.shortcuts import render, get_object_or_404
from .models import номенклатура,цена,тип_сыра

from database.serializers import DBserializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from django.forms import model_to_dict

class DatabaseView(APIView):
    def get(self, request):
        lst=номенклатура.objects.all().values()
        return Response({'chese':list(lst)})

    def post(self, request):
        post= номенклатура.objects.create(
            название = request.data['название'],
            доступность_товара = request.data['доступность_товара'],
            id_тип_сыра_id = request.data['id_тип_сыра']
        )

        return Response({'post':model_to_dict})

# class DatabaseView(generics.ListAPIView):
#     queryset= номенклатура.objects.all()
#     serializer_class= DBserializer



# from rest_framework import viewsets

# from database.serializers import OrderSerializer,Order


# class OrderView(viewsets.ModelViewSet):
#     def list(self, request):
#         queryset=номенклатура.objects.all()
#         serializer=OrderSerializer(queryset, many=True)
#         return response(serializer.data)
    
#     # def tsena(self, request):
#     #     dbset=цена.objects.all()
#     #     serializer=Order
#     #     return response(serializer.data)




def input_date(request):
    news=номенклатура.objects.all()
    type= тип_сыра.objects.all()
    return render(request,'database/input_date.html', {'news': news,'type':type})

def get_type(request, pk):
    news=номенклатура.objects.filter(id_тип_сыра=pk)
    type= тип_сыра.objects.all()
    typ=тип_сыра.objects.get(id=pk)
    return render(request,'database/type.html', {'news': news,'type':type,'typ':typ})

def obj_cheese(request,pk ):
    cheese=get_object_or_404(номенклатура,pk=pk)
    #cheese=номенклатура.objects.get(pk=pk)
    type= тип_сыра.objects.all()
    return render(request, 'database/obj_cheese.html', {'cheese':cheese,'type':type}) 

# Create your views here.
# def date_id(request, номенклатура_id):
#     pass


