from django.contrib import admin
from .import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', include('imageupload.urls')),
    path('',views.index),
    path('darta/', include('authentication.urls')),
    # path('/', include('home.urls'))
] #+ #static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  