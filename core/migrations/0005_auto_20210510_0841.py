# Generated by Django 3.1.7 on 2021-05-10 06:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_item_discount_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='Discount_price',
            new_name='discount_price',
        ),
    ]
