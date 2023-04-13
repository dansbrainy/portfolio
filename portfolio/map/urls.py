from django.urls import path

from portfolio.map.views import map_view

app_name = "map"
urlpatterns = [
    path("", view=map_view, name="map"),
]
