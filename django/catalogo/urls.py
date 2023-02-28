from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name = 'index'),
    path('<slug:id>/', peliculas, name = 'peliculas'),

]