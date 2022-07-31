# Generated by Django 4.0.6 on 2022-07-19 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_userdocuments'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='status',
            field=models.CharField(blank=True, choices=[('registered', 'registered'), ('requested_to_driver', 'requested_to_driver'), ('allowed', 'allowed'), ('disallowed', 'disallowed')], default='registered', max_length=255, null=True, verbose_name='Status'),
        ),
    ]