# Generated by Django 4.1.10 on 2023-08-03 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Villet1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='villetuser',
            name='aadhar',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='villetuser',
            name='anninc',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='villetuser',
            name='c_b_name',
            field=models.CharField(default=0, max_length=328),
        ),
        migrations.AddField(
            model_name='villetuser',
            name='city',
            field=models.CharField(default=0, max_length=328),
        ),
        migrations.AddField(
            model_name='villetuser',
            name='designation',
            field=models.CharField(default=0, max_length=28),
        ),
        migrations.AddField(
            model_name='villetuser',
            name='dob',
            field=models.CharField(default='01/01/2000', max_length=20),
        ),
        migrations.AddField(
            model_name='villetuser',
            name='exc_cre',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='villetuser',
            name='gender',
            field=models.CharField(default=0, max_length=128),
        ),
        migrations.AddField(
            model_name='villetuser',
            name='no_of_yemp',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='villetuser',
            name='occn',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='villetuser',
            name='pan',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='villetuser',
            name='perm_adr',
            field=models.CharField(default=0, max_length=328),
        ),
        migrations.AddField(
            model_name='villetuser',
            name='state',
            field=models.CharField(default=0, max_length=328),
        ),
        migrations.AddField(
            model_name='villetuser',
            name='temp_adr',
            field=models.CharField(default=0, max_length=328),
        ),
    ]
