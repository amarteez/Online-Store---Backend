# urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('store.urls')),  # Rutas de tu API Django
    path('', include('store.urls')),      # Rutas adicionales de Django si las tienes
    path('', include('frontend.urls')),   # Rutas de tu aplicación frontend React
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
