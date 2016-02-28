from django.conf.urls import url
#importando de la clase index2 de views
from . import views

urlpatterns = [
    url(r'^$', views.index2, name='index2'),
]


