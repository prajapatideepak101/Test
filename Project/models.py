from django.db import models
from django.utils import timezone
from account.models import CustomUser
# Create your models here.
class Projects(models.Model):
    title = models.CharField(max_length=255)
    about = models.CharField(max_length=255)
    date = models.DateField(default=timezone.now)
    user = models.ManyToManyField(CustomUser, related_name='users')
    def __str__(self):
        return self.title
