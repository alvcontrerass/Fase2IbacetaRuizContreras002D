from django.urls import path
from sitio_web import views

urlpatterns=[
    path('',views.inicio),
    path('catalogo/',views.catalogo),
    path('contacto/',views.contacto),
]