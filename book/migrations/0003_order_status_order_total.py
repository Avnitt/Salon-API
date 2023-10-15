# Generated by Django 4.2.5 on 2023-10-14 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_alter_subservice_price_order_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('C', 'Completed'), ('X', 'Cancelled'), ('I', 'Incomplete')], default='I', max_length=1),
        ),
        migrations.AddField(
            model_name='order',
            name='total',
            field=models.CharField(default=0, max_length=10),
        ),
    ]
