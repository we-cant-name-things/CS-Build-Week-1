# Generated by Django 3.0.2 on 2020-01-07 22:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('location', models.CharField(max_length=30)),
                ('food_available', models.IntegerField()),
                ('water_available', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('food', models.IntegerField()),
                ('water', models.IntegerField()),
                ('current_place', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='canada_adv.Place')),
            ],
        ),
    ]
