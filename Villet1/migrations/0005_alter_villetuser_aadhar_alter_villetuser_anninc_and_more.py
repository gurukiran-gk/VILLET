# Generated by Django 4.1.10 on 2023-08-10 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Villet1', '0004_alter_villetuser_pan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='villetuser',
            name='aadhar',
            field=models.CharField(default=0, max_length=98),
        ),
        migrations.AlterField(
            model_name='villetuser',
            name='anninc',
            field=models.CharField(default=0, max_length=98),
        ),
        migrations.AlterField(
            model_name='villetuser',
            name='c_b_name',
            field=models.CharField(default=0, max_length=98),
        ),
        migrations.AlterField(
            model_name='villetuser',
            name='city',
            field=models.CharField(default=0, max_length=128),
        ),
        migrations.AlterField(
            model_name='villetuser',
            name='designation',
            field=models.CharField(default=0, max_length=98),
        ),
        migrations.AlterField(
            model_name='villetuser',
            name='exc_cre',
            field=models.CharField(default=0, max_length=98),
        ),
        migrations.AlterField(
            model_name='villetuser',
            name='no_of_yemp',
            field=models.CharField(default=0, max_length=98),
        ),
        migrations.AlterField(
            model_name='villetuser',
            name='occn',
            field=models.CharField(default=0, max_length=98),
        ),
        migrations.AlterField(
            model_name='villetuser',
            name='pan',
            field=models.CharField(default=0, max_length=98),
        ),
        migrations.AlterField(
            model_name='villetuser',
            name='state',
            field=models.CharField(default=0, max_length=128),
        ),
    ]