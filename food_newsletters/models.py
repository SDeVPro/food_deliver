from django.db import models

# Create your models here.
class NewsLetterUsers(models.Model):
    email = models.EmailField(unique=True)

    class Meta:
        ordering = ['-id']
        verbose_name_plural = 'NewsLetter Users'

    def __str__(self):
        return self.email
