from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView
from tokens.services.redirect import redirection


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('<str:short_url>/', redirection),
]
