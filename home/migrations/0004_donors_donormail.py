# Generated by Django 3.1.3 on 2020-11-13 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20201112_1332'),
    ]

    operations = [
        migrations.AddField(
            model_name='donors',
            name='donorMail',
            field=models.CharField(default='nasartarique@gmail.com', max_length=30),
        ),
    ]
