from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from food_area.models import *
from food_providers.models import *
from food_delivery.models import *

# Create your models here.

class FoodCategory(models.Model):
    category_name = models.CharField(max_length=150)
    class Meta:
        verbose_name_plural = 'Food Categories'
    def __str__(self):
        return self.category_name
class FoodItems(models.Model):
    ITEM_STATUS = (
        ('mavjud','mavjud'),
        ('sotilgan','sotilgan'),
        ('mavjud emas', 'mavjud emas'),
    )
    name = models.CharField(max_length=100, blank=False)
    food_image = models.ImageField(blank=False, upload_to='images')
    category = models.ForeignKey(FoodCategory, blank=False, on_delete=models.CASCADE)
    price = models.PositiveIntegerField(blank=False)
    area = models.ForeignKey(Area,on_delete=models.CASCADE)
    provider = models.ForeignKey(CookInfo, on_delete=models.CASCADE)
    delivery_point = models.ForeignKey(DeliveryPoint, on_delete=models.CASCADE)
    minimum_quantity = models.PositiveSmallIntegerField(default=1, blank=False)
    posted_at = models.DateTimeField(auto_now=False, auto_now_add=True, blank=False)
    slug = models.SlugField(null=True)
    status = models.CharField(max_length=20, choices=ITEM_STATUS, default='mavjud')
    draft = models.BooleanField(default=False)

    class Meta:
        ordering = ['-id']
        verbose_name_plural = 'Food Items'
    def __str__(self):
        return self.name
