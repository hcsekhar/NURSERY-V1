# Generated by Django 4.2.5 on 2024-02-09 07:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drive', '0035_address_address_line2'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Order',
        ),
    ]
