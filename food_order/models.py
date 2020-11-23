from django.db import models
from food_area.models import *
from food_providers.models import *
from food_user_profiles.models import *
from food_items.models import *
from food_delivery.models import *

# Create your models here.

class Client(models.Model):
    client_name = models.CharField(max_length=100)
    role = models.ForeignKey(Profile, blank=False,on_delete=models.CASCADE)
    client_image = models.ImageField(blank=False,upload_to='images')
    client_contact_no = models.PositiveIntegerField(blank=False)
    area = models.ForeignKey(Area, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.client_name

class Order(models.Model):
    client_info = models.ForeignKey(Profile, on_delete=models.CASCADE)
    food_name = models.ForeignKey(FoodItems, on_delete=models.CASCADE, blank=False)
    provider = models.ForeignKey(CookInfo, on_delete=models.CASCADE, blank=False)
    quantity = models.PositiveSmallIntegerField(blank=False)
    delivery_point = models.ForeignKey(DeliveryPoint, on_delete=models.CASCADE, blank=False)
    area = models.ForeignKey(Area, on_delete=models.CASCADE, blank=False)

    def __str__(self):
        return str(self.food_name)