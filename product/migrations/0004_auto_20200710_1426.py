# Generated by Django 3.0.8 on 2020-07-10 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20200709_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_details',
            name='added_on',
            field=models.DateField(blank=True),
        ),
    ]
