# Generated by Django 3.2.7 on 2022-03-04 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0036_auto_20220304_2233'),
    ]

    operations = [
        migrations.AddField(
            model_name='vertical',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='vertical',
            name='title',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
    ]