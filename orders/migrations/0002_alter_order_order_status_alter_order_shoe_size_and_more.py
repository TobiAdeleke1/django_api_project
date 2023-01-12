# Generated by Django 4.1 on 2023-01-12 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.CharField(choices=[('pending', 'PENDING'), ('in_transit', 'IN_TRANSIT'), ('delivered', 'DELIVERED')], default='pending', max_length=50),
        ),
        migrations.AlterField(
            model_name='order',
            name='shoe_size',
            field=models.CharField(choices=[('3', 'first_small'), ('4', 'second_small'), ('5', 'first_medium'), ('6', 'second_medium'), ('7', 'first_large'), ('8', 'second_large')], default='3', max_length=50),
        ),
        migrations.AlterField(
            model_name='order',
            name='shoe_type',
            field=models.CharField(choices=[('flat', 'FLATS'), ('boot', 'BOOTS'), ('trainers', 'TRAINERS'), ('sandals', 'SANDLES')], default='flat', max_length=50),
        ),
    ]
