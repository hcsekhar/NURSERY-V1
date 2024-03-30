# Generated by Django 4.2.5 on 2024-01-29 12:35

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drive', '0018_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dropdown',
            name='drop_slug',
            field=autoslug.fields.AutoSlugField(always_update=True, editable=False, populate_from='title'),
        ),
        migrations.AlterField(
            model_name='navbar',
            name='nav_slug',
            field=autoslug.fields.AutoSlugField(always_update=True, editable=False, populate_from='title'),
        ),
        migrations.AlterField(
            model_name='navitem',
            name='item_slug',
            field=autoslug.fields.AutoSlugField(always_update=True, editable=False, populate_from='title'),
        ),
        migrations.AlterModelTable(
            name='dropdown',
            table='Dropdown',
        ),
        migrations.AlterModelTable(
            name='navbar',
            table='Navbar',
        ),
        migrations.AlterModelTable(
            name='navitem',
            table='NavItem',
        ),
    ]
