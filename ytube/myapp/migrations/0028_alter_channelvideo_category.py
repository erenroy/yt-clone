# Generated by Django 4.1.3 on 2023-11-18 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0027_alter_channelvideo_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channelvideo',
            name='category',
            field=models.CharField(choices=[('X', 'Action'), ('AN', 'Animes'), ('K', 'Film'), ('G', 'Gaming'), ('L', 'Learing'), ('FN', 'Fashion'), ('S', 'Sports')], default='A', max_length=25),
        ),
    ]
