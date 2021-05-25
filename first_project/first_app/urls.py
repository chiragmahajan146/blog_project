from django.urls import path,include
from first_app import views

urlpatterns=[
    path('', views.index, name='index'),
    path('index1/', views.index1, name='index1'),

]