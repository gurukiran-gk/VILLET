# Generated by Django 4.1.10 on 2023-09-06 15:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Villet1', '0010_activecreditcard_bill_paid'),
    ]

    operations = [
        migrations.AddField(
            model_name='activecreditcard',
            name='new_bill_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
