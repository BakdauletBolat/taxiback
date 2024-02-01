from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from taxiback.views import render_privacy_view, render_index

urlpatterns = [
    path('', render_index),
    path('admin/', admin.site.urls),
    path('privacy/', render_privacy_view),
    path('feedback/', include('form.urls')),
    path('api/', include([
        path('users/', include('apps.users.urls')),
        path('order/', include('apps.order.urls')),
        path('regions/', include('apps.regions.urls'))
    ]))

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
