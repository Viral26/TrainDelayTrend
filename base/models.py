from django.db import models

# Create your models here.
class main(models.Model):
    train_no = models.CharField(db_column='train_no',max_length=200)
    date = models.CharField(db_column='date',max_length=200)
    delay = models.CharField(db_column='delay',max_length=200)
    station_code = models.CharField(db_column='station_code',max_length=200)
    start_from_source = models.CharField(db_column='start_from_source',max_length=200)
    
    class Meta:
        managed = False
        db_table = 'main'

class station_mapping(models.Model):
    station_code = models.CharField(db_column='station_code',max_length=200)
    station_name = models.CharField(db_column='station_name',max_length=200)

    class Meta:
        managed = False
        db_table = 'station_mapping'


# class Train_no(models.Model):
#     number = models.CharField(db_column="train_no",max_length=200)

#     class Meta:
#         db_table = 'main'



# class Station(models.Model):
#     name = models.CharField(db_column='station_code',max_length=200)

#     class Meta:
#         db_table = 'main'