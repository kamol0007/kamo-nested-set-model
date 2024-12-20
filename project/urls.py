from django.contrib import admin
from django.urls import path, include
from project import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('nested-set-model/', include('nested.urls'), name="nested-set-model"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
