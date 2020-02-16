from django.urls import path, include
from . import views


urlpatterns = [
    path("calculador/<nombre>/<peso>/<estatura>",views.calculoIMC,name="reporte"),
]