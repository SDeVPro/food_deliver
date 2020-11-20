from django.db import models
from food_area.models import *

# Create your models here.

class CookInfo(models.Model):
    cook_name = models.CharField(max_length=255,blank=False)
    cook_image = models.ImageField(blank=False, upload_to='images')
    contact_no = models.PositiveIntegerField(blank=False)
    area = models.ForeignKey(Area, blank=False, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Cook Infos'

    def __str__(self):
        return self.cook_name