# Generated by Django 4.1.3 on 2023-11-18 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0023_channelvideo_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='channelvideo',
            name='category',
            field=models.CharField(choices=[('A', 'Action'), ('AN', 'Animes'), ('K', 'Film'), ('G', 'Gaming'), ('L', 'Learing'), ('F', 'Fashion'), ('S', 'Sports')], default='All', max_length=25),
        ),
    ]
