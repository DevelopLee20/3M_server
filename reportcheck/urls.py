from django.contrib import admin
from django.urls import path,include
import reportcheck.views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('myreport', reportcheck.views.myreport, name='myreport'),
    path('mycar', reportcheck.views.mycar, name='mycar'),

    path('image_api', reportcheck.views.image_views, name='image_api'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
