from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [

    path('', include('main_app.urls')),
    path('social_vk/', include('social_django.urls', namespace='social')),
    path('accounts/', include('allauth.urls')),
    path('accounts/', include('accounts_app.urls')),
    path('shop/', include('shop_app.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

