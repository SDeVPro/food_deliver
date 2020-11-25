from django.shortcuts import render
from food_delivery.models import DeliveryPoint
# Create your views here.

def delivery_point(request):
    delivery_point_info = DeliveryPoint.objects.all()
    template = 'food_delivery/delivery_point.html'
    context = {'delivery_point_info':delivery_point_info}
    return render(request, template, context)