from django.db import models

# Create your models here.


class User (models.Model):
    first_name = models.CharField(max_length=20, blank=False)
    last_name = models.CharField(max_length=20, blank=True)
    password = models.CharField(max_length=40, blank=False)
    email_id = models.EmailField(max_length=40, blank=False, unique=True)
    age = models.IntegerField(default=None, blank=False)
    gender = models.CharField(max_length=10, blank=False)
    phone_num = models.CharField(max_length=10, blank=True)
    picture = models.ImageField(upload_to='static/profile_images', blank=True, null=True)
    date = models.DateTimeField(blank=True)

    def __unicode__(self):
        return self.first_name