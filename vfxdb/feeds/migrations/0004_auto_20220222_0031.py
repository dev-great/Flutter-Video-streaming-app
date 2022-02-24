# Generated by Django 3.2.12 on 2022-02-21 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0003_auto_20220222_0026'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedpost',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='documents/'),
        ),
        migrations.AlterField(
            model_name='feedpost',
            name='PostImage',
            field=models.ImageField(blank=True, null=True, upload_to='feedpost/'),
        ),
    ]