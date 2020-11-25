from django.urls import path, include
from . import views
from food_area.views import food_area_name
#from deliverApp.views import home
urlpatterns = [
    path('food-area-name/', food_area_name, name='food_area_name'),
]