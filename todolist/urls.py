from django.conf.urls import url, include
from django.contrib import admin
#url general de proyecto
urlpatterns = [
	url(r'^todo/', include('todo.urls')),
    url(r'^admin/', admin.site.urls),
]

