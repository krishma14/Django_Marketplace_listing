# Generated by Django 5.0 on 2024-01-31 06:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ShopSkate', '0003_rename_state_shippingaddress_country_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='country',
            new_name='state',
        ),
    ]
