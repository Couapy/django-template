from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.conf import settings


from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),

    # Social Django views
    path('', include("social_django.urls", namespace="social")),

    # Account
    path('account/', include('account.urls')),
] + static(
    settings.STATIC_URL,
    document_root=settings.STATIC_ROOT
) + static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)
