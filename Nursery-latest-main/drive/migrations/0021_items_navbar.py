# Generated by Django 4.2.5 on 2024-01-29 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('drive', '0020_items'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='navbar',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='drive.navbar'),
        ),
    ]
