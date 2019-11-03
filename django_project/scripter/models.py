from django.db import models

# Create your models here.
class script_data(models.Model):
    script_name = models.CharField(max_length = 30)
    dialogue_number = models.IntegerField()
    gender = models.CharField(max_length = 10)
    character_name = models.CharField(max_length = 30)
    dialogue = models.TextField()
    