# Generated by Django 4.2.3 on 2023-11-16 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_alter_channelvideo_channelimages_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='channelvideo',
            name='smallimage',
            field=models.ImageField(default=5, upload_to='smallchannelimage'),
            preserve_default=False,
        ),
    ]
