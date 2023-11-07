from django.db import models

class Coinstock(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    _1h_percent = models.CharField(max_length=100)
    _24h_percent =models.CharField(max_length=100)
    _7d_percent = models.CharField(max_length=100, default="NULL")
    market_cap = models.CharField(max_length=100)
    volume_24h = models.CharField(max_length=100)
    circulating_supply = models.CharField(max_length=100)

