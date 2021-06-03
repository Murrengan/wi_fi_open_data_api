from django.db import models


class WiFiSpot(models.Model):
    external_id = models.IntegerField()
    name = models.CharField(max_length=100)
    adm_aria = models.CharField(max_length=100, blank=True, null=True)
    district = models.CharField(max_length=50, blank=True, null=True)
    park_name = models.CharField(max_length=200, blank=True, null=True)
    wi_fi_name = models.CharField(max_length=50, blank=True, null=True)
    coverage_area = models.IntegerField(blank=True, null=True)
    function_flag = models.CharField(max_length=50, blank=True, null=True)
    access_flag = models.CharField(max_length=50, blank=True, null=True)
    longitude_WGS84 = models.FloatField(blank=True, null=True)
    latitude_WGS84 = models.FloatField(blank=True, null=True)

    class Meta:
        verbose_name = 'Точка доступа Wi-fi'
        verbose_name_plural = 'Точки доступа Wi-fi'

    def __str__(self):
        return self.name
