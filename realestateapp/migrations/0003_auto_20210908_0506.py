# Generated by Django 3.1.1 on 2021-09-08 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realestateapp', '0002_auto_20210908_0334'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='offer_type',
            field=models.CharField(choices=[('rent', 'rent'), ('sale', 'sale'), ('', 'choose offer_type')], default='', max_length=15),
        ),
        migrations.AlterField(
            model_name='property',
            name='prop_img1',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/', verbose_name='property Image 1'),
        ),
        migrations.AlterField(
            model_name='property',
            name='prop_img2',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/', verbose_name='property Image 2'),
        ),
        migrations.AlterField(
            model_name='property',
            name='prop_img3',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/', verbose_name='property Image 3'),
        ),
    ]