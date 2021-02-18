from django.db import models
from django.contrib.auth.models import AbstractUser



class CustomUser(AbstractUser):
    reserv = models.CharField(max_length=100, blank=True)
    reserv2 = models.BooleanField(blank=True, default=False)
    reserv3 = models.CharField(max_length=100, blank=True)
    reserv4 = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f'{self.username}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        Profile.objects.get_or_create(user=self)



class Profile(models.Model):
    user = models.OneToOneField('CustomUser', on_delete=models.CASCADE, primary_key=True)
    user_name = models.CharField(max_length=100, blank=True)
    user_lastname = models.CharField(max_length=150, blank=True)
    avatar = models.ImageField(upload_to='%Y/%m/%d', blank=True, null=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    gender = models.CharField(max_length=100, blank=True)
    birthday = models.CharField(max_length=50,blank=True)
    created = models.DateField(auto_now=True)
    reserv = models.CharField(max_length=100, blank=True)
    reserv1 = models.CharField(max_length=100, blank=True)
    reserv2 = models.CharField(max_length=100, blank=True)
    reserv3 = models.CharField(max_length=100, blank=True)
    reserv4 = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f'{self.user} profile'






