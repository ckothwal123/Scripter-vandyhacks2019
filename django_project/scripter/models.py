from django.db import models

# Create your models here.
class script_data(models.Model):
    script_name = models.CharField(max_length = 30)
    dialogue_number = models.IntegerField()
    gender = models.CharField(max_length = 10)
    character_name = models.CharField(max_length = 30)
    dialogue = models.TextField()

class characters(models.Model):
    num_of_characters = models.IntegerField()
    Character_1 = models.CharField(max_length = 30)
    gender_1 =  models.CharField(max_length = 30)
    Character_2 = models.CharField(max_length = 30)
    gender_2 =  models.CharField(max_length = 30)
    Character_3 = models.CharField(max_length = 30)
    gender_3 =  models.CharField(max_length = 30)
    Character_4 = models.CharField(max_length = 30)
    gender_4 =  models.CharField(max_length = 30)
    Character_5 = models.CharField(max_length = 30)
    gender_5 =  models.CharField(max_length = 30)
    