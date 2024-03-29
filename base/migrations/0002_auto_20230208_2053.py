# Generated by Django 3.2.15 on 2023-02-08 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='main',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('train_no', models.IntegerField(db_column='train_no')),
                ('station_code', models.CharField(db_column='station_code', max_length=4)),
                ('delay', models.IntegerField(db_column='delay')),
                ('date_epoch', models.IntegerField(db_column='date_epoch')),
                ('start_from_source_epoch', models.IntegerField(db_column='start_from_source_epoch')),
            ],
            options={
                'db_table': 'main',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='station_mapping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('station_code', models.CharField(db_column='station_code', max_length=200)),
                ('station_name', models.CharField(db_column='station_name', max_length=200)),
            ],
            options={
                'db_table': 'station_mapping',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='main_CR',
        ),
    ]
