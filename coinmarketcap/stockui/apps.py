from django.apps import AppConfig


class StockuiConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "stockui"
    def ready(*args):
        from . import schedular
        schedular.start()
