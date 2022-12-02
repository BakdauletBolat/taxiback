from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('telemetry/', include('django_telemetry.urls')),
    path('api/', include([
<<<<<<< HEAD
        path('users/', include('apps.users.urls')),
        path('order/', include('apps.order.urls')),
        path('regions/', include('apps.regions.urls'))
=======
        path('users/', include('users.urls')),
        path('order/', include('order.urls')),
        path('regions/', include('regions.urls'))
>>>>>>> origin/release
    ]))

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
