from django.urls import path, register_converter
from .views import HexColorConverter, PlaceHolderView


register_converter(HexColorConverter, "color")


urlpatterns = [
    path("<color:bg>/<color:fnt>/", PlaceHolderView.as_view(), name="placeholder")
]
