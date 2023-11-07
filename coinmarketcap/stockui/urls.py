from django.urls import path
from . import views
from . import schedular

urlpatterns = [

    path("", views.web_scraping, name="web_scraping"),
    path("fetch_coin_data/", views.fetch_coin_data, name="fetch_coin_data"),
    path("put_coin_data/", views.put_coin_data, name="put_coin_data"),

]