# Generated by Django 4.0.6 on 2022-07-18 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='status',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
