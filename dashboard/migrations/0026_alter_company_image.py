# Generated by Django 3.2.7 on 2022-01-10 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0025_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='company'),
        ),
    ]