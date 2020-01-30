#from django.db import models

class uploadImage(models.Model):
    pic = models.ImageField(upload_to='images/')