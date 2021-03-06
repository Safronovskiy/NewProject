# Generated by Django 3.1.5 on 2021-02-05 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0002_auto_20210205_1438'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wearmodel',
            name='res1',
        ),
        migrations.AddField(
            model_name='wearmodel',
            name='popular',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='wearmodel',
            name='discount',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='wearmodel',
            name='discount_image',
            field=models.ImageField(blank=True, null=True, upload_to='media/%Y/%m/%d'),
        ),
    ]
