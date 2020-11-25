from django.urls import path, include
from food_delivery.views import delivery_point
#from deliverApp.views import home
urlpatterns = [
    path('delivery-point/',delivery_point, name='delivery_point'),
] 