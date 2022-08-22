from django.contrib import admin
from django.urls import path

from.import views
urlpatterns = [
    path('', views.input_date, name='home'),
    path('<int:pk>', views.get_type, name='types' ),
    path('cheese/<int:pk>',views.obj_cheese, name='cheese'),
    path('api/dblist',views.DatabaseView.as_view())
]


#views.date_id(), name='spisok-deteils'