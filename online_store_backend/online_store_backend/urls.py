from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('store.urls')),  # Rutas de la API de Django
    path('', TemplateView.as_view(template_name='index.html')),  # Ruta para el frontend React
    path('', include('store.urls')),
]
