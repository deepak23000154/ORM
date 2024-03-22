from django.db import models
from django.contrib import admin
class Train(models.Model):
    train_code=models.IntegerField()
    train_name=models.CharField(max_length=20,primary_key=True)
    distance=models.IntegerField()
    starting_time=models.IntegerField()
    ending_time=models.IntegerField()
    start_station_code=models.IntegerField()
    end_station_code=models.IntegerField()
    frequency=models.IntegerField()
class TrainAdmin(admin.ModelAdmin):
    list_display=('train_code','train_name','distance','starting_time','ending_time','start_station_code','end_station_code','frequency')