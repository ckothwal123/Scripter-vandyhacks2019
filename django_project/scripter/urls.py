from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('submitdata/', views.submitdata, name='submitdata'),
    # path('viewscript/', views.getdata, name='getdata'),
    
]