# Generated by Django 3.2.7 on 2022-01-25 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0031_auto_20220119_1827'),
    ]

    operations = [
        migrations.AddField(
            model_name='index',
            name='skillset_1_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='index',
            name='skillset_1_heading',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='index',
            name='skillset_2_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='index',
            name='skillset_2_heading',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='index',
            name='skillset_3_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='index',
            name='skillset_3_heading',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='index',
            name='skillset_4_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='index',
            name='skillset_4_heading',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='index',
            name='skillset_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='index',
            name='skillset_heading',
            field=models.TextField(blank=True, null=True),
        ),
    ]