from . import views
from django.urls import path
from . views import file_storage_to_db
from django.conf.urls.static import static
from django.conf import settings 
from django.contrib import admin



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.file_storage_to_db, name = 'file_storage_to_db')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)