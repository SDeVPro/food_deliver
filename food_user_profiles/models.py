from django.db import models
from django.contrib.auth.models import User
from food_area.models import Area
# Create your models here.

class Profile(models.Model):
    ROLE_CHOICE = (
        ('Cook', 'COOK'),
        ('Client', 'CLIENT'),
        ('Delivery', 'DELIVERY'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    user_name = models.CharField(blank=False,max_length=150)
    role = models.CharField(max_length=25, choices=ROLE_CHOICE, blank=False)
    profile_image = models.ImageField(upload_to='images', blank=False)
    contact_no = models.PositiveIntegerField()
    email = models.EmailField(blank=True)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username