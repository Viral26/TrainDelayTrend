from django.db import models

# Create your models here.
class main(models.Model):
    train_no = models.IntegerField(db_column='train_no')
    station_code = models.CharField(db_column='station_code',max_length=4)
    delay = models.IntegerField(db_column='delay')
    date_epoch = models.IntegerField(db_column='date_epoch')
    start_from_source_epoch = models.IntegerField(db_column='start_from_source_epoch')
    
    class Meta:
        managed = False
        db_table = 'main'

# class train_info(models.Model):
#     train_no = models.IntegerField(db_column='train_no')
#     station_code = models.CharField(db_column='station_code',max_length=4)
#     delay = models.IntegerField(db_column='delay')
#     date_epoch = models.CharField(db_column='date_epoch')
#     start_from_source_epoch = models.CharField(db_column='start_from_source_epoch')
    
#     class Meta:
#         managed = False
#         db_table = 'main'

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