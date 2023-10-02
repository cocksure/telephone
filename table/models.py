from django.db import models
from django.contrib.auth.models import User


class Department(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Bo'lim"
        verbose_name_plural = "Bo'limlar"

    def __str__(self):
        return self.name


class MyTable(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    col1 = models.CharField(max_length=255, blank=True)
    col2 = models.CharField(max_length=255, blank=True)
    col3 = models.CharField(max_length=255, blank=True)
    col4 = models.CharField(max_length=255, blank=True)
    col5 = models.CharField(max_length=255, blank=True)
    col6 = models.CharField(max_length=255, blank=True)
    col7 = models.CharField(max_length=255, blank=True)
    col8 = models.CharField(max_length=255, blank=True)
    col9 = models.CharField(max_length=255, blank=True)
    col10 = models.CharField(max_length=255, blank=True)

    class Meta:
        verbose_name = 'Jadval'
        verbose_name_plural = 'Jadvallar'

    def __str__(self):
        return f"Row: {self.pk}"
