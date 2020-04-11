from django.urls import path, register_converter
from .views import HexColorConverter, PlaceHolderView


register_converter(HexColorConverter, "color")


urlpatterns = [
    path("", PlaceHolderView.as_view()),
    path("<color:bg>/", PlaceHolderView.as_view()),
    path("<color:bg>/<color:fnt>/", PlaceHolderView.as_view()),
]
