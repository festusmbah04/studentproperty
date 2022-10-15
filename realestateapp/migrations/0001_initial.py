# Generated by Django 3.1.1 on 2021-09-06 14:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='propertyType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property_type_name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property_name', models.CharField(max_length=200)),
                ('slug', models.SlugField(unique=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('prop_img1', models.ImageField(blank=True, null=True, upload_to='uploads/')),
                ('prop_img2', models.ImageField(blank=True, null=True, upload_to='uploads/')),
                ('prop_img3', models.ImageField(blank=True, null=True, upload_to='uploads/')),
                ('description', models.TextField()),
                ('address', models.TextField()),
                ('numbers', models.PositiveBigIntegerField()),
                ('Location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='realestateapp.location')),
                ('property_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='realestateapp.propertytype')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ContactAgent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('property_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='realestateapp.property')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]