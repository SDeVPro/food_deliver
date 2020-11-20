from django.db import models
from food_area.models import Area
# Create your models here.

class DeliveryPoint(models.Model):
    delivery_point_name = models.CharField(max_length=255, blank=False)
    delivery_point_image = models.ImageField(blank=False, upload_to='images')
    delivery_point_contact_no = models.PositiveIntegerField(blank=False)
    delivery_point_address = models.CharField(max_length=255,blank=False)
    area = models.ForeignKey(Area, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.delivery_point_name