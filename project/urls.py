from django.contrib import admin
from django.urls import path

from project.ninja import ninja_


@ninja_.get('/hello/')
def hello(request):
    return 'Hello world'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', ninja_.urls),
]
