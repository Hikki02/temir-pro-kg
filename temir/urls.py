"""temir URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

from django.urls import path, include

from django.conf.urls.static import static

from temir.conf import static_media

from temir import settings

from .conf.static_media import static_media_root
from .conf.yasg import urlpatterns as yasg_url

urlpatterns = [
                  path('admin/', admin.site.urls),
                  # Temir
                  path('', include('apps.users.urls')),
                  path('', include('apps.socials.urls')),
                  path('', include('apps.companies.urls')),
                  path('client_part/', include('apps.client_part.urls')),

                  path('api/v1/product/', include('apps.products.urls')),
                  path('api/v1/application/', include('apps.applications.urls')),
                  path('api/v1/orders/', include('apps.orders.urls')),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += yasg_url
# urlpatterns += static_media_root
