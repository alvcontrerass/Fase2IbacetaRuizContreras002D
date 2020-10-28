from django.urls import path
from sitio_web import views

urlpatterns=[
    path('',views.inicio,name='index'),
    path('catalogo/',views.catalogo,name='catalogo'),
    path('contacto/',views.contacto,name='contacto'),
]