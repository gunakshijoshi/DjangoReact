from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path("stockui/", include("stockui.urls")),
    # path("admin/", admin.site.urls)

]
