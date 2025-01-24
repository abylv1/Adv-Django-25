# task_management/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # URL для админки Django
    path('api/', include('core.urls')),  # Маршруты для API из приложения core
]
