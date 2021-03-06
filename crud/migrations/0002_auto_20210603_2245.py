# Generated by Django 3.2.4 on 2021-06-03 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wifispot',
            name='access_flag',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='wifispot',
            name='adm_aria',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='wifispot',
            name='coverage_area',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='wifispot',
            name='district',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='wifispot',
            name='function_flag',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='wifispot',
            name='latitude_WGS84',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='wifispot',
            name='longitude_WGS84',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='wifispot',
            name='park_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='wifispot',
            name='wi_fi_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
