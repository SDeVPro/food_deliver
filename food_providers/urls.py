from django.urls import path, include
from . import views 
#from deliverApp.views import home
urlpatterns = [
    path('', views.index, name='index'),
] 