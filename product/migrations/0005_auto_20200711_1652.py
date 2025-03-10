# Generated by Django 3.0.8 on 2020-07-11 11:22

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
        ('product', '0004_auto_20200710_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_details',
            name='order_no',
            field=models.CharField(blank=True, default=uuid.uuid4, max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='order_details',
            name='total_price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order_details',
            name='user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='childer', to='myapp.UserDetails'),
        ),
    ]
