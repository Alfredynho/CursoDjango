from django.conf.urls import url
#importando de la clase index2 de views
urls de la aplicacion todo
from . import views

urlpatterns = [
    url(r'^$', views.index2, name='index2'),
]


