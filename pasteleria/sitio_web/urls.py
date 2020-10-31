from django.urls import path
from sitio_web import views

urlpatterns=[
    path('index/',views.index,name='index'),
    path('catalogo/',views.catalogo,name='catalogo'),
    path('contacto/',views.contacto,name='contacto'),
    path('enviar_formulario/', views.enviar_formulario, name='enviar_formulario')
]