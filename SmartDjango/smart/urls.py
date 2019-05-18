from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('', include('website.urls', namespace='website')),

    path('admin/', admin.site.urls),
]
