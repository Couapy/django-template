from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.conf import settings


from . import views

urlpatterns = [
    path('account/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),

    # Social Django views
    path('', include("social_django.urls", namespace="social")),

    # My apps
    path('account/', include('account.urls')),
    path('', views.index),
] + static(
    settings.STATIC_URL,
    document_root=settings.STATIC_ROOT
) + static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)
