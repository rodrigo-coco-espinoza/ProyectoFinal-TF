from django.contrib import admin
from django.urls import path
from planes_admin.views import home
from planes_admin.urls import *
from django.urls import include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('planes_admin/', include('planes_admin.urls')),
    path('', home),
]
