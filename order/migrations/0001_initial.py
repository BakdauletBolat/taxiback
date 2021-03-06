# Generated by Django 4.0.6 on 2022-07-18 11:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('regions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TypeOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_address', models.CharField(blank=True, max_length=255, null=True)),
                ('to_address', models.CharField(blank=True, max_length=255, null=True)),
                ('price', models.IntegerField()),
                ('comment', models.TextField()),
                ('date_time', models.DateTimeField()),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('from_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders_from', to='regions.city')),
                ('to_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders_to', to='regions.city')),
                ('type_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.typeorder')),
            ],
        ),
    ]
